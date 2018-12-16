import Data.Array
import Data.Ix
import Control.Monad
import Control.Applicative
import Control.Arrow
import Data.Set(Set,empty,member,insert,singleton)
import Data.List(partition)
import Control.Monad.State
import System.IO.Unsafe

(^&&^) = liftA2 (&&)

type MAP = Array Pos Species
type Species = Char
type Pos = (Int,Int)
type Info = (Pos,Int)
type Participant = (Info,Species)

type World = (MAP,[Participant])

input :: [String]
input = [
 "################################",
 "##########################.#####",
 "##########################.#####",
 "##########################.#.###",
 "#######################......###",
 "#################....#........##",
 "##############.##....G......G.##",
 "#############..#G...##.........#",
 "#############.GG..G..##.......##",
 "#############.................##",
 "#############G.........G....#.##",
 "###########G..........E........#",
 "###########...#####............#",
 "###########..#######...........#",
 "#######.....#########........###",
 "#######....G#########.......####",
 "##...G.G....#########...#....###",
 "#...G..G...G#########.###E...###",
 "##.......#..#########.#####..E##",
 "#............#######..##########",
 "#.GG........G.#####...##########",
 "#................E.....#########",
 "########..........##.###########",
 "#########.....###.....##########",
 "##########.E..##......##########",
 "#######..#....###.E...##########",
 "######.........###.E############",
 "######.#..G....##..#############",
 "######.....##..##.E#############",
 "#######....##.E...E#############",
 "######....G#......##############",
 "################################"]


m2 f = f***f

bnds = ((1,1),(length input,length $ head input))
bnds' = m2 (m2 (+ (-1))) bnds

f ... g = (f.) . g

getAt :: Pos -> MAP -> Char
getAt (y,x) w = w!(y,x)

isWall = ((=='#').). getAt

(x,y)+.(a,b) = (x+a,y+b)

dirs = [(-1,0),(0,-1),(0,1),(1,0)]

neighbs :: Pos -> [Pos]
neighbs p = map (p+.) dirs



people ::[Participant]
people = map (first (flip (,) 200)) $ filter (((/='.') ^&&^ (/='#')).snd) $assocs $ fst orig

orig  :: World
orig = (listArray bnds $ join input,people)

-- | (start,end)
type Path = (Pos,Pos)

getPos :: Participant -> Pos
getPos = fst.fst

fight :: Participant -> [Participant]
fight ((pos,h),sp) = if (h-3)>0 then [((pos,h-3),sp)] else []

searchFrom :: Pos -> World -> Species -> [Path]
searchFrom p w@(m,ps) sp = evalState  (srch $ map (join (,)) $filter (not . flip isWall m )$neighbs p) $ singleton p
  where
    srch :: [Path] -> State (Set Pos) [Path]
    srch [] = return []
    srch pths  = do
      pths' <- search1 pths w
      let (filled,nxt) = partition (\(s,e) -> any (==e) (map getPos ps)) pths'
      let targets = filter (\(s,e) -> any (\ ((pos,h),spe)->pos==e && spe/= sp) ps) filled
      if null targets then srch nxt else return targets

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

act :: Participant -> (World,[Participant]) -> (World,[Participant])
act self@((pos,h),sp) (w@(m,ps1),ps2) =
  let others = ps1++ps2
      enemies = filter (\ e -> any (\ ((pos,h),spe)->pos==e && spe/= sp) others) (neighbs pos)
      ts = map (join (,)) enemies ++ searchFrom pos (m,others) sp in
  case ts of
    [] -> (w,self:ps2)
    ((s,e):_) ->
      let
        altr :: Participant -> [Participant]
        altr o = if getPos o/=e then [o] else fight o in
         ((m,ps1 >>=altr),((pos,h),sp):(ps2>>=altr))


step :: World -> World
step (m,ps) = 

main :: IO ()
main = undefined
