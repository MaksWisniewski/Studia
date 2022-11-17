type formula = 
| Var of string 
| False 
| Imp of formula * formula

module Ordered_formula = 
struct
type t = formula 
let compare = compare
end

module FormulaSet = Set.Make(Ordered_formula)
let set_to_list s = List.of_seq (FormulaSet.to_seq s)
let rec string_of_formula f =
    match f with 
    | False -> "_|_"
    | Var string -> string
    | Imp (f1, f2) -> let str1 = string_of_formula f1 in 
    (match f1 with 
        | Imp (_,_) -> "(" ^ str1 ^ ")"
        | _ -> str1) ^ "=>" ^ string_of_formula f2


let pp_print_formula fmtr f =
  Format.pp_print_string fmtr (string_of_formula f)

type theorem = 
  | Ax of   {ass : FormulaSet.t; f : formula}
  | ImpI of {ass : FormulaSet.t; f : formula; th : theorem}
  | ImpE of {ass : FormulaSet.t; f : formula; th1 : theorem; th2 : theorem}
  | NeqE of {ass : FormulaSet.t; f : formula; th : theorem}

let _assumptions = function
  | Ax    {ass} -> ass
  | ImpI  {ass} -> ass
  | ImpE  {ass} -> ass
  | NeqE  {ass} -> ass

let assumptions = (fun x -> _assumptions x |> set_to_list)
let consequence = function 
  | Ax    {f} -> f
  | ImpE  {f} -> f
  | ImpI  {f} -> f
  | NeqE  {f} -> f
  


let pp_print_theorem fmtr thm =
  let open Format in
  pp_open_hvbox fmtr 2;
  let list_from_set = set_to_list (_assumptions thm) in
  begin match list_from_set with
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
  Ax {ass = FormulaSet.singleton f; f = f}
  

let imp_i f thm = ImpI {ass = FormulaSet.remove f (_assumptions thm); f = Imp(f, consequence thm); th = thm}

let imp_e the1 the2 =
  let fa = match (consequence the1) with
  | Imp (pre, phi) -> if consequence the2 = pre then phi else failwith "impl_e inocrrect proof?"
  | _ -> failwith "impl_e inocrrect proof???" in

  ImpE {    
    ass = FormulaSet.union (_assumptions the1) (_assumptions the2);
    f = fa;
    th1 = the1; 
    th2 = the2 }

let bot_e f thm =
  match (consequence thm) with
  | False -> NeqE {ass = _assumptions thm; f = f; th = thm}
  | _ -> failwith "Raise with incorrect proof"
