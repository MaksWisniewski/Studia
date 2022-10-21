(* fun x -> x   has type of 'a -> 'a *)

(*   (fun (x : int) -> x *)

let e1 f g x = x |> g |> f

let e2 x y = x

let e3 x y = if x = y then x else x
