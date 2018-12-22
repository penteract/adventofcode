{-# LANGUAGE MonadComprehensions #-}
import qualified Data.Set.Monad as S

import Data.Char
--import Data.Bits
import Data.Maybe
import Control.Arrow
import System.IO.Unsafe
import qualified Data.Map.Strict as Map
--import qualified Data.Set as S
import Data.List

--(.^.) a b = fromEnum a `xor` fromEnum b


-- proc (x:y:rs) = let p = proc (y:rs) in if p/=[] && head p == other 32 then tail p else (x:p)
-- proc c = c

data RE = Alt RE RE | ES | Cons RE RE | Char Char deriving Show

sh ES = ""
sh (Alt a b) = "("++sh a++"|"++sh b++")"
sh (Cons x y) = sh x ++sh y
sh (Char a) = [a]

-- make cons-trees top heavy
recons (Cons a b) = let a' = recons a
                        b' = recons b in
           case b' of
             Cons c d -> Cons (Cons a' c) d
             ES -> a'
             o -> Cons a' o
recons (Alt a b) = Alt (recons a) (recons b)
recons o = o

parse [] = (ES,"")
parse ('(':xs) = unsafePerformIO $ (do
  --print$ parse xs
  let (a,(xs')) = parse xs
  case xs' of
    ('|':xs'') -> return$ let ((Cons x y),xs''')=parse ('(':xs'') in  ((Cons $ Alt a x) y,xs''')
    (')':xs'') -> return$ first (Cons a) $ parse xs'')
parse (x:xs) = if x `elem` "|)" then (ES,x:xs)
  else if x `elem` "NESW" then first (Cons (Char x)) $ parse xs else parse xs


count :: RE -> Integer
count (Alt a b) = count a + count b
count (Cons x y)= count x * count y
count _ = 1

(a,x) +. (b,y) = (a+b,x+y)

-- add n to m from position x
comb :: [(Pos,[Char])] -> MP -> Pos -> MP
comb n m x = (Map.unionWith (union) m$ (Map.fromList [(k+.x,v) |  (k,v)<- n]))

type Pos = (Int,Int)
type MP = Map.Map Pos [Char]
e = Map.empty

--dir :: Char -> [(Int,Int)]
dir 'N' = [(1,0)]
dir 'W' = [(0,-1)]
dir 'S' = [(-1,0)]
dir 'E' = [(0,1)]

hd = head.dir

neighbs m pos = [p +. pos | p <- map hd $ (m Map.! pos)]

search1 :: MP -> ([Pos] , S.Set Pos) -> ([Pos],S.Set Pos)
search1 m (front,seen) = (nub $ filter (`S.notMember` seen) (front>>=neighbs m)  , seen `S.union` S.fromList front)

--ser :: MP -> ([Pos],S.Set Pos) -> Int -> a
ser m n([],seen) = 0
ser m n(nx,seen) = (if n>=1000 then length nx else 0) + (ser m (n+1) (search1 m (nx,seen))) 

other 'N' = 'S'
other 'S' = 'N'
other 'E' = 'W'
other 'W' = 'E'

--type SS = S.Set Pos
--(****) :: (MP -> MP -> MP) -> (SS ->SS->SS) -> (MP->MP)
(****) f g (x,y) (a,b) = (f x a,g y b)

getall :: RE -> (MP,S.Set Pos)
getall ES = (e,(return (0,0)))
getall (Cons a b) =
               let (m,x) = getall a
                   (n,y) = getall b in
               (S.foldl' (comb $ Map.toList n) m x  ,  [x1+.y1 |  x1<-x , y1<-  y])
getall (Alt a b) = (Map.unionWith (++)  **** S.union) (getall a) (getall b)
getall (Char c) = (Map.fromList [((0,0),[c])] , S.fromList $ dir c)

main = do
    t <- readFile "input"
    let (s,"") = parse t
--    print s
--    putStrLn $ show $ count s
--    putStrLn $ sh $ (recons s)
    let (a,ls) = getall (recons s)
    let m = eqlz a
    --print ls
   -- print a
    --print $ m
    print $ Map.size (eqlz a)
    print $ ser m 0 ([(0,0)],S.empty)
--    putStrLn $ show $ [length (proc (filter ((/= c).toLower) s)) | c <-['a'..'z']]
--    putStrLn .show $ (head s,last s)

eqlz :: MP -> MP
eqlz m = Map.fromListWith union [x  |  p <- Map.toList m, x<-prs p ]

prs :: (Pos,[Char] ) -> [(Pos,[Char])]
prs (p,cs) = (p,cs) : [(p+. (head $ dir c),[other c]) | c <- cs]
