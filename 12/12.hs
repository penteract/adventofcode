import Control.Monad.State
import Data.Maybe
import Data.List
import qualified Data.Map as M

type Memo a = State (M.Map (Int,Int,Int) Tr) a

data Dat = E | F deriving Show


-- `Br hash n x y` is a pair of Trees of size 2^n (n>=1). Leaf x has size zero
data Tr = Leaf Dat | Br Integer Tr Tr deriving Show

depth (Leaf _) = 0
depth (Br _ t _) = 1+ depth t

toC (Leaf E) = '.'
toC (Leaf F) = '#'

frC '.' = Leaf E
frC '#' = Leaf F

step = frC . s' . map toC
  where
    s' "##..."  = '.'
    s' "##.##"  = '.'
    s' ".#.#."  = '#'
    s' "#..#."  = '.'
    s' "#.###"  = '#'
    s' ".###."  = '.'
    s' "#.#.."  = '.'
    s' "##..#"  = '.'
    s' "....."  = '.'
    s' "...#."  = '.'
    s' ".#..#"  = '.'
    s' "####."  = '#'
    s' "...##"  = '#'
    s' "..###"  = '#'
    s' "#.#.#"  = '#'
    s' "###.#"  = '#'
    s' "#...#"  = '#'
    s' "..#.#"  = '.'
    s' ".##.."  = '#'
    s' ".#..."  = '#'
    s' ".##.#"  = '#'
    s' ".####"  = '.'
    s' ".#.##"  = '.'
    s' "..##."  = '.'
    s' "##.#."  = '.'
    s' "#.##."  = '.'
    s' "#..##"  = '.'
    s' "###.."  = '.'
    s' "....#"  = '.'
    s' "#####"  = '#'
    s' "#...."  = '.'
    s' "..#.."  = '#'

hash :: Tr -> Integer
hash (Br h _ _) = h
hash (Leaf E) = 0
hash (Leaf F) = 1

hi = fromInteger.hash

mkT :: Tr -> Tr -> Tr
mkT l r = Br ((104729 + (1191679 * hash l) + hash r) `mod` 15284271881 ) l r

empty 0 = Leaf E
empty n = let e = empty (n-1)
                  in mkT e e

toKey :: Tr -> Tr -> Tr -> (Int,Int,Int)
toKey l c r = (hi l, hi c, hi r)

toLst :: Tr -> [Tr]
toLst (Br n l r) = [l,r]

sects :: Int -> [a] -> [[a]]
sects n xs = take (length xs - n + 1) $ (map $ take n) $ tails xs

-- | make sure the list has length 6
comp :: [Tr] -> Memo Tr
comp t@(Leaf a : rs) =return$  mkT (step $ take 5 t) (step $ tail t)
comp trs = do
  fours <- sequence $ map (\ [q,w,e] -> do3 q w e) $ sects 3 trs
  lr <- sequence $ map (\ [q,w,e] -> do3 q w e) $ sects 3 fours
  let [l,r] = lr
  return $ mkT l r


-- for 3 adjacent Trs of depth d, compute the state of the central one 2^(d-1) steps in the future
do3 :: Tr -> Tr -> Tr -> Memo Tr
do3 l c r = do
  let k = toKey l c r
  mres <- gets (M.lookup k)
  res <- maybe (comp $ [l,c,r] >>= toLst ) return mres
  modify $ M.insert k res
  return res


disp :: Tr -> String
disp (Br n l r) = disp l ++disp r
disp l = return $ toC l

undisp (a:l)= fst $ undisp' (map frC l) 0 (frC a)
  where
    undisp' [] n t = (t,[])
    undisp' l@(_:_) n t = let (t',l')= mkUpTo n l in undisp' l' (n+1) (mkT t t')
    mkUpTo n [] = (empty n,[])
    mkUpTo 0 (a:l) = (a,l)
    mkUpTo n l = let (t,l') = mkUpTo (n-1) l
                     (t',l'') = mkUpTo (n-1) l' in
                 (mkT t t' , l'')


-- | Given a list of trees of the same nonzero depth d, calculate the generation 2^(d-1)
doRow :: [Tr] -> Memo [Tr]
doRow (a:b:c:rs) = do3 a b c >>= (\ a -> (a:) <$> doRow (b:c:rs))
doRow _ = return []


-- | Given a list of depth 1 trees, compute exactly n generations
doN :: Integer -> [Tr] -> Memo [Tr]
doN 0 ts = return ts
doN i ts = do
  let e = empty $ depth $ head ts
  next <- if i `mod` 2 == 0
    then return ts
    else  doRow $ e:e:ts ++[e,e]
  doN  (i`div`2) (dLst next)

-- | halve the length of a list of trees while increasing their depth
dLst :: [Tr] -> [Tr]
dLst [] = []
dLst (a:b:rs) = mkT a b : dLst rs
dLst [a] = [mkT a (empty (depth a))]

checkT (Leaf _) = True
checkT (Br _ l r) = if depth l /= depth r then False else checkT l && checkT r

--exl


-- | read a string into a list of depth 2 trees
readL = dLst . map frC

showL = join . map disp

ss = "#..####.##..#.##.#..#.....##..#.###.#..###....##.##.#.#....#.##.####.#..##.###.#.......#............"
rr = dLst $ map frC ss

showSt = showL . eSt

eSt = flip evalState M.empty

-- | get the sum of scores for a tree based at 0
get1 :: Tr -> State (M.Map Int (Integer,Integer)) (Integer,Integer)
get1 (Leaf E) = return (0,0)
get1 (Leaf F) = return (0,1)
get1 t@(Br k t1 t2) = do
  mres <- gets (M.lookup $ hi t)
  maybe (do (a,x) <- get1 t1
            (b,y) <- getn [t2] (2 ^ depth t1)
            modify $ M.insert (hi t) (a+x,b+y)
            return (a+x,b+y)
               ) return mres


getn :: [Tr] -> Integer ->  State (M.Map Int (Integer,Integer)) (Integer,Integer)
getn [] pos = return (0,0)
getn (t:ts) pos = let d = depth t in do
  (a,x) <- get1 t
  (b,y) <- getn ts (pos + (2^d))
  return (a+x*pos+b,x+y)

main :: IO ()
main = do
  putStrLn "done"


iterCountM :: (Monad m) => Int -> (a -> m a) -> a -> m [a]
iterCountM 0 _ _ = return []
iterCountM k step start = do
    first <- step start
    rest <- iterCountM (k-1) step first
    return (first:rest)
