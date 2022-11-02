(* Sublist of l := are obtained from l by removing some of it's elements.
    * type : alpha list -> alpha list list
    * sublist [] = [[]]
    * if list = head::tail
        then any sublist of list 
        ---> either is some sublist of tail
        ---> or is obtained from tail by putting head in the front. *)



let rec sublist = function
    | [] -> [ [] ]
    | hd::tl -> let temp = sublist tl in 
                temp @ List.map (fun x -> hd::x) temp

let _ = sublist (1::2::[])
