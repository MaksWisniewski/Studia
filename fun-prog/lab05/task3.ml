type 'a inftree =
| Tree of (unit -> 'a inftree)  * 'a * (unit -> 'a inftree)

let left (Tree (l,v,r)) = l () 

let right (Tree (l,v,r)) = r () 



(* let value (Tree (l,v,r)) = v *)



let gen_left_range ((a, b), (c, d))  =
  ((a, b), (a+c, b+d))



let gen_right_range ((a, b), (c, d))  =
  ((a+c, b+d), (c, d))
  

let gen_value_range ((a, b), (c, d)) =
  (a+c, b+d)

let value (Tree (_, v, _)) =
  gen_value_range v

let rec gt v  =
  let l = fun () -> gt (gen_left_range v) in
  let r = fun () -> gt (gen_right_range v) in
  Tree (l, v, r)


let all =
  gt ((0,1), (1,0))
