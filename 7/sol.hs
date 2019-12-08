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

disass :: Int -> [Int] -> [String]
disass i xs = if xs == [] then []
  else case getOpModes (head xs) of
     (Right (op,modes)) -> let mds = zipWith see modes (take (len op - 1) (tail xs)) in (show i ++ ": " ++ seeOp op ++ " " ++ intercalate "," mds ): disass (i+len op) (drop (len op) xs)
     Left err -> [err]


main = do
    system "pwd"
    f <- readFile "../2/input"
    let s =  newState (getints $ head $ lines f) [] --  "3,1,4,0,99"
    let ((err, out) , (S ip m inp)) = examine runProg s
    putStrLn $ unlines (disass 0 (M.elems $ mem s))
    f <- readFile "../5/input"
    let d =   getints $ head $ lines f --  "3,1,4,0,99"
    --let s = psSetAt 1 82 $ psSetAt 2 26 $ newState d []
    let s = newState d [1]
    putStrLn $ unlines (disass 0 d)
    print s
    let ((err, out) , (S ip m inp)) = examine runProg s
    --print ip
    --let ((err, out) , (S ip m inp)) = examine (applyOp In [Imm]) s
    print err
    putStrLn $ unlines (disass 0 (M.elems m))
    print out
    print (inp, ip, map (m M.!) [ip-2..ip])
    print$ map snd (M.toList m)
    --19690720
    --10810694
    -- print d
    --print$ sum $ map (foldr1 max ^-^ foldr1 min ) d
    --print$ sum $ map (fromJust . getFirst . mconcat . map ( (uncurry sm ^<>^ uncurry (flip sm))) . pairs ) d
