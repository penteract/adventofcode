{-# LANGUAGE MonadComprehensions, LambdaCase, BlockArguments #-}
import Data.Char
import Control.Arrow
import Data.List
import Data.Maybe
import Control.Monad
import Control.Monad.State hiding (get)
import Control.Monad.Except
import Control.Applicative
import qualified Data.Map as M
import Data.Bits
import System.IO.Unsafe
import Data.Monoid
import System.Process
import Monad
import Interpreter

manhat (x,y) (z,w) = abs (x-z) + abs (y-w)


--convert a reversed list of base 10 digit characters into a number
gi :: String -> Int
gi "" = 0
gi (c:rs) = (ord c - 48) + 10*gi rs


--ignore characters until an int is read
ri :: String -> (Maybe Int,String)
ri "" = (Nothing,"")
ri ('-':rs) = (if not (null rs) && head rs `elem` ['0'..'9'] then first (return.negate.gi.reverse).(span (`elem` ['0'..'9'])) else ri) rs
ri (d:rs) = (if d `elem` ['0'..'9'] then first (return.gi.foldl (flip (:)) [d]).(span (`elem` ['0'..'9']))  else ri) rs

ri2 :: String -> Integer
ri2 = read

getints :: String -> [Int]
getints = unfoldr ((uncurry$flip$fmap.flip(,)).ri)

getgr = map getints

sm :: Int -> Int -> First Int
sm x y
  | (x `div` y)*y == x = First (Just (x `div` y))
  | otherwise = First Nothing

pgrid :: Show a => [a] -> IO ()
pgrid = putStrLn . unlines . map show

-- (^-^) = liftA2 (-)
-- (^<>^) = liftA2 (<>)


pairs :: [a] -> [(a,a)]
pairs [] = []
pairs (x:xs) = map ((,) x) xs ++ pairs xs


dis1 :: Int -> [Int] -> String
dis1 i xs = if xs == [] then []
  else case getOpModes (head xs) of
    (Right (op,modes)) -> let mds =  zipWith see modes (take (len op - 1) (tail xs)) in
                                 show i ++ ": " ++ seeOp op ++ " " ++ intercalate "," mds
    Left err -> err

disass :: Int -> [Int] -> [String]
disass i xs = if xs == [] then []
  else case getOpModes (head xs) of
     (Right (op,modes)) -> let mds = zipWith see modes (take (len op - 1) (tail xs)) in (show i ++ ": " ++ seeOp op ++ " " ++ intercalate "," mds ): disass (i+len op) (drop (len op) xs)
     Left err -> [err]

debug :: PState -> IO PState
debug s@(S ip m inp) = do
  putStrLn (dis1 ip  (drop ip $ M.elems m))
  let ((err, out) , s') = examine step s
  if err == Right False then debug s' else return s'

-- program , input , output , memory
tests =[
    ("1,9,10,3,2,3,11,0,99,30,40,50",[],[],[(3,70),(0,3500)])
  , ("1,1,1,4,99,5,6,0,99",[],[],[(4,2),(0,30)])
  , ("1002,4,3,4,33", [],[],[(0,1002),(2,3),(3,4),(4,99)])
  , ("3,9,8,9,10,9,4,9,99,-1,8",[8],[1],[])
  , ("3,9,8,9,10,9,4,9,99,-1,8",[9],[0],[])
  , ("3,9,8,9,10,9,4,9,99,-1,8",[7],[0],[])
  , ("3,9,7,9,10,9,4,9,99,-1,8",[8],[0],[])
  , ("3,9,7,9,10,9,4,9,99,-1,8",[9],[0],[])
  , ("3,9,7,9,10,9,4,9,99,-1,8",[7],[1],[])
  , ("3,9,7,9,10,9,4,9,99,-1,8",[6],[1],[])
  ]

test :: IO ()
test = mapM_ (\ (prog,inp,outchk,memchk) -> do
  let s = newState (getints prog) inp
  let ((err, out) , (S ip m inp)) = examine runProg s
  when (err /= Right ()) (putStrLn ("Error: "++ show err))
  when (out /= outchk)  (putStrLn ("Bad output - Expected: "++show outchk++" Actual: "++show out))
  let xs = memchk >>= (\(addr,val) ->
                     if m M.! addr == val then []
                       else ["Expected: "++show val++" Actual: "++show (m M.! addr)]
                       )
  when (not (null xs)) (putStrLn$ "Bad memory:\n" ++ unlines xs)
    ) tests

system code setts = foldl (\ inp sett ->
  let s = newState code sett:inp
      ((err, out) , _) = examine runProg s in out
  ) [0] setts

main = do
    f <- readFile "../2/input"
    let s =  newState (getints $ head $ lines f) [] --  "3,1,4,0,99"
    let s' = psSetAt 1 12 $ psSetAt 2 2 $ s
    let ((err, out) , (S ip m inp)) = examine runProg s'
    when (m M.! 0 /= 2890696)  (print "test (day 2) failed")
    test
    f <- readFile "../5/input"
    let d =   getints $ head $ lines  f --"3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9"
    let s = newState d [1]
    let ((err, out) , (S ip m inp)) = examine runProg s
    when (out /= [0,0,0,0,0,0,0,0,0,6761139]) do
      print err
      print out
      print (inp, ip, map (m M.!) [ip-2..ip])
      print$ map snd (M.toList m)
    let s52 = newState d [5]
    let ((err, out) , (S ip m inp)) = examine runProg s52
    when (out /= [9217546]) do
      print err
      print out
      print (inp, ip, map (m M.!) [ip-2..ip])
      print$ map snd (M.toList m)
    f <- readFile "../7/input"
    let d = getints $ head $ lines  f



    --19690720
    --10810694
    -- print d
    --print$ sum $ map (foldr1 max ^-^ foldr1 min ) d
    --print$ sum $ map (fromJust . getFirst . mconcat . map ( (uncurry sm ^<>^ uncurry (flip sm))) . pairs ) d
