type 'a mylazy_data = 
  | Lazy of (unit -> 'a)
  | Busy
  | Ready of 'a

type 'a mylazy = 'a mylazy_data ref

let force (l : 'a mylazy) =
    match !l with
      | Ready v -> v
      | Busy -> failwith "evaluating"
      | Lazy f ->  l := Busy; let res = f () in l := (Ready res); res 
  
let fix (f : 'a mylazy -> 'a) : 'a mylazy =
    let (rek :'a mylazy) = ref Busy in
    rek := Lazy (fun () -> (f rek));  rek


type 'a lazy_list =
  | Nil
  | Cons of 'a * 'a lazy_list mylazy 


let head (ls : 'a lazy_list) =
  match ls with
  | Nil -> failwith "pustoooo"
  | Cons (l, ls) -> l

let tail (ls : 'a lazy_list) =
  match ls with
  | Nil -> failwith "puuuuusto"
  | Cons (l, ls) -> force ls


let stream_of_ones = fix (fun stream_of_ones -> Cons(1, stream_of_ones))


let nat_from n =
  let rec succ x =
    fun nat_stream -> Cons (x, fix (succ (x+1))) in
   force (fix (succ n))

let filter (p : 'a -> bool) (xs : 'a lazy_list) =
  let rec filt (source : 'a lazy_list) =
    (fun filter_stream -> 
      match source with
      | Nil -> Nil
      | Cons (l, ls) ->if p l then Cons (l, fix (filt (tail source)) ) else force (fix (filt (tail source))))
    in force (fix (filt xs))


let take_while (p : 'a -> bool) (xs : 'a lazy_list) =
  let rec take (source : 'a lazy_list) =
    (fun take_stream -> 
      match source with
      | Nil -> Nil
      | Cons (l, ls) ->if p l then Cons (l, fix (take (tail source)) ) else Nil)
    in force (fix (take xs))


let rec for_all p xs =
  match xs with
  | Nil -> true
  | Cons (x, _) ->
    p x && for_all p (tail xs)



let sing x =
  Cons (x, ref (Ready Nil))
let primes =
  let is_prime n source =
    source
    |> for_all (fun p -> n mod p <> 0) in
  let rec worker n curr =
    (fun prime_stream -> 
      if is_prime n curr
        then Cons (n, fix (worker (n+1) (Cons (n, ref (Ready curr)))))
        else force (fix (worker (n+1) curr))
    )
      in
  force (fix (worker 2 Nil))

