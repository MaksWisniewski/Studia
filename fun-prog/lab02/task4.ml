(* 1. implement merge function*
  * example usage : merge (<=) [1;2;3] [4;5;6]*)

let rec merge ?(cmp = (<=)) xs ys =
  match (xs, ys) with
  | [], _ -> ys
  | _, [] -> xs
  | x :: xs', y :: ys' ->
          if cmp x y then x :: merge cmp xs' ys else y :: merge cmp xs ys'
  

(* rewrite merge to be tail recursive funciton*)

let rec tail_merge ?(cmp = (<=)) xs ys acc =
  match (xs, ys) with
  | [], _ -> acc @ ys
  | _, [] -> acc @ xs
  | x :: xs', y :: ys' ->
    if cmp x y then tail_merge ~cmp:cmp xs' ys (acc@[x]) else tail_merge ~cmp:cmp xs ys' (acc@[y])

(* example: tail_merge (<=) [1;2;3] [4;5;6] [];; *)

let rec take k = function 
    | [] -> []
    | x :: xs -> if k = 0 then [] else x :: take (k - 1) xs

let rec drop k = function
    | [] -> []
    | (_ :: t) as lst -> if k = 0 then lst else drop (k - 1) t


let rec merge_sort = function
    | [] -> [] 
    | [x] -> [x]
    | xs ->
      let lenn = List.length xs / 2 in 
      merge (merge_sort (take lenn xs)) (merge_sort (drop lenn xs))

let _ = merge_sort [69;1;2;3;4;5;6;7;8]
