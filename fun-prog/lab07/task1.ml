

type 'a t = int -> 'a * int

let rand_val s = 16807 * (s mod 127773) - 2836 * (s / 127773)

let gen_seed s =
  let temp = rand_val s in 
    if temp > 0 then temp else temp + 2147483647


let return ( x : 'a ) = fun ( s : int ) -> x, s

let run ( m : 'a t) ( s : int ) = m s |> fst

let rand s = (rand_val s, gen_seed s)

let bind ( x : 'a t) ( f : 'a -> 'b t) : 'b t =
  fun s -> let (v, ns) = x s in f v ns

let ( let* ) = bind


let rec ref xs n =
  if n = 0 then List.tl xs else List.hd xs :: (ref (List.tl xs) (n-1))



let rec shuffle (xs : 'a list) (acc : 'a list) : 'a list t =
  match xs with
  | [] -> (return acc)
  | y :: ys -> 
    let* r = rand in 
    let i = (r mod (List.length xs)) in 
        shuffle (ref xs i) (List.nth xs i :: acc) 

let _ = run (shuffle [1;2;3;4;5;6;] []) (rand_val 24)