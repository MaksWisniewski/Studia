(* task 3 *)

exception EXCEPTION

let for_all pred xs =
  let aux = fun accumulator x -> if pred x then accumulator 
  else raise EXCEPTION in 
    try List.fold_left aux true xs with EXCEPTION -> false

let mult_list xs = 
  let aux = (fun accumulator x -> if x = 0  then raise EXCEPTION 
                                            else accumulator * x) 
  in try List.fold_left aux 1 xs with EXCEPTION -> 0

let sorted xs =
  let rec aux = (fun (answer, previous) x ->
    begin match previous with 
    | None   -> (answer, Some x)
    | Some a -> if x <= a then raise EXCEPTION 
                          else (answer, Some x)
    end) in try List.fold_left aux (true, None) xs |> fst with EXCEPTION -> false


let _ = for_all ((&&) true) [true; true; true; false; false]
let _ = mult_list [1;2;3;4;5;6]
let _ = mult_list [0;1]
let _ = sorted [1;2;3]
let _ = sorted [3;1]