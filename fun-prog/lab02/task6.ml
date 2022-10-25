let rec flatten = function
  | [] -> []
  | x :: xs -> x @ flatten xs

let rec insert x xs =
    match xs with
        | [] -> [[x]]
        | head :: tail -> (x :: xs) :: (List.map (fun el -> head :: el) (insert x tail));;

let rec perm xs =
    match xs with
        | [] -> [xs]
        | head :: tail -> List.flatten (List.map (insert head) (perm tail));;