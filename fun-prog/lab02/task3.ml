(* Write a function that generates all sufixes of a given list *)

let rec sufixes_aux = function
    | [] -> []
    | hd::tl -> tl :: sufixes_aux tl

let sufixes xs = xs::sufixes_aux xs

let rec suffixes = function
    | [] -> []
    | x :: xs as lst -> lst :: (suffixes xs)

let _ = sufixes (1::2::3::5::6::[])

(* Write a function that generates all prefixes of a given list *)

let rec prefixes = function 
    | [] -> [[]]
    | x::xs -> [] :: ( List.map (fun s -> x :: s) (prefixes xs) )

let _ = prefixes (1::2::3::5::6::[])
