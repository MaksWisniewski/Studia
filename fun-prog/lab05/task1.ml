let rec fix f x = f (fix f) x

let rec fix_with_limit limit f x = 
  if limit <= 0 then failwith "aaaa"
  else f (fix_with_limit (limit-1) f) x

let fix_memo f x = 
  let memo = Hashtbl.create(1000) in 
    let rec inner f x = match Hashtbl.find_opt memo x with
        | Some x -> x
        | None -> let ANSWER = f (inner f) x in 
        begin
          Hashtbl.add memo x ANSWER;
          ANSWER
        end
  in inner

let fib_f fib n = 
  if n <= 1 then n else
    fib(n-1) + fib(n-2)

let fib = fix fib_f
let fib_limit = fix_with_limit 100 fib_f
let fib_memo = fix_memo fib_f