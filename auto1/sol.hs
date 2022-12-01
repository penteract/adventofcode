{-# LANGUAGE FlexibleInstances #-}
import Control.Monad (join)
import qualified System.Environment
import System.IO
import Data.List
import Data.Foldable(toList)
import Data.Char
import Control.Arrow

data T a b =  L a | B Int b (T a b) (T a b) deriving (Eq)

str :: O -> Char
str Mul = '*'
str Add = '+'
str Mod = '%'

varnames :: [Char]
varnames = "XY" ++ repeat 'Z'

instance Show (T L O)
    where
        showsPrec _ (L (Num n)) s = shows n s
        showsPrec _ (L (Var n)) s = varnames!!n:s
        showsPrec _ (B _ op l r) s = '(': shows l (str op: shows r (')':s) )

newtype DL a = DL {unDL::[a]}
newtype EL a = EL {unEL::[a]}

data O = Mul | Mod | Add | Null deriving (Eq,Show)

type Op = (O,Bool,Bool)
-- Associative, Commutative, fn
operations :: [Op]
--operations = [((+),True,True),((*),True,True), (mod,False,False)]
operations = [(Mod,True,False),(Mul,True,True),(Add,True,True)] -- Mod (or whatever it's used as) isn't associative, but it's rarely useful to have too many of them in a chain
numberedOps :: [(Int,Op)]
numberedOps = zip [1..] operations

-- fairly merge a finite list of potentially infinite lists
rr ::[[a]]->[a]
rr = concat . transpose
{- ~1.5x worse time and memory:
rr [] = []
rr [xs] = xs
rr ([]:xss) = rr xss
rr xss = uncurry ((.rr) . (++) ) $ unzip (xss >>= (toList . uncons))
-}

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

-- take from a potentially infinite list of potentially infinite lists
-- take in a bablanced manner that favors the elements of the first lists and the fronts of the later lists
--   (along a something like a hyperbola)
hl :: [[a]] -> [a]
hl = concat . hl' 2
  where
    hl' :: Int -> [[a]] -> [[a]]
    hl' n [] = []
    hl' n xss = let (lot,rest) = splitAt n xss 
                    xs = map concat (transpose (map (hl''  2) lot)) in
                        if null xs then [] else head xs: rr [tail xs, hl' (n+n) rest]
    hl'' :: Int -> [a] -> [[a]]
    hl'' n [] = []
    hl'' n xs = (\(x,y)-> x:hl'' (n+n) y) (splitAt n (xs))


data L = Var Int | Num Int deriving Show

isUseful :: (O,Bool) -> L -> Bool
isUseful (Mul,_) (Num 0) = False
isUseful (Mul,_) (Num 1) = False
isUseful (Add,_) (Num 0) = False
isUseful (Mod,_) (Num 1) = False
isUseful (Mod,_) (Num 0) = False
isUseful (Mod,_) (Num (-1)) = False
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
    ss = zip s (reverse s) in
      if n+1<l then (error "argh") else
        rr [
        rr [
            [ B i fn l r  |
                (l,r) <- diagCross (eTrees (n-1-i) (fn,True) ys vs) (eTrees i (fn,False) xs vs)
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
exc Mod a b = a `mod` b

consts :: [Int]
consts = rr [[1,3..], [-1,-2..], [2,4..]]

eval :: T L O -> [Int] -> Int
eval (L (Num n)) vs = n
eval (L (Var n)) vs = vs !! n
eval (B i op l r) vs = exc op (eval l vs) (eval r vs)

eval' :: (Int->Int->Int)-> T L O -> [Int] -> Int
eval' _ (L (Num n)) vs = n
eval' _ (L (Var n)) vs = vs !! n
eval' fn (B i Mod l r) vs = fn (eval' fn l vs) (eval' fn r vs)
eval' fn (B i op l r) vs = exc op (eval' fn l vs) (eval' fn r vs)

--singleVarExprs =  (take (sampleOut `div` 3) (el [ (eTrees i (Null,False) [Var 0] (map Num consts)) | i <- [1..]]))
--convert a reversed list of base 10 digit characters into a number
gi :: String -> Int
gi "" = 0
gi (c:rs) = (ord c - 48) + 10*gi rs


--ignore characters until an int is read
ri :: String -> (Maybe Int,String)
ri "" = (Nothing,"")
ri ('-':rs) = (if not (null rs) && head rs `elem` ['0'..'9'] then first (return.negate.gi.reverse).(span (`elem` ['0'..'9'])) else ri) rs
ri (d:rs) = (if d `elem` ['0'..'9'] then first (return.gi.foldl (flip (:)) [d]).(span (`elem` ['0'..'9']))  else ri) rs

getints :: String -> [Int]
getints = unfoldr ((uncurry$flip$fmap.flip(,)).ri)

readInp :: String -> String -> [[Int]]
readInp test s = let
    l = lines test
    iss = map getints l
    cl = concat l
    fcl = filter (`elem` ['0'..'9']) cl
    mn = minimum (map ord cl)
    in
        if (length fcl * 8) < length cl then map (map ((subtract mn) . ord)) (lines s)
        else if length l==1 && all (`elem` ['0'..'9']) (head l) then [[ord c - ord '0'] | c <- concat (lines s)]
            else map getints (lines s)

folds :: [[Int]->Int]
folds = [sum, maximum ,minimum, (\ xs -> minimum xs * maximum xs), product]

nfolds :: [(String, [Int] -> Int)]
nfolds = [("max",maximum),("min",minimum),("min*max",(\ xs -> minimum xs * maximum xs))]

trees :: Int -> [T L O]
trees j = el [ (eTrees i (Null,False) (map Var [0..(j-1)]) (map Num consts)) | i <- [(j-1)..3]]
trees' :: Int -> [T L O]
trees' j = el [ (eTrees i (Null,False) (map Var [0..(j-1)]) (map Num consts)) | i <- [j..3]]

solveGeneric :: [(String,[[Int]] -> Int)]
solveGeneric = hl [
    [ (name2++"("++name1++")", fn2 . map fn1) | (name1,fn1) <- (("prod",product):solveSimple')]
    | (name2,fn2) <- solveSimple'
  ]

namedOps :: [(String,Int->Int->Int)]
namedOps = [
    --("mod",\ x y -> if y/=0 then x`mod`y else 1),
    ("gt",\x y -> if x>y then 1 else 0),
    ("div",\ x y -> if y/=0 then x`div`y else 1),
    ("pow",\ x y -> if y>=0 then x^y else 1 )]

solvePairs :: [ (String,[(Int,Int)] -> Int) ]
solvePairs = el $ [
    map (\ t -> ("sum:"++show t, sum . map (eval t . (\ (a,b)->[a,b])) ))  (trees 2) 
  , rr [ map (\ t -> ("<"++opname++">"++"sum:"++show t, sum . map (eval' op t . (\ (a,b)->[a,b])) ))  (trees' 2) | 
     (opname,op) <- namedOps
    ]
  , rr [
     rr (map (\ t -> (foldname++":"++show t, fn . map (eval t . (\ (a,b)->[a,b])) ))  (trees 2) :
      [ map (\ t -> ("<"++opname++">"++foldname++":"++show t, fn . map (eval' op t . (\ (a,b)->[a,b])) ))  (trees' 2) | 
        (opname,op) <- namedOps
      ]
    ) | (foldname,fn) <- [("max",maximum),("min",minimum), ("min*max",(\ xs -> minimum xs * maximum xs))]
    ]
  ]

solvePairsUnsafe :: [ (String,[[Int]] -> Int) ]
solvePairsUnsafe = [(a, f . map (\[a,b] -> (a,b)) ) | (a,f)<-solvePairs]

solveSimple' :: [(String,[Int] -> Int)]
solveSimple' = el $ [
    map (\ t -> ("sum:"++show t, sum . map (eval t . (:[])) ))  (trees 1)  --(el [ (eTrees i (Null,False) [Var 0] (map Num consts)) | i <- [1..5]]),
  , rr [ map (\ t -> ("<"++opname++">"++"sum:"++show t, sum . map (eval' op t . (:[])) ))  (trees' 1) | 
     (opname,op) <- namedOps
    ]
  , [("adjacent "++name,\l -> fn (zip l (tail l))) | (name, fn)<- solvePairs]
  , rr [
     rr (map (\ t -> (foldname++":"++show t, fn . map (eval t . (:[])) ))  (trees 1) :
      [ map (\ t -> ("<"++opname++">"++foldname++":"++show t, fn . map (eval' op t . (:[])) ))  (trees' 1) | 
        (opname,op) <- namedOps
      ]
    ) | (foldname,fn) <- [("max",maximum),("min",minimum), ("min*max",(\ xs -> minimum xs * maximum xs))]
    ]
  ]
solveSimple :: [(String,[Int] -> Int)]
solveSimple = el $ [
    map (\ t -> ("sum:"++show t, sum . map (eval t . (:[])) ))  (trees 1)  --(el [ (eTrees i (Null,False) [Var 0] (map Num consts)) | i <- [1..5]]),
  , rr [ map (\ t -> ("<"++opname++">"++"sum:"++show t, sum . map (eval' op t . (:[])) ))  (trees' 1) | 
     (opname,op) <- namedOps
    ]
  , [("adjacent "++name,\l -> fn (zip l (tail l))) | (name, fn)<- solvePairs]
  , rr [
     rr (map (\ t -> (foldname++":"++show t, fn . map (eval t . (:[])) ))  (trees 1) :
      [ map (\ t -> ("<"++opname++">"++foldname++":"++show t, fn . map (eval' op t . (:[])) ))  (trees' 1) | 
        (opname,op) <- namedOps
      ]
    ) | (foldname,fn) <- [("max",maximum),("min",minimum), ("min*max",(\ xs -> minimum xs * maximum xs))]
    ]
  ] 
  -- ++ [map (\ t -> (foldname++":"++show t, fn . map (eval t . (:[])) ))  (trees 1)
  --      | (foldname,fn) <- [("max",maximum),("min",minimum),("min*max",(\ xs -> minimum xs * maximum xs))]]

lg :: Int -> Int
lg n = if n<=1 then 1 else 1+ lg (n`div`2)

handleInp :: String -> String -> Int -> (String,Int)
handleInp tests reals testout =
    let rd = readInp tests
        testn = rd tests
        realn = rd reals
        ctn = concat testn 
        maxtries = testout*(lg testout) -- If there weren't any duplicate functions, this might be more like testout/10 (to give at least 90% chance that if we're wrong we don't submit anything)
         in
            if length testn == 1 || all ((==1).length) testn then head [(s,f (concat realn)) | (s,f)<-take maxtries solveSimple, f ctn==testout]
            else if ((==2).length) testn then head [ (s,f realn) | (s,f) <- take (maxtries*2) (rr [solvePairsUnsafe, solveGeneric]), f testn == testout ]
            else head [ (s,f realn) | (s,f) <- take maxtries solveGeneric, f testn == testout ]


main :: IO ()
main = do
    [fname] <- System.Environment.getArgs
    c <- readFile fname
    --let inp = (map read (lines c) :: [Int])
    --print inp
    sampleIn <- readFile "input1"
    -- let sampleInp = map read (lines sampleIn) :: [Int]
    --print "hi"
    sampleOut <- (read <$> readFile "output1-1") :: IO Int
    --mapM_ print (take 100 $ eTrees 2 (Null,False) [Var 0] (map Num [1..]))
    --  (take (sampleOut `div` 3) (el [ (eTrees i (Null,False) [Var 0] (map Num consts)) | i <- [1..]]))
    --let a = head$ filter (\ (_,(_,f)) -> f sampleInp == sampleOut) $ take (sampleOut)
    --             (zip [1..] $ map (\ t -> (t, sum . map (eval t) . map (:[])))  (el [ (eTrees i (Null,False) [Var 0] (map Num consts)) | i <- [1..]]))
    --print (a sampleInp)
    let (n,r) = handleInp sampleIn c sampleOut
    putStrLn n
    print r
    --print (fst a,fst (snd a))
    --print (snd (snd a) inp)
