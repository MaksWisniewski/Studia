type formula = False | Var of String | Imp of formula * formula

let string_of_formula f =
    match f with 
    | False -> "_|_"
    | Var of String -> String
    | Imp (f1, f2) -> let str1 = string_of_formula f1 in 
    (match f1 with 
        | Imp (_,_) -> "(" ^ str1 ^ ")"
        | _ -> str1) ^ "=>" ^ string_of_formula f2

let pp_print_formula fmtr f =
  Format.pp_print_string fmtr (string_of_formula f)

  module FormulaSet = Set.Make(Ordered_formula)

  (* tutaj istotne jest zaprogramowanie orderde_formula*)
  
type theorem = 
  | Proof_1 of FormulaSet.t * formula
  | Proof_2 of theorem * FormulaSet.t * formula
  | Proof_3 of theorem * theorem * FormulaSet.t * formula
  | Proof_4 of theorem * FormulaSet.t * formula


  let assumptions thm = 
    match thm with
        | Proof_1 (a, _) ->a
        | Proof_2 (_, a, _) -> a
        | Proof_3 (_, _, a, _) -> a
        | Proof_4 (_, a, _) -> a

let consequence thm = 
    match thm with
        | Proof_1 (_, c) -> c
        | Proof_2 (_, _, c) -> c
        | Proof_3 (_, _, _, c) -> c
        | Proof_4 (_, _, c) -> c

let pp_print_theorem fmtr thm =
  let open Format in
  pp_open_hvbox fmtr 2;
  begin match assumptions thm with
  | [] -> ()
  | f :: fs ->
    pp_print_formula fmtr f;
    fs |> List.iter (fun f ->
      pp_print_string fmtr ",";
      pp_print_space fmtr ();
      pp_print_formula fmtr f);
    pp_print_space fmtr ()
  end;
  pp_open_hbox fmtr ();
  pp_print_string fmtr "⊢";
  pp_print_space fmtr ();
  pp_print_formula fmtr (consequence thm);
  pp_close_box fmtr ();
  pp_close_box fmtr ()

let by_assumption f = 
  Proof_1 ((FormulaSet.singleton f), f)

let imp_i f thm = 
  Proof_2(
      thm,
      FormulaSet.remove f (assumptions thm),
      Impl(f, (consequence thm))
  )

exception Incorrect_proof

let imp_e thm1 thm2 = 
  Proof_3(
      thm1,
      thm2,
      FormulaSet.union (assumptions thm1) (assumptions thm2),
      match (consequence thm1) with
          | Impl (_, phi) -> phi
          | _ -> raise Incorrect_proof
  )

let bot_e f thm = 
  Proof_4 (
      thm, 
      assumptions thm, 
      f
  )
