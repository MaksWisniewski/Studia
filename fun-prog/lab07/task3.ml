
module Mid = 
struct
  type 'a t = 'a
  let return x = x
  let bind x f = f x
end

module Mod =
struct
  type 'a t = unit -> 'a
  let return x = fun () -> x
  let run a = a ()

  let bind x f = 
    fun () -> f (x ()) ()
end
