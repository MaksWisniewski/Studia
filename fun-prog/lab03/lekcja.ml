type formula = Bottom | Var of string | Impl of formula * formula


(* Zadanie 5 *)

(* gamma \- fi ==== under the assumptions of gamma we proof ??? phi *)

type theorem = theorem of Assumptions.t * Formula 

module Assumptions = Set.Make(Formula)

module Formula = struct
    type t = formula
    let compare = compare
end

let assumtions = function 
    Theorem (gamma,_) -> Assumptions.fold (fun x xs -> x :: xs) gamma []

let consequence = functin Theorem (_, x) -> x


(* zadanie 5 wzorcowka kowalewicza )





