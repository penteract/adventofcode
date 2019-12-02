import Data.Array
import Data.Ix
import Control.Monad
import Control.Applicative
import Control.Arrow
import Data.Set(Set,empty,member,insert,singleton)
import Data.List(partition,find,sort)
import Data.Maybe
import Control.Monad.State
import System.IO.Unsafe
import GHC.Exts(sortWith)

(^&&^) :: (a -> Bool) -> (a -> Bool) -> a -> Bool
(^&&^) = liftA2 (&&)

infix 5 ^&&^

type MAP = Array Pos Species
type Species = Char
type Pos = (Int,Int)
type Info = (Pos,Int)
type Participant = (Info,Species)

type World = (MAP,[Participant])


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

act :: Participant -> (World,[Participant]) -> (World,[Participant])
act self@((pos,h),sp) (w@(m,ps1),ps2) =
  let others = ps1++ps2
      --enemies = map (fst.fst) $ sortWith(\ ((pos,h),sp)-> (h,pos)) $  join $ map (`getPAt` others) (neighbs pos)
      enemies =  sortWith(\ ((pos,h),sp)-> (h,pos)) $  join $ map (getPAt sp others) (neighbs pos)
      ts = map ((,) pos) (map (fst.fst) $enemies) ++ searchFrom pos (m,others) sp in
  case (debug (self,enemies,ts)  ts) of
    [] -> (w,self:ps2)
    ((s,e):_) ->if e `elem` neighbs s then
         let (en:_) = map (fst.fst) $ sortWith(\ ((pos,h),sp)-> (h,pos)) $  join $ map (getPAt sp others) (neighbs s) in
           ((m,ps1 >>=altr en),self':(ps2>>=altr en))
       else ((m,ps1),self':ps2)
      where
        altr :: Pos -> Participant -> [Participant]
        altr en o = if getPos o/=en then [o] else fight o
        self' = ((s,h),sp)


step :: World -> World
step (m,ps) = step' ((m,sort ps),[])

step' :: (World,[Participant]) -> World
step' ((m,[]),ps) = (m,ps)
step' ((m,p:ps),ps2) = step' $ act p ((m,ps),ps2)


shw :: World -> String
shw (m,ps) = shw' 1 (assocs m) ps

shw' n [] ps = "\n"
shw' n (d@((y,x),c):xs) ps = (if y>n then ('\n' :) else id) $ shc d ps : shw' y xs ps


shc (_,'#')   ps = '#'
shc (pos,_) ps = case find (\((p,_),_) -> p==pos) ps of
           (Just (_,c)) -> c
           Nothing -> '.'

looop :: Int -> World -> IO ()
looop n w@(m,p:ps) = do
  --print n
 -- print (p:ps)
  --putStrLn $ shw w
  if all ((snd p==).snd) ps then
    let tt =(sum $map (snd.fst) (p:ps)) in 
                                      print (p:ps) >> (putStrLn $ shw w) >> print (n,tt, n*tt, (n-1)*tt)
    else looop (n+1) (step w)

main = main' "input"

main' :: String ->IO ()
main' fname = do
  f <- lines <$> readFile fname
  let m = fromLines f
      ps = people m
  looop 0 (m,ps)
