import Control.Monad
import Data.Maybe
import Data.Char


echo :: IO ()
echo = do
  x <- getLine
  if x == "" then return ()
  else do
    putStrLn $ map Data.Char.toLower x
    echo