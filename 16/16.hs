import Data.Char
import Control.Arrow
import Data.List
import Data.Maybe
import Control.Monad
--import Control.Monad.State
import qualified Data.Map as M
import Data.Bits
import System.IO.Unsafe
--import 



gi :: String -> Int
gi "" = 0
gi (c:rs) = (ord c - 48) + 10*gi rs

ri :: String -> (Maybe Int,String)
ri "" = (Nothing,"")
ri (d:rs) = (if d `elem` ['0'..'9'] then first (return.gi.foldl (flip (:)) [d]).(span (`elem` ['0'..'9']))  else ri) rs

get = unfoldr ((uncurry$flip$fmap.flip(,)).ri)

data BinOp = Ad | Ml | An | Or | Gt | Eq deriving (Enum,Eq,Show)
data VR = Val | Reg deriving (Eq,Show)

data OpCode = Bin BinOp VR | Setr | Seti | Gtir | Eqir deriving (Eq,Show)

opcds = ([Ad ..Eq]>>=(\o -> map (Bin o) [Val,Reg])) ++ [Setr,Seti,Gtir,Eqir]

type Val =Int

type Regs = [Val]

type Ixs = (Int,Int,Int)

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
run o is@(a,b,c) regs = take c regs ++ [run' o is regs] ++ drop (c+1) regs

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

ops = M.fromList[
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
    f <- readFile "in1"
    let l= get f
    let r = mer (dotw l) intersect
    
    putStr $ unlines $ map show $ M.toList  r
    f2 <- readFile "in2"
    let ins = get f2
    print =<< do4 ops ins [0,0,0,0]



