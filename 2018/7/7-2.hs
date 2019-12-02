import Data.Char
import Data.List
import Control.Monad
import Control.Monad.State
import System.IO.Unsafe
pair [x,y] = (x,y)
unpair (x,y) = [x,y]


-- next :: Eq a => ([a], [(a,a)]) -> (as,([a],[(a,a)]))
next (nodes,edges) = filter (\n ->not $ any ((==n).snd) edges) nodes


coll _ done [] _  rs = rs
coll time done nodes edges rs=
  let (d', finished) = partition ((/=time).snd) done
      e' =  filter (\e -> all (\n -> (fst n /= fst e)) finished) edges
      toAdd = take (5-length d') $ next (nodes,e')
      in
    coll (time+1)
      (map (\c -> (c,time + ord c - 4)) (reverse toAdd) ++ d')
      (filter (not . (`elem` toAdd)) nodes) e'
      (zip toAdd (repeat time) ++ rs)


main = do
  input <- map (pair.tail.filter isUpper) .  lines <$> readFile "input"
  let all = sort $ nub $ join $ map unpair input
  -- putStrLn $ coll (all,input)
  
  putStrLn .unlines $ map show $ coll 0 [] all input []
  putStrLn (' ':all)
  
  putStr $ unlines [a: [if (a,b) `elem` input then '<' else '#' | b <- all] | a <- all]
  putStrLn (' ':all)
  --putStrLn $all
  
