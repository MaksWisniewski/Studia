
type symbol = string

type 'v term =
  | Var of 'v
  | Sym of symbol * 'v term list


let bind t sub = 
  let rec r_ = function
    | Var v -> sub v
    | Sym (s, xs) -> Sym (s, List.map r_ xs)
  in r_ t


(* value assesment and evaluation??? *)
let example = Sym("a", [Var false])
let _ = bind example (fun x -> Var (not x))
