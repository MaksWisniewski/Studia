module type OrderedType = sig
  type t
  val compare : t -> t -> int
end

module type S = sig
  type key
  type t
  (** permutacja jako funkcja *)
  val apply : t -> key -> key
  (** permutacja identycznościowa *)
  val id : t
  (** permutacja odwrotna *)
  val invert : t -> t
  (** permutacja która tylko zamienia dwa elementy miejscami *)
  val swap : key -> key -> t
  (** złożenie permutacji (jako złożenie funkcji) *)
  val compose : t -> t -> t
  (** porównywanie permutacji *)
  val compare : t -> t -> int
end
  
module Make(Key : OrderedType) = struct
  type key = Key.t

  module MyMap = Map.Make(Key)

  type t = key MyMap.t * key MyMap.t

  let apply ((map, inv_map) : t) k = 
    match (MyMap.find_opt k map) with
    | None -> k
    | Some x -> x

  let id : t = (MyMap.empty, MyMap.empty)

  let invert ((map, inv_map) : t) : t = (inv_map, map)

  let swap x1 x2 : t =
    let (map, inv_map) = id in 
      (MyMap.add x2 x1 (MyMap.add x2 x1 map), MyMap.add x2 x1 (MyMap.add x1 x2 inv_map))

  let compose ((map1, invMap1) : t )((map2, invMap2) : t) : t =
    let f1 key e1 e2 = 
      match e1, e2 with
      | None, None -> None
      | None, Some x2 -> Some x2
      | Some x1, _ -> 
        let app = apply (map2, invMap2) x1 
        in if app = key then None else Some app
    in let f2 key e1 e2 = 
        match e2, e1 with
        | None, None -> None
        | None, Some x2 -> Some x2
        | Some x1, _ -> 
          let app = apply (invMap1, map1) x1 
          in if app = key then None else Some app
    in let r1 = MyMap.merge f1 map1 map2
    in let r2 = MyMap.merge f2 invMap1 invMap2
  in (r1, r2)

  let compare ((map1, map1i) : t)((map2, map2i) : t) = MyMap.compare Key.compare map1 map2
end