sn = 18

powl x y = pl4 - 5
  where rid = x+10
        pl1 = rid*y
        pl2 = pl1+sn
        pl3 = (pl2 * rid) `mod` 1000
        pl4 = pl3 `div` 100

ns = [1..300]

z3 = zip3

uc3 f (a,b,c) = f a b c

grid = [[0 | x <- 0:ns] | y <- 0:ns ] : [[powl x y | y <- [1..300]] | x <- [1..300]] : map f (zip [2..] $ zip grid $ tail grid)

f (n,(centers, corners)) = zipWith (f' n) [1..] $ map (uc3 z3) $ z3  (tail $ map tail centers) (tail corners) (map tail corners)
  where
    f' n x cs = zipWith f'' [1..] cs
      where
        f'' y (cen,cor1,cor2) = cor1+cor2-cen + powl x y + powl (x+n-1) (y+n-1)

gi :: [[[((Int,(Int,Int,Int)))]]]
gi = zipWith (\gn g -> zipWith (\ l x -> zipWith (\ v y -> (v,(x,y,gn))) l [1..]  )g [1..]) [0..] grid

main = do
  putStrLn "hi"
  print $ grid !! 3 !! 19
  putStrLn $ (+) 4 3
  --  putStrLn $ show $ thrs (((+).).(+)) (grid !! 0 !! 0)
  -- print $ foldl1 max $ map (foldl1 max) gi
  
  print $ concat $ map (filter (\(x,y)-> x>87)) (concat (take 301 gi))
  
