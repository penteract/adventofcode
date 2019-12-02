import Prelude hiding ((!!))
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


a !! b = a Prelude.!! fromInteger b

gi :: String -> Integer
gi "" = 0
gi (c:rs) = toInteger (ord c - 48) + 10*(gi rs)

ri :: String -> (Maybe Integer,String)
ri "" = (Nothing,"")
ri (d:rs) = (if d `elem` ['0'..'9'] then first (return.gi.foldl (flip (:)) [d]).(span (`elem` ['0'..'9']))  else ri) rs

get = unfoldr ((uncurry$flip$fmap.flip(,)).ri)

data BinOp = Ad | Ml | An | Or | Gt | Eq deriving (Enum,Eq,Show)
data VR = Val | Reg deriving (Eq,Show)

data OpCode = Bin BinOp VR | Setr | Seti | Gtir | Eqir deriving (Eq,Show)

opcds = ([Ad ..Eq]>>=(\o -> map (Bin o) [Val,Reg])) ++ [Setr,Seti,Gtir,Eqir]

type Val =Integer

type Regs = [Val]

type Ixs = (Integer,Integer,Integer)

type Instr = (OpCode,Ixs)

p1 "add" = Ad
p1 "mul" = Ml
p1 "eqr" = Eq
p1 "gtr" = Gt

poc :: String -> OpCode
poc "gtir" = Gtir
poc "eqir" = Eqir
poc "seti" = Seti
poc "setr" = Setr
poc o = Bin (p1 $ take 3 o) (if last o=='r' then Reg else Val)

parse :: String -> Instr
parse s = (poc$take 4 s, to3 $ get$ drop 4 s)

to3 [a,b,c] = (a,b,c)

bin :: BinOp -> Val -> Val -> Val
bin Ad x y = x+y
bin Ml x y = x*y
bin An x y = x .&. y
bin Or x y = x.|. y
bin Gt x y = if x>y then 1 else 0
bin Eq x y = if x==y then 1 else 0

run' :: OpCode->Ixs ->Regs -> Val
run' (Bin op Val) (a,b,_) rs = let v = rs!!a in bin op v b
run' (Bin op Reg) (a,b,_) rs = let v = rs!!a in bin op v (rs!!b)
run' Setr (a,b,c) rs = rs!!a
run' Seti (a,b,c) rs = a
run' Eqir (a,b,c) rs = if a==rs!!b then 1 else 0
run' Gtir (a,b,c) rs = if a>rs!!b then 1 else 0

run :: OpCode -> Ixs -> Regs -> Regs
run o is@(a,b,c) regs = take (fromInteger c) regs ++ [run' o is regs] ++ drop (fromInteger (c+1)) regs
{-
seeif :: [Int] -> (Int,[OpCode])
seeif xs =
  let inp = take 4 xs
      [a,b,c] = take 3 $ drop 5 xs
      out = drop 8 xs in
   (head$ drop 4 xs ,(map fst $ filter ((==out).snd) $ map (\ cd-> (cd,run cd (a,b,c) inp ))opcds))

dotw :: [Int] -> [(Int,[OpCode])]
dotw [] = []
dotw xs =do
  seeif (take 12 xs): (dotw $ drop 12 xs)

mer ::Ord a => [(a,b)] -> (b -> b -> b) -> M.Map a b
mer xs f = foldr (\(a,b) -> M.insertWith f a b ) M.empty xs

do4 :: M.Map Int [OpCode] -> [Val] -> Regs -> IO Regs
do4 m [] rs = return rs
do4 m ls @ (r:a:b:c:rss) rs =  do
     let [opc] = (m M.! r)
     print  (take 4 ls,rs)
     do4 m rss $ run opc (a,b,c) rs

-- seq (unsafePerformIO $ print  r)
-}
ipr = 1

do3 [r0,r1,r2,r3,r4,r5] = [r0+ (if (r5>=1 && r5<=r4 && r4 `mod` r5==0) && r2*r5<=r4 then r5 else 0),12,(max r2 r4)+1, 1, r4, r5]

do2 [r0,r1,r2,r3,r4,r5] = [r0 + sum (filter (>=r5) (factors r4)), 16 , r4+1 , 1 , r4 ,r4+1]

factors :: Integer -> [Integer]
factors n = nub $ factors' 1 n
  where
    factors' ::Integer -> Integer -> [Integer]
    factors' i n = if fromInteger i>sqrt (fromInteger n) then [] else if n `mod` i ==0 then i:(n `div` i) :factors' (i+1) n else factors' (i+1) n

runlst :: [Instr] -> Regs -> Regs
runlst ins rs = if rs!!ipr==2 then runlst ins (do2 rs) else
  if (rs!!ipr)>=toInteger (length ins) then rs else
    let rs' = uncurry run (ins!!(rs!!ipr)) rs
        rs'' = uncurry run (Bin Ad Val,(ipr,1,ipr)) rs' in
    unsafePerformIO (print rs >> return (runlst ins rs''))
    --(runlst ins rs'')

ops = M.fromList [
  (0,[Eqir]),
  (1,[Bin Or Reg]),
  (2,[Bin Ad Reg]),
  (3,[Bin Gt Val]),
  (4,[Bin Ml Val]),
  (5,[Gtir]),
  (6,[Bin Ml Reg]),
  (7,[Bin An Reg]),
  (8,[Bin Or Val]),
  (9,[Bin Eq Val]),
  (10,[Bin Eq Reg]),
  (11,[Bin An Val]),
  (12,[Setr]),
  (13,[Bin Gt Reg]),
  (14,[Bin Ad Val]),
  (15,[Seti])
  ]

main = do
    f <- readFile "input"
    let l= map parse $ tail$ lines f
    putStr $ unlines $map show l
    print $ runlst l [1,0,0,0,0,0]
    --putStr $ unlines $ map show $ M.toList  r
    --f2 <- readFile "in2"
    --let ins = get f2
    --print =<< do4 ops ins [0,0,0,0]



