(* task 4 : fold left in continuation passing style *)

let rec fold_left (f : ('a -> 'b -> ('a -> 'c) -> 'c))
                  (accumulator : 'a)
                  (xs : 'b list)
                  (kont : ('a -> 'c)) = 
        
        match xs with 
          | [] -> kont accumulator
          | x :: xs -> 
            let new_kont = fun new_acc -> fold_left f new_acc xs kont 
          in f accumulator x new_kont

(* example interface *)


let _ = fold_left (fun acc x k -> k (acc * x)) 1 [1;2;3;4;5;6] (fun x -> x)