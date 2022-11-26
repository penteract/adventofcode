import Control.Arrow(first,second)

import qualified Data.Vector as V
import qualified Data.Map.Strict as M

import Data.Int
import Data.Tuple
import Data.List
import Data.Char
import Data.Function

import Control.Monad.State

main :: IO ()
main = do
  {-
  -- This searches the whole space,
  -- compiled with -O2, it takes ~13 minutes
  let m1 = (mp' 100000000)
  print (M.size m1)
  let revm = foldl' (\ mp (k,(_,x)) -> M.alter (Just.(+1).sum ) x mp) M.empty (M.toList m1)
  print (M.size revm)
  let m = trim [a | (a,_)<-M.toList m1, revm M.!? a == Nothing ] m1 revm
  print (M.size m)
  -}
  s <- readFile "out3.txt"
  let m = read s :: M.Map Int (Int,Int)
  let samples = groupBy ((==) `on` snd) (sortOn snd$ toCycles m)
  putStrLn "(Cycle length, number of cycles):"
  let cts = map (\ xnms -> (snd (head xnms),sum (map (snd.fst) xnms) `div` snd (head xnms))) samples
  putStr$unlines$map show cts
  putStrLn "Sample cycle for each cycle length"
  putStr$unlines $ map (\ x -> (show$ snd x) ++":\n"++ pp (fst$fst x)) $ map head samples


toCycles :: Ord a => M.Map a (Int,a) -> [((a,Int),Int)]
toCycles mp = map (uncurry findCycle) (M.toList mp)
  where
    findCycle x (n,y) = findCycle' (x,n) (n,y)
    findCycle' (x,n) (m,y) = if x==y
      then ((x,n),m)
      else findCycle' (x,n) (first (+m) (mp M.! y))

-- | Split a list into chunks of /n/ elements
chunkList :: Int -> [a] -> [[a]]
chunkList _ [] = []
chunkList n xs = as : chunkList n bs where (as,bs) = splitAt n xs

pp :: Int -> String
pp n = let v = V.toList (fromInt n) in unlines$ map (map (chr.(+48))) (chunkList 3 v)

-- Remove vertices that aren't part of a cycle
trim :: Ord a => [a] -> M.Map a (Int,a) -> M.Map a Int -> M.Map a (Int,a)
trim [] m rev = m
trim (x:xs) m rev = if indegree==1 then trim (y:xs) m' rev
    else trim xs m' (M.insert y (indegree-1) rev)
  where
    y = snd (m M.! x)
    m' = M.delete x m
    indegree = rev M.! y

type PreGrid = V.Vector (Int,Int)
-- during construction -1 = not yet filled
type Grid = V.Vector Int


fp :: Eq a => (a->a) -> a -> a
fp f x = let y = f x in if y==x then x else fp f y

steps :: Grid -> (Int,Grid)
steps = until (\(_,g)->g V.! 8 == 0) (\(a,b) -> first (+a) (step b) ) . step

step :: Grid -> (Int,Grid)
step g = (steps, g'')
  where
    steps = 10 - V.maximum g
    g' = V.map (+steps) g
    g'' = fp (\ g -> V.imap (\ i x -> if x==0 || x==10 then 0 else
      min 10 (x+sum [fromEnum ((g V.! j)==10) | j <- ns i])) g) g'

toInt :: Grid -> Int
toInt = V.foldr (\ a b -> a + 16*b) 0

fromInt :: Int -> Grid
fromInt = V.unfoldrExactN 9 (\ n -> swap  (n `divMod` 16))

nonadj :: Grid -> Bool
nonadj g = V.ifoldr (\i x b -> (x==9 || x==0 || x < 9-sum [fromEnum ((g V.! j)==9) | j <- ns i]) && b) True g

-- Weirdly, M.fromAscList appears to be slower than M.fromList
mp' :: Int -> M.Map Int (Int,Int)
mp' n = M.fromList [(toInt m, second toInt (steps m)) | m <- map (snd . steps) as2 ]
  where
    -- don't use a top-level definition to hopefully save memory
    as2 = take n $ filter nonadj $ map (V.unfoldrExactN 9 (\ n -> swap  (n `divMod` 10))) [(0::Int) .. (10^8 - 1)]




ns :: Int -> [Int]
ns 0 = [1,3,4]
ns 1 = [0,2,3,4,5]
ns 2 = [1,4,5]
ns 3 = [0,1,4,6,7]
ns 4 = [0,1,2,3,5,6,7,8]
ns 5 = [1,2,4,7,8]
ns 6 = [3,4,7]
ns 7 = [3,4,5,6,8]
ns 8 = [4,5,7]


ns4 :: Int -> [Int]
ns4 0 = [1,3]
ns4 1 = [0,2,3,5]
ns4 2 = [1,5]
ns4 3 = [0,1,6,7]
ns4 4 = [0,1,2,3,5,6,7,8]
ns4 5 = [1,2,7,8]
ns4 6 = [3,7]
ns4 7 = [3,5,6,8]
ns4 8 = [5,7]

pnodes :: Int -> [Int]
pnodes 0 = []
pnodes 1 = [0]
pnodes 2 = [1]
pnodes 3 = [0,1]
pnodes 4 = [0,1,2,3]
pnodes 5 = [1,2,4]
pnodes 6 = [3,4]
pnodes 7 = [3,4,5,6]
pnodes 8 = [4,5,7]