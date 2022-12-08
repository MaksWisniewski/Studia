let rec fold_left (f : ('a -> 'b -> ('a -> 'c) -> 'c))
                  (accumulator : 'a)
                  (xs : 'b list)
                  (kont : ('a -> 'c)) = 
        
        match xs with 
          | [] -> kont accumulator
          | x :: xs -> 
            let new_kont = fun new_acc -> fold_left f new_acc xs kont 
          in f accumulator x new_kont


let for_all pred xs = 
  let aux = fun acc x k -> 
    if pred x then k acc else false
  in fold_left aux true xs (fun x -> x)

let test1 = for_all ((&&) true) [true; true]
let test2 = for_all ((&&) true) [true; false; true]


let mult_list xs =
  let aux = fun acc x k -> if x = 0 then 0 else k (acc*x)
in fold_left aux 1 xs (fun x -> x)

let test3 = mult_list [0;1;2]
let test4 = mult_list [1;2;20;40]



let sorted xs = 
  let aux = fun (result, previous) x k -> 
    begin match previous with 
        | None   -> k (result, Some x)
        | Some a -> if x <= a then (false, None) else
                              k (result, Some x)
    end
  in fold_left aux (true, None) xs (fun x -> x) |> fst

(* k stands for continuation **)

let test5 = sorted [10;-1]
let test6 = sorted [1;2;3;4;5;6;7;8;9;10]