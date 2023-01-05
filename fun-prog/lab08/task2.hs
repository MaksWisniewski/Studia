{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use lambda-case" #-}
import Data.Char
import GHC.Types (IO(IO))
import GHC.IO.Handle (isEOF)
import System.IO

data StreamTrans i o a =
    Return a
    | ReadS (Maybe i -> StreamTrans i o a)
    | WriteS o (StreamTrans i o a)


toLower :: StreamTrans Char Char ()

toLower = ReadS (\ inp -> case inp of
                            Nothing -> Return ()
                            Just x  -> WriteS (Data.Char.toLower x) Main.toLower) 

                            

runIOStreamTrans :: StreamTrans Char Char a -> IO a
runIOStreamTrans (Return a) = return a
runIOStreamTrans (WriteS o x) = do putChar o
                                   runIOStreamTrans x 


runIOStreamTrans (ReadS x) = do isEND <- isEOF
                                if isEND 
                                    then do runIOStreamTrans $ x Nothing -- nic do przeczytania
                                    else do 
                                            c <- getChar
                                            runIOStreamTrans $ x (Just c)

-- runIOStreamTrans Main.toLower

main :: IO ()                                        
main = runIOStreamTrans Main.toLower    

-------------------------------------------------------------------------------------------------------------------------------------
---------------------------------TASK 3----------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------

-- listTrans :: StreamTrans i o a -> [i] -> ([o], a)


listTrans :: StreamTrans i o a -> [i] -> ([o], a)
listTrans (Return a) _ = ([], a)
listTrans (WriteS o t) is = (o : os, a)
  where
    (os, a) = listTrans t is
listTrans (ReadS f) [] = listTrans (f Nothing) []
listTrans (ReadS f) (x : xs) = listTrans (f (Just x)) xs

abc = take 3 $ fst $ listTrans Main.toLower ['A' ..]

aBc = fst $ listTrans Main.toLower ['a', 'B', 'c']

