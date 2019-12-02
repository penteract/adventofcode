import Data.Char
import Control.Arrow
import Data.List
import Data.Maybe
import Data.Function
import Control.Monad
--import Control.Monad.State
import qualified Data.Map as M

gi :: String -> Int
gi "" = 0
gi "-" = 0
gi (c:rs) = (ord c - 48) + 10*gi rs

ri :: String -> (Maybe Int,String)
ri "" = (Nothing,"")
ri (d:rs) = (if d `elem` ('-':['0'..'9']) then first (return.(if d=='-' then negate else id).gi.foldl (flip (:)) [d]).(span (`elem` ['0'..'9']))  else ri) rs

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

topos [x,y,dx,dy] = ((x,y),(dx,dy))

atn n ((x,y),(dx,dy)) = (x+n*dx,y+n*dy)

mp2 :: (a -> b) -> (a,a) -> (b,b)
mp2 = join (***)

swp = uncurry $ flip (,)

type P = (Int,Int)

{-
bb :: [(Int,Int)] -> ((Int,Int),P)
bb xs = bb' xs ((-100000,-100000),(100000,100000)) -- ((right,top),(left,bot))
  where
    bb' [] = id
    bb' (x:xs) = ((mp2$ max x) *** (mp2$ min x)) ---- on ar mp2 max min --
-}

in2 = join ar

bb = foldl (\ (a,b) x -> (in2 max x a, in2 min x b)) ((-100000,-100000),(100000,100000))
    

ar :: (a -> b -> c) -> (d-> e ->f) -> (a,d) -> (b,e) -> (c,f)
ar f g x = uncurry (***) ((f***g) x)

sz :: (P,P) -> Int
sz =  uncurry (+) . uncurry ((-) `ar` (-))



draw ps = let cor@((r,t),(l,b)) = bb ps
              (w,h) = uncurry ((-) `ar` (-)) cor
              ps' =nub $ sort $ map (\ (x,y) -> (y-b,x-l) ) ps in
          show ps'++ unlines ( dolines ps' w 0 0)

dolines [] w n h = [replicate (n-w) '#']
dolines ps@((y,x):rs) w n h 
  | n > w         = "" : dolines ps w 0 (h+1)
  | h>=y && n==x  = let (he:ta) = dolines rs w (n+1) h in ('#' : he) : ta
  | otherwise     = let (he:ta) = dolines ps w (n+1) h in  (' ' : he) :ta


-- search (low,mid] and [mid,high)
tersearch score high mid low
  | high == low+2 = mid
  | otherwise   = let q1 = (low + mid) `div` 2
                      q2 = (mid + high + 1) `div` 2  in
                  if score q1 < score mid then tersearch score low q1 mid else
                    if score q2 < score mid then tersearch score mid q2 high else
                      tersearch score q1 mid q2

main = do
    f <- readFile "input"
    let l= map (topos.get) (lines f)
        n = 10942-- tersearch (\n -> sz.bb.map (atn n)$ l) (-200) 10000 12200
    
    putStrLn$ show n
    putStrLn $ show $ bb $ map (atn n) l
    putStrLn $ show $ bb $ map (atn n) l
    putStrLn $ show $ sz $ bb $ map (atn n) l
    putStr $ draw $ map (atn n) l
