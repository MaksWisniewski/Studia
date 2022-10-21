(* Version 1 *)
type t = string

let create pat = pat

let match_line line pat =
  let line_len = String.length line in
  let pat_len  = String.length pat in
  let rec aux pos =
    if pos + pat_len > line_len then
      false
    else if pat = String.sub line pos pat_len then
      true
    else
      aux (pos+1)
  in
  aux 0

(* Version 2 *)
(*
type t = Str.regexp

let create = Str.regexp

let match_line line pat = Str.string_match pat line 0
*)
