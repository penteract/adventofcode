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
import AbsInt

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

get :: String -> [Int]
get = unfoldr ((uncurry$flip$fmap.flip(,)).ri)

getgr = map get

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

step :: Value a => M a Bool
step = getI >>= getOp >>= \op -> (applyOp op <* modify (incIP $ len op))

indirect :: Value a => Int -> M a a
indirect n = do
  p <- getRel n
  either return (getAt) (ref p)

applyOp :: Value a => Op -> M a Bool
applyOp Halt = return True
applyOp o = do
  x <- indirect 1
  y <- indirect 2
  pz <- getRel 3
  let r = case o of Add -> add x y
                    Mul -> mul x y
  case ref pz of Left a -> throwError ("Can't write to "++ show a)
                 Right n -> setAt n r
  return False

runProg :: Value a =>M a ()
runProg = do
  stop <- step
  if stop then return () else runProg

examine :: Value a => PState a -> (Either String (),PState a)
examine s = runState (runExceptT runProg) s

main = do
    system "pwd"
    f <- readFile "input"
    let d =  map I $ get $ head $ lines f
    let s = psSetAt 1 (Var "n") $ psSetAt 2 (Var "v") $ newState d
    print$ examine$ s
    -- print d
    --print$ sum $ map (foldr1 max ^-^ foldr1 min ) d
    --print$ sum $ map (fromJust . getFirst . mconcat . map ( (uncurry sm ^<>^ uncurry (flip sm))) . pairs ) d
