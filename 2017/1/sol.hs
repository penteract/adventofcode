import Data.Char
import Control.Arrow
import Data.List
import Data.Maybe
import Control.Monad
import Control.Applicative
import qualified Data.Map as M
import Data.Bits
import System.IO.Unsafe

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

get = unfoldr ((uncurry$flip$fmap.flip(,)).ri)

sm :: [(Int,Int)] -> Int
sm [] = 0
sm ((x,y):rs) = (if x==y then (+x) else id) $ sm rs

main = do
    f <- readFile "input"
    let d =  head $ lines f
    let b = map ((subtract 48).ord) d
    print$ sm (zip b (tail b++[head b]))
    let n = length b `div` 2
    print$ sm (zip b (drop n b++ take n b))
