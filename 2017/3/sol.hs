{-# LANGUAGE MonadComprehensions #-}
import Data.Char
import Control.Arrow
import Data.List
import Data.Maybe
import Control.Monad
import Control.Applicative
import qualified Data.Map as M
import Data.Bits
import System.IO.Unsafe
import Data.Monoid

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

(^-^) = liftA2 (-)
(^<>^) = liftA2 (<>)


pairs :: [a] -> [(a,a)]
pairs [] = []
pairs (x:xs) = map ((,) x) xs ++ pairs xs



main = do
    f <- readFile "input"
    let d =  map get $ lines f
    print$ sum $ map (foldr1 max ^-^ foldr1 min ) d
    print$ sum $ map (fromJust . getFirst . mconcat . map ( (uncurry sm ^<>^ uncurry (flip sm))) . pairs ) d
