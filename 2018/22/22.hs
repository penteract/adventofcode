import Data.Array
import Data.Ix
import Control.Monad
import Control.Applicative hiding (empty)
import Control.Arrow
import Data.Set(Set,empty,member,insert,singleton,size)
import Data.List(partition,find,sort,foldl',nub)
import Data.Maybe
--import Control.Monad.State
import System.IO.Unsafe
import GHC.Exts(sortWith)

(^&&^) :: (a -> Bool) -> (a -> Bool) -> a -> Bool
(^&&^) = liftA2 (&&)

infix 5 ^&&^

type Pos = (Int,Int)

{-
swp (a,b) = (b,a)
m2 f = f***f

bnds ss = ((1,1),(length ss,length $ head ss))
-- bnds' ss = m2 (m2 (+ (-1))) $ bnds ss

f ... g = (f.) . g

getAt :: Pos -> MAP -> Char
getAt (y,x) w = w!(y,x)

isWall = ((=='#').). getAt

(x,y)+.(a,b) = (x+a,y+b)

dirs = [(-1,0),(0,-1),(0,1),(1,0)]

neighbs :: Pos -> [Pos]
neighbs p = map (p+.) dirs



people ::MAP -> [Participant]
people w = map (first (flip (,) 200)) $ filter (((/='.') ^&&^ (/='#')).snd) $assocs w

--orig  :: World
--orig = (listArray (bnds input) $ join input,people $ fst orig)

fromLines ss = listArray (bnds ss) $ join ss

-- | (start,end)
type Path = (Pos,Pos)

getPos :: Participant -> Pos
getPos = fst.fst

fight :: Participant -> [Participant]
fight ((pos,h),sp) = if (h-3)>0 then [((pos,h-3),sp)] else []

isFree :: MAP -> [Participant] -> Pos -> Bool
isFree m ps pos = null(getPAt '.' ps pos) && not (flip isWall m pos)

searchFrom :: Pos -> World -> Species -> [Path]
searchFrom p w@(m,ps) sp = evalState  (srch $ map (join (,)) $filter (isFree) $neighbs p) $ singleton p
  where
    srch :: [Path] -> State (Set Pos) [Path]
    srch [] = return []
    srch pths  = do
      pths' <- search1 pths w
      let (filled,nxt) = partition (\(s,e) -> any (==e) (map getPos ps)) pths'
      let targets = filter (\(s,e) -> any (\ ((pos,h),spe)->pos==e && spe/= sp) ps) filled
      if null targets then srch nxt else return (sortWith swp $ targets)

search1 :: [Path] -> World -> State (Set Pos) [Path]
search1 [] (m,p) = return []
search1 ((start,end):frontier) (m,p) = do
  s <- get
  let xs = (neighbs end) >>= (\pos -> do
                 if isWall pos m || member pos s then [] else [(start,pos)] )
  let l1 = xs
  mapM (modify.insert.snd) l1
  l2 <- search1 frontier (m,p)
  return (l1++l2)

getPAt :: Species ->[Participant] ->  Pos -> [Participant]
getPAt sp ps p = filter (((/=sp) .snd) ^&&^ ((==p).fst.fst)) ps

debug :: Show a => a -> b -> b
--debug x y=  unsafePerformIO $ print x >> return y
debug x y = y


shw :: World -> String
shw (m,ps) = shw' 1 (assocs m) ps

shw' n [] ps = "\n"
shw' n (d@((y,x),c):xs) ps = (if y>n then ('\n' :) else id) $ shc d ps : shw' y xs ps


shc (_,'#')   ps = '#'
shc (pos,_) ps = case find (\((p,_),_) -> p==pos) ps of
           (Just (_,c)) -> c
           Nothing -> '.'

-}

-- [[(y,x)]]
-- [[(0,0), (0,1) ],[(1,0) , (1,1)]]
{-
layout :: [[Integer]]
layout = map (map (`mod` base))$ (dpth:map (+dx) (head layout)) : zipWith (\ xs (y:ys) -> (y +dy ) : zipWith (\ x y -> x*y+dpth) xs ys) (tail layout) layout

ll = let rest = map () in
  map (map (`mod` base))$ ((dpth:map (+dx) (head ll)) : rest)-}

(x,y)+.(a,b) = (x+a,y+b)
debug x y=  unsafePerformIO $ print x >> return y

data Eqip = Torch| Gear| Neith deriving (Eq,Show,Ord)

type State = (Pos,Eqip)
type Terr = Integer

dirs = [(-1,0),(0,-1),(0,1),(1,0)]

neighbs :: Pos -> [Pos]
neighbs p = map (p+.) dirs

allowed :: Terr -> [Eqip]
allowed 0 = [Torch,Gear]
allowed 1 = [Gear,Neith]
allowed 2 = [Torch,Neith]

allowedAt :: Pos -> [Eqip]
allowedAt p = (terr p) >>= allowed

opts :: State -> [[State]]
opts (pos,eq) = [(do
                     p<- neighbs pos
                     e <- allowedAt p
                     if e==eq then [(p,eq)] else []),[],[],[],[],[],[ (pos,e') | e'<- allowedAt pos ]]

search1 :: [[State]] -> Set State -> ([[State]], Set State)
search1 (ths:front) ss = (foldl' (zipWith (flip (++)) ) (front ++[[]]) [opts s | s <- nub ths , not (s `member` ss)] ,foldl' (flip insert) ss ths) -- it's only a constantish factor (6.6)
  --foldl' (\ (fronts,set) st -> if not (st `member` set) then (zipWith (++) (opts st) fronts ,insert st set) else (fronts,set) ) (front++[[]],ss) ths

search :: Int -> [[State]] -> Set State -> Int
search n sss ss = debug (n, size ss) $ if final `member` ss then n else uncurry (search (n+1)) (search1 sss ss)

terr (y,x) = if y<0 || x<0 then [] else [(el!!y!!x) `mod` 3]

el ::[[Integer]]
el = [[(gi (y,x)+dpth) `mod` base | x<-[0..]] | y <- [0..] ]

gi :: (Int,Int) -> Integer
gi (0,0) = dpth
gi (0,x) = toInteger x*dx
gi (y,0) = toInteger y*dy
gi p@(y,x) = if p==trgt then 0 else  (el!!y!!(x-1)) * (el!!(y-1)!!x)

base = 20183

dy = 48271
dx = 16807

segment = take (fst trgt +1) $ map (take (snd trgt + 1)) el

sh :: Integer -> Char
sh a = case a `mod` 3 of
  0 -> '.'
  1 -> '='
  2 -> '|'

mm = map.map

main = print$ search 0 ([start] : replicate 6 []) empty
  --print segment--
  --print$ sum $map (sum.map (`mod` 3)) segment  --unlines $ map (map sh) segment

dpth = --510
  3066
trgt = --(10,10)
  (726,13)

final = (trgt,Torch)
start = ((0,0),Torch)
