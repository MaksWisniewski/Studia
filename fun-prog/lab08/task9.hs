import Control.Monad

-- W Haskellu żeby typ był monadą, to musi być funtkorem (Functor) i funktorem
-- aplikatywnym (Applicative). Jeśli potrafimy napisać funkcje return i (>>=),
-- to implementacja odpowiednich metod z klas Functor i Applicative może taka
-- jak poniżej (niezależnie od monady). Funkcja ap jest zdefiniowana w module
-- Control.Monad jako:
--
-- ap :: Monad m => m (a -> b) -> m a -> m b
-- ap m1 m2 = do { x1 <- m1; x2 <- m2; return (x1 x2) }
--
-- co można zapisać bezpunktowo (w tym wypadku *pointless*, a nie *pointfree*)
--
-- ap = flip (.) (flip (.) (return .) . (>>=)) . (>>=)

data StreamTrans i o a =
    Return a
    | ReadS (Maybe i -> StreamTrans i o a)
    | WriteS o (StreamTrans i o a)



instance Functor (StreamTrans i o) where
  fmap f m = m >>= return . f

instance Applicative (StreamTrans i o) where
  pure = return
  (<*>) = ap


-- Natomiast implementacje metod return i (>>=) trzeba napisać dla każdej
-- monady osobno.


instance Monad (StreamTrans i o) where
    -- return :: a -> m a
    return = Return


    -- (>>=) :: ma -> ( a -> mb ) -> mb

    (>>=) (Return x) f = f x
    -- (Return X) >>= f = f x
    -- (>>=) (Return x) = flip (Return x)

    (>>=) (WriteS o str) f = WriteS o $ str >>= f

    -- ReadS x
    -- x :: (maybe i -> ma)
    --                                              mb
    --                                    -----------------------
    --                                        ma        (a -> mb)
    --                                    ---------      --------
    (>>=) (ReadS x) f = ReadS (\maybe_i -> x maybe_i     >>= f )



-------------------------------------------------------------------------------------------------------------------------------------
---------------------------------TASK 4----------------------------------------------------------------------------------------------


-------------------------------------------------------------------------------------------------------------------------------------
---------------------------------TASK 5----------------------------------------------------------------------------------------------


-------------------------------------------------------------------------------------------------------------------------------------
---------------------------------TASK 6----------------------------------------------------------------------------------------------


