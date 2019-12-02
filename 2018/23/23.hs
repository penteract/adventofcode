import Prelude -- hiding ((!!))
import qualified Prelude
import Data.Char
import Control.Arrow
import Data.List hiding((!!))
import Data.Maybe
import Control.Monad
--import Control.Monad.State
import qualified Data.Map as M
import Data.Bits
import System.IO.Unsafe

--import 


--a !! b = a Prelude.!! fromInteger b
gi :: String -> Int
gi "" = 0
gi "-" = 0
gi (c:rs) = (ord c - 48) + 10*gi rs

ri :: String -> (Maybe Int,String)
ri "" = (Nothing,"")
ri (d:rs) = (if d `elem` ('-':['0'..'9']) then first (return.(if d=='-' then negate else id).gi.foldl (flip (:)) [d]).(span (`elem` ['0'..'9']))  else ri) rs

swp (a,b) = (b,a)

get = unfoldr ((uncurry$flip$fmap.flip(,)).ri)

type Pos = (Int,Int,Int)
type Bot = (Pos,Int)

d:: Pos -> Pos -> Int
d (x,y,z) (x2,y2,z2) = abs (x-x2) + abs (y-y2) + abs (z-z2)


parse :: String -> Bot
parse s = let [a,b,c,d] = (get s) in ((a,b,c),d)

to3 [a,b,c] = (a,b,c)

ir pos (pos1,r) = d pos pos1 <= r

bbase = 2

base bbase =  99768722 `div` (2*bbase)

squash scale ((x,y,z),r) = let b = 2^scale in  ((x`div`b,y`div`b,z`div`b),r`div`b+2)

data Cover = None | Partial | Full deriving (Eq,Show,Ord)

corners :: Box -> [Pos]
corners (c1,s) = map ((m3 (*2^s)) . z3 (+) c1) (cb [0,1])

-- Is part, all or none of the box within the bot's radius
test :: Box -> Bot -> Cover
test b (p,r) = let cs = corners b
                   c2 = last$ corners b
                   c1 = head$corners b
                   d1 = d p c1
                   d2 = d p c2
                   dn = (d1 + d2 - d c1 c2) `div` 2 in
    if all (<=r) (map (d p) cs) then Full else if dn<=r then Partial else None

m3 f (x,y,z) = (f x , f y, f z)

z3 f (a,b,c) (q,w,e) = (f a q, f b w , f c e)

-- pos, log scale
type Box = (Pos,Int)

initial :: [Box]
initial = [(m3 negate p, 27 ) |  p <-cb [0,1]]

count f = length . filter f

part :: Box -> [Bot] -> ([Bot],Int)
part b bts = let next = [bt | bt<-bts ,test b bt ==Partial] in
  (next,count ((==Full).test b) bts )

score :: Box -> [Bot] -> Int
score (p,s) = length . filter (ir p . squash s)


score' :: Pos -> [Bot] -> Int
score' p = length . filter (ir p )

divide :: Box -> [Box]
divide (p,r) = [(z3 ((+).(*2)) p up  ,r-1) | up <- cb [0,1]]

sc (xs,n) = ( length xs ) + n

looop :: Int -> [Bot] -> [Box] -> IO ()
looop n bots boxes = do
  if snd (head boxes) <0 then return ()
    else do
    let scored = map  (\bx -> (part bx  bots,bx)) boxes
    putStrLn$ unlines$ map (show. first ((n+).sc)) scored
    let ((bots',m),nb) = foldl1 (\(b1,p1) (b2,p2)  -> if sc b1 >=sc b2 then (b1,p1) else (b2,p2)  ) scored
    looop (n + m) bots' (divide nb)

main = do
    f <- readFile "input"
    let bots= map parse $ lines f
    --putStr $ unlines $map show l
    --putStr$ unlines$ map show $ sort (map swp bots)
    -- putStr$ unlines$ map (\p -> show (score p  bots,p)) initial
    looop 0 bots initial
    --let scrs  = map (\x -> (score' x bots , 0 - d (0,0,0) x,x)) reg
    --putStr $unlines$ map show  (sort scrs)
    -- putStr$ unlines$ map show $ [[((i,j,k),length [() | b<-bots, ir (i,j,k) (squash b bbase) ]) | i<-[-bbase..bbase],j<-[-bbase..bbase]] | k<-[-bbase..bbase]]

hn = [-30..0]
cb ns = [(i,j,k) | i <- ns, j <- ns, k <- ns]

reg = map (z3 (+) (15208328,49201000,48480208)) (cb hn)


