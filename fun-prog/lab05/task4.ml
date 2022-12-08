type 'a dllist = 'a dllist_data lazy_t
and 'a dllist_data =
  { prev : 'a dllist
  ; elem : 'a
  ; next : 'a dllist
  }

let prev = function
  | lazy (dll) -> dll.prev

let elem = function
  | lazy (dll) -> dll.elem

let next = function
  | lazy (dll) -> dll.next

let create x =
  let rec s = lazy {next = s; elem = x; prev = s} in s

let rec gen (prev : 'a dllist) xs first =
  match xs with
  | [] -> first, prev
  | x :: xs -> 
    let last = ref (create x) in
    let rec z = lazy begin
        let (a,b) = gen z xs first in
        last := b; {prev = prev; elem = x; next = a} 
    end in
    let k = (Lazy.force z) in lazy k, (fun last -> last.contents) last 


let rec of_list xs =
  match xs with
  | [] -> failwith "empty"
  | x :: xs -> 
    let rec first = lazy begin
      let (a,b) = gen first xs first in
      {prev = b; elem = x; next = a}
    end in first

let x = (of_list [1 ; 2 ; 3;]);;


(* TASK 5 *)

let rec left_int v p =
  let rec g = lazy {prev = left_int (v-1) g ; elem = v; next = p} in g

let rec right_int v p=
  let rec g = lazy {prev = p; elem = v; next = right_int (v+1) g} in g

let rec integers = lazy {prev = left_int (-1) integers; elem = 0; next = right_int 1 integers}
  