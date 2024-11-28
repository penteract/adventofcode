import Control.Applicative
import Data.Char
bounds = (165432,707912)

fac :: Int -> Integer
fac 0 = 1
fac n = (toInteger n) * fac (n-1)

ncr :: Int -> Int -> Int
ncr a b = fromInteger $ fac a `div` fac b `div` fac (a-b)

ci sz n = ncr (sz+n-1) n
wd sz n = ci sz n - ncr sz n

cf :: [Int] -> Int
cf xs = f (>=) ci -- - f (<) ncr + f (<=) ncr
 where f c k = sum (map (uncurry k)$zip [length xs,length xs - 1 ..]$map snd
                           (takeWhile (uncurry c) (zip (10:xs) xs))
                       ) -- needs some details

get = cf . map ((57-) . ord) . show

main = print$ get  (fst bounds) - get (snd bounds + 1)
