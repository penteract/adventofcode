import Data.Char
import Control.Arrow
import Data.List
import Data.Maybe
import Control.Monad
--import Control.Monad.State
import qualified Data.Map as M

gi :: String -> Int
gi "" = 0
gi (c:rs) = (ord c - 48) + 10*gi rs

ri :: String -> (Maybe Int,String)
ri "" = (Nothing,"")
ri (d:rs) = (if d `elem` ['0'..'9'] then first (return.gi.foldl (flip (:)) [d]).(span (`elem` ['0'..'9']))  else ri) rs

get = unfoldr ((uncurry$flip$fmap.flip(,)).ri)

powset [] = [[]]
powset (x:xs) = let p = powset xs in p ++ map (x:) p

data T = T Int Int [T] [Int] deriving (Show)

procn :: Int -> [Int] -> ([T],[Int])
procn 0 s = ([],s)
procn x s = let (k,s')= proc s in first (k:) (procn (x-1) s')

proc :: [Int] -> (T,[Int])
proc (x:y:rs) = let (ch,rs') = procn x rs   in (T x y ch (take y rs'), drop y rs')

sm (T a b c d) = sum d +sum (map sm c)

vl (T a b [] d) = sum d
vl (T a b c d) = sum [vl (c!!(i-1)) | i<-d, i<=a ]
                                               
main = do
    f <- readFile "input"
    let l= get f
    let t = proc l
    putStrLn $ show (sm (fst t))
    putStrLn $ show (vl (fst t))
    
    
    

