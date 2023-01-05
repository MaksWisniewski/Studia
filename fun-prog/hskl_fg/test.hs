import Prelude


double x = x + x
doubleUs x y = x*2 + y*2

doubleSmall x = if x > 100
                    then x
                    else double x


-- list comprehension
-- take first 10 even natural numbers
-- [x*2 | x <- 1..10]]

boomBang xs = [ if x `mod` 2 == 0 then "BOOM" else "bang" | x <- xs, x>=10]


-- typy

--   nazwa  = konstruktor argumenty
data Person = Mk_Person String Int

brian :: Person
brian = Mk_Person "brian" 42


-- cos tam, --- top class instance

data Z = X String | Y
    deriving (Show)

instance Eq Z where
    -- pattern matching
    X a == X b = a == b
    Y == Y = True
    _ == _ = False

j :: Z
j = X "TESTING"

-- type classes
class ToString  a where
    toString :: a -> String

instance ToString Int where
    toString = show

instance ToString Bool where
    toString True  = "True"
    toString False = "False"