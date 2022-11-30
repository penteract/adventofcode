{-# LANGUAGE FlexibleInstances #-}
import Control.Monad (join)
import qualified System.Environment
import System.IO
import Data.List(uncons, subsequences)
import Data.Foldable(toList)

data T a b =  L a | B Int b (T a b) (T a b) deriving (Eq)

str :: O -> Char
str Mul = '*'
str Add = '+'
str Mod = '%'
instance Show (T L O)
    where
        showsPrec _ (L (Num n)) s = shows n s
        showsPrec _ (L (Var n)) s = "XYZ"!!n:s
        showsPrec _ (B _ op l r) s = '(': shows l (str op: shows r (')':s) )

newtype DL a = DL {unDL::[a]}
newtype EL a = EL {unEL::[a]}

data O = Mul | Mod | Add | Null deriving (Eq,Show)

type Op = (O,Bool,Bool)
-- Associative, Commutative, fn
operations :: [Op]
--operations = [((+),True,True),((*),True,True), (mod,False,False)]
operations = [(Mul,True,True),(Add,True,True), (Mod,False,False)]
numberedOps :: [(Int,Op)]
numberedOps = zip [1..] operations

-- fairly merge a finite list of potentially infinite lists
rr ::[[a]]->[a]
rr [] = []
rr [xs] = xs
rr ([]:xss) = rr xss
rr xss = uncurry ((.rr) . (++) ) $ unzip (xss >>= (toList . uncons))

-- take from a potentially infinite list of potentially infinite lists 
--  along diagonals - like the classical proof that there are as many rationals as integers
dl :: [[a]] -> [a]
dl xss = dl' [] xss
    where
        dl' started [] = rr started
        dl' started (xs:xss) = let (hds,tls) = unzip ((xs:started) >>= (toList . uncons)) in hds ++ dl' tls xss

-- dl [[(x,y) | x <-xs] | y<-ys] but returns the empty list if xs is empty
diagCross :: [a] -> [b] -> [(a,b)]
diagCross [] _ = []
diagCross _ [] = []
diagCross xs ys = dl [[(x,y) | x <-xs] | y <-ys] 

-- take from a potentially infinite list of potentially infinite lists
--   elements from later lists are exponentially rarer
el :: [[a]] -> [a]
el [] = []
el (xs:xss) = rr [xs,el xss]

data L = Var Int | Num Int deriving Show

isUseful :: (O,Bool) -> L -> Bool
isUseful (Mul,_) (Num 0) = False
isUseful (Mul,_) (Num 1) = False
isUseful (Add,_) (Num 0) = False
isUseful (Mod,_) (Num 1) = False
isUseful (Mod,_) (Num 0) = False
isUseful _ _ = True

-- let  a ->> b be (a->b) without the affine non-linear elements
-- Size(number of branches), operation not to use,  required variables, non-required variables
eTrees :: Int -> (O,Bool) -> [L] -> [L] -> [T L O]
eTrees 0 opl [] vs = [L v | v <- vs, isUseful opl v]
eTrees 0 _ (v:[]) _ = [L v]
eTrees 0 _ (v:_) _ = []
eTrees n (op,wasLeft) [] vs =  rr [
    rr [
        [ B i fn l r  |
            (l,r) <- diagCross (eTrees i (fn,True) [] vs) (eTrees (n-1-i) (fn,False) [] vs)
        ]
    | i <-  [0..n-1]]
    | (m,(fn,assoc,comm)) <-numberedOps , ((fn/=op) || wasLeft || (not assoc)) ]
eTrees n (op,wasLeft) xs vs =  let
    l = length xs
    s = subsequences xs
    ss = zip s (reverse s) in if n+1<l then (error "argh") else
        rr [
        rr [
            [ B i fn l r  |
                (l,r) <- diagCross (eTrees i (fn,True) xs vs) (eTrees (n-1-i) (fn,False) ys vs)
            ]
        | i <-  [0..n-1], (xs,ys) <- ss, length xs<=(i+1) && length ys <= (n-i)]
        | (m,(fn,assoc,comm)) <-numberedOps , ((fn/=op) || wasLeft || (not assoc)) ]
--eTrees _ _ _ _ = undefined

eTreesMustUseOp:: Int -> (Int,Op)
eTreesMustUseOp = undefined

allTreesOfSize :: Int -> [T () ()]
allTreesOfSize 0 = [L()]
allTreesOfSize n = [B i () l r | i<-[0..n-1], l<-allTreesOfSize i, r <- allTreesOfSize (n-i)  ]

allTrees :: [T () ()]
allTrees = join [allTreesOfSize i | i<-[1..]]


exc :: O -> Int -> Int -> Int
exc Mul a b = a*b
exc Add a b = a+b
exc Mod a 0 = 0
exc Mod a b = a `div` b

consts :: [Int]
consts = rr [[1,3..], [-1,-2..], [2,4..]]

eval :: T L O -> [Int] -> Int
eval (L (Num n)) vs = n
eval (L (Var n)) vs = vs !! n
eval (B i op l r) vs = exc op (eval l vs) (eval r vs)

--singleVarExprs =  (take (sampleOut `div` 3) (el [ (eTrees i (Null,False) [Var 0] (map Num consts)) | i <- [1..]]))

main :: IO ()
main = do
    [fname] <- System.Environment.getArgs
    c <- readFile fname
    let inp = (map read (lines c) :: [Int])
    --print inp
    sampleIn <- readFile "input1"
    let sampleInp = map read (lines sampleIn) :: [Int]
    print "hi"
    sampleOut <- (read <$> readFile "output1-1") :: IO Int
    --mapM_ print (take 100 $ eTrees 2 (Null,False) [Var 0] (map Num [1..]))
    --  (take (sampleOut `div` 3) (el [ (eTrees i (Null,False) [Var 0] (map Num consts)) | i <- [1..]]))
    let a = head$ filter (\ (_,(_,f)) -> f sampleInp == sampleOut) $ take (sampleOut)
                 (zip [1..] $ map (\ t -> (t, sum . map (eval t) . map (:[])))  (el [ (eTrees i (Null,False) [Var 0] (map Num consts)) | i <- [1..]]))
    --print (a sampleInp)
    print (fst a,fst (snd a))
    print (snd (snd a) inp)
