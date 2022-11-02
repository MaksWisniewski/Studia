(* last intiger is a rank*)

type 'a leaf =
    | Leaf
    | Node of 'a leaf * 'a leaf * int
