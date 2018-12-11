
data Rect = Rect {
  lef::Int,
  rig::Int,
  top::Int,
  bot::Int}


data Dir = H | V deriving Show
alt H = V
alt V = H

-- B V n t1 t2 means l--(n-1),t--b is t1 and n--r,t--b is t2
data Tree a = B Dir Integer (Tree a) (Tree a)  | Leaf a deriving Show

type Pos = (Integer,Integer)
type Box = (Pos,Pos)



{-
Quad a = Quad {
  tl :: Tree a,
  tr :: Tree a,
  bl :: Tree a,
  br :: Tree a,
  cutx :: Int,
  cuty :: Int}
-}



foldT :: (Dir -> b -> b -> b) -> (Integer-> Integer -> a ->b) -> Tree a -> b
foldT = foldT' outer 
 where foldT' ((l,r),(t,b)) f g (Leaf a) = g (r-l) (b-t) a
       foldT' ((l,r),v) f g (B H n t1 t2) = f H (f' ((l,n),v) t1) (f' ((n,r),v) t2)
          where f' bx = foldT' bx f g
       foldT' (v,(t,b)) f g (B V n t1 t2) = f V (f' (v,(t,n)) t1) (f' (v,(n,b)) t2) 
          where f' bx = foldT' bx f g


--crop1 :: (Int,Int) -> Int -> (Int,Int)

addBox :: Box ->  (a -> a) -> Box -> Tree a -> Tree a
addBox ps@((l,r),(t,b)) f bx@((tl,tr),(tt,tb)) lf@(Leaf dat)
  | l>tl = addBox ps f bx $ B H l lf lf
  | t>tt = addBox ps f bx $ B V t lf lf
  | r<tr = addBox ps f bx $ B H r lf lf
  | b<tb = addBox ps f bx $ B V b lf lf
  | otherwise = Leaf $ f dat
addBox ps@((l,r),(t,b)) f bx@((tl,tr),v) (B H n t1 t2)
  | n<=l  = B H n t1 $ addBox ps f ((n,tr),v) t2
  | n>=r  = B H n (addBox ps f ((tl,n),v) t1) t2
  | otherwise = B H n (addBox ((l,n),(t,b)) f ((tl,n),v) t1) (addBox ((n,r),(t,b)) f ((n,tr),v) t2)
addBox ps@((l,r),(t,b)) f bx@(h,(tt,tb)) (B V n t1 t2)
  | n<=t  = B V n t1 $ addBox ps f (h,(n,tb)) t2
  | n>=b  = B V n (addBox ps f (h,(tt,n)) t1) t2
  | otherwise = B V n (addBox ((l,r),(t,n)) f (h,(tt,n)) t1) (addBox ((l,r),(n,b)) f (h,(n,tb)) t2)
           
get :: String -> [Integer]
get [] = []
get s@(c:cs)  = case reads s of
  []         -> get cs
  ((n,rs):_) -> n : get rs

outer :: Box
outer = ((0,1001),(0,1001))

addAll xfs t = foldl (\t (x,f) -> addBox x f outer t ) t xfs

shw _ _ [] = [" "]
shw _ _ (x:xs) = ["#"]

aln n xs = replicate (max (n - length xs) 0) (head xs)  ++ xs

vmerge xs ys = al xs ++ (al ["-"] ++ al ys)
  where al = map$aln$max(length$head ys)$length$head xs
hmerge xs ys = zipWith (\ x y -> x++('|':y)) (al xs) (al ys)
  where al = aln$max(length ys)$length xs

ff H = hmerge
ff V = vmerge

indent c = map (c:)

ind t@(Leaf _) = [show t]
ind (B d k t1 t2) = ("B "++show d++" "++show k)  : i '|' t1 ++ i ' ' t2
  where i c = indent c.ind

grd = unlines . foldT ff shw

main :: IO ()
main = do
  f <- map get <$> lines <$> readFile "day3.txt"
  --print f
  let tree = addAll [ (((x,x+w),(y,y+h)),(i:)) | [i,x,y,w,h]<-f ] (Leaf [])
  --putStr$ unlines $ ind tree
  --print tree
  --putStr $ unlines $ foldT ff shw tree
  
  putStrLn . show $ foldT (const (+)) (\ w h  a -> if length a <= 1 then 0 else w*h ) tree
  
