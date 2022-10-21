let rec fib n =
  if n <= 1 then n
  else fib (n-1) + fib (n-2)

let _ =
  if Array.length Sys.argv <= 1 then
    Printf.printf "Usage: %s NUMBER\n" Sys.argv.(0)
  else
    Sys.argv.(1) |> int_of_string |> fib |> Printf.printf "%d\n"
