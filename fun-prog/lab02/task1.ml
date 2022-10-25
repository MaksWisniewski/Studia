(*lenght*)
let len xs = List.fold_right (fun _ x -> x + 1) xs 0

(* reverse *)

let rev xs = List.fold_right :: xs []