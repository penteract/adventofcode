import Data.Char
import Data.List
import Control.Monad
import Control.Monad.State

pair [x,y] = (x,y)
unpair (x,y) = [x,y]


next :: Eq a => ([a], [(a,a)]) -> (a,([a],[(a,a)]))
next (nodes,edges) = let x = head $ filter (\n ->not $ any ((==n).snd) edges) nodes in
  (x,(filter (/=x) nodes, filter ((/=x).fst) edges))

coll ([],es) = []
coll nses = let (x,nx) = next nses in x:coll nx

main = do
  input <- map (pair.tail.filter isUpper) .  lines <$> readFile "input"
  let all = sort $ nub $ join $ map unpair input
  putStrLn $ coll (all,input)
  
  --putStrLn .unlines $ map show  input
  --putStrLn $all
  
