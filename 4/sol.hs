import Control.Applicative
bounds = (165432,707912)

fac 0 = 1
fac n = n * fac (n-1)

ncr a b = fac a `div` fac b `div` fac (a-b)

ci sz n = ncr (sz+n-1) n
wd sz n = ci sz n - ncr sz n

(^-^) = liftA2 (+)

cf :: [Integer] -> Integer
cf = f (<=) ci ^-^ f (<) comb
 where f c k xs = sum (map k (takeWhile (uncurry c) (zip xs (tail xs))) -- needs some details

get = (cf . map ((57 -) .ord) . show)

main = print$ get  (fst bounds) - get (snd bounds + 1)
