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
