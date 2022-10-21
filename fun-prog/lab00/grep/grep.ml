let rec grep pat =
  match read_line () with
  | exception End_of_file -> ()
  | line ->
    if Matcher.match_line line pat then
      print_endline line;
    grep pat

let _ =
  if Array.length Sys.argv <= 1 then
    Printf.eprintf "USAGE: %s PATTERN\n" Sys.argv.(0)
  else
    grep (Matcher.create Sys.argv.(1))
