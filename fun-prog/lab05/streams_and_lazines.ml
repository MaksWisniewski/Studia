

type 'a stream = 
  Cons of 'a * (unit -> 'a stream)

let rec from n = Cons (n, fun () -> from (n+1))
let rec nats = from 0
let hd (Cons (h, _)) = h
let tl (Cons (_, tl)) = tl ()
let rec take n s =
  if n=0 then [] else hd s :: take (n-1) (tl s)
let rec drop (n : int) (s : 'a stream) = 
  if n = 0 then s else drop (n-1) (tl s)


(* that produces stack overflow? for n = 1e8 *)

let rec square (Cons (head, tail)) = 
  Cons (head*head, fun () -> square (tail ()))

let rec sum (Cons (head1, tail1)) (Cons (head2, tail2)) = 
  Cons (head1+head2, fun() -> sum (tail1 ()) (tail2 ()))

let rec map f (Cons (head, tail)) = 
  Cons (f head, fun () -> map f (tail ()))

let rec map2 f (Cons (h1, tf1)) (Cons (h2, tf2)) =
  Cons (f h1 h2, fun () -> map2 f (tf1 ()) (tf2 ()))

let square' = map (fun x -> x*x)
let sum' = map2 (+)

let rec fibs =
  Cons(1, fun () ->
    Cons(1, fun () ->
      sum fibs (tl fibs)))



(*  Unfortunately, it's highly inefficient. Every time we 
    force the computation of the next element,
    it required recomputing all the previous elements, twice: 
    once for fibs and once for tl fibs in the last line of the definition.
    By the time we get up to the 30th number,  *)

(* L A Z I N E S S *)

(* module Lazy : 
      sig
          type 'a t = 'a lazy_t
          val force : 'a t -> 'a
      end

let fib30 = Lazy.force 
                lazy (take 30 fibs |> List.rev |> List.hd)

                let fib30fast = Lazy.force fib30lazy *)


(* to do : 
   https://www.kuniga.me/blog/2016/11/18/streams-and-lazy-evaluation-in-ocaml.html *)