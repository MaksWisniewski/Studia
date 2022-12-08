open Proc


let rec echo k =
  recv (fun v ->
  send v (fun () ->
  echo k))



let rec map (f : 'i -> 'o) (cont : 'a) =
  recv (fun v ->
  send (f v) (fun () ->
    map f cont))
    
let rec map f cont = 
  recv (fun v ->
    send f v (fun () -> map f cont))




let rec filter (p : 'i -> bool) (cont : 'a) =
  recv (fun v ->
    if p v 
      then
        send v (fun () ->
          filter p cont)
      else
        filter p cont)

let rec nats_from (n : int) (cont : 'a -> ('a, 'i, 'o) ans) =
    send n (fun () -> nats_from (n+1) cont) 

  

let rec sieve (cont : 'a -> ('a, 'i, 'o) ans) =
  recv (fun v ->
  send v (fun () ->
  ((filter (fun x -> (x mod v) <> 0)) >|> sieve) cont))




let _ = run (nats_from 2 >|> sieve >|> map string_of_int)