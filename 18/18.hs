import Data.Char
import Control.Arrow
import Data.List
import Data.Maybe
import Control.Monad
--import Control.Monad.State
import qualified Data.Map as M
import Data.Bits
import System.IO.Unsafe
--import 



gi :: String -> Int
gi "" = 0
gi (c:rs) = (ord c - 48) + 10*gi rs

ri :: String -> (Maybe Int,String)
ri "" = (Nothing,"")
ri (d:rs) = (if d `elem` ['0'..'9'] then first (return.gi.foldl (flip (:)) [d]).(span (`elem` ['0'..'9']))  else ri) rs

get = unfoldr ((uncurry$flip$fmap.flip(,)).ri)


z3 :: [a] -> [[a]]
z3 (x:xs) =  map tol $ zip3 (x:xs) xs (tail xs)

tol (a,b,c) = [a,b,c]

surr ::[[Char]] -> [[Char]]
surr xs = affix $ map (('@':).(++"@")) xs
  where affix xs = let l=replicate (length (head xs)) '@' in l : xs++[l]

count c = length . filter (==c)

z9 xss = map transpose (z3 $ map z3 (surr xss))

extr ::[[Char]] -> [[(Char,[Char])]]
extr xss = map (map ((\ ls -> (ls!!4,take 4 ls ++ drop 5 ls) ).join)) (z9 xss)

next ('.',xs) = if count '|' xs >=3 then '|' else '.'
next ('|',xs) = if count '#' xs >=3 then '#' else '|'
next ('#',xs) = if count '#' xs >=1  && count '|' xs >=1 then '#' else '.'
next (c,rs) = error (show (c,rs))

type MP =M.Map [[Char]] Int

don :: ([[Char]],MP,Int) -> ([[Char]],MP,Int)
don (xss,m,n) = if M.lookup xss m /=Nothing then error (show $(n,M.lookup xss m)) else 
    let e =  map (map next) (extr xss) in
      (e,M.insert xss n m,n+1)

main = do
    f <- readFile "input"
    let l= lines $ f
    -- print (extr l)
    let e = scanl (\ a b -> don a) (l,M.empty,0) [1..]
    --putStr$ unlines $ (map (unlines.(\(s,d,f)->s))) e
    let (s,_,_) = e!!412
    putStr $unlines s
    print $ (count '|' (join s))*(count '#'$join s)
--    print "hi"



