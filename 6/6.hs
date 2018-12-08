import Data.Char
import Control.Arrow
import Data.List
import Data.Maybe
import Control.Monad
import qualified Data.Map as M

gi :: String -> Int
gi "" = 0
gi (c:rs) = (ord c - 48) + 10*gi rs

ri :: String -> (Maybe Int,String)
ri "" = (Nothing,"")
ri (d:rs) = (if d `elem` ['0'..'9'] then first (return.gi.foldl (flip (:)) [d]).(span (`elem` ['0'..'9']))  else ri) rs

get = unfoldr ((uncurry$flip$fmap.flip(,)).ri)

powset [] = [[]]
powset (x:xs) = let p = powset xs in p ++ map (x:) p

-- probably unnecessary - anything that hits the bounding box must be infinite
fin :: (Int,Int) -> [(Int,Int)] -> Bool
fin r rs = all id [any id [ ((y - b) >= (abs (x-a))) | (x,y) <- xys ,(x,y)/=(a,b)] | ((a,b):xys) <- [map (foldl (.) id fs) (r:rs) | fs<-powset [swap,negate***negate] ] ]

fins :: [(Int,Int)] -> [(Int,Int)]
fins dat =  filter (flip fin dat) dat

pair [x,y] = (x,y)
swap = uncurry $ flip (,)


type A = M.Map (Int,Int) Node

type Pos = (Int,Int)
type Label = (Int,Int)

bfsStep :: [(Pos,Label)] -> Int -> A -> (A,[(Pos,Label)])
bfsStep new time prev = foldl' (\ (a,next) (p,l) -> second (++next) $
                          let x = M.lookup p a in
                              case x of
                                Nothing -> (M.insert p (Node time (Just l)) a, zip (neighbs p) (repeat l))
                                (Just (Node old l')) -> (if old==time && l'/=Just l then M.insert p (Node time Nothing) a else a ,[])
                        ) (prev,[]) new

data Node = Node { dist :: Int , nearest :: Maybe Label}

neighbs = flip map [ix (+d) | d <-[1,-1] , ix <-[first,second]] . flip ($)


doall :: [Label] -> [(Pos,Label)] -> Int -> A -> A
doall fins gen time a
  | any ((`elem` fins).snd) gen = let (b,next) = bfsStep gen time a in doall fins next (time+1) b
  | otherwise = a

manhat (x,y) (z,w) = abs (x-z) + abs (y-w)



main = do
    f <- readFile "input"
    let d =  map (pair.get) $ lines f
    let dd p = sum $ map (manhat p) d
    putStrLn.show $ foldr1 min [dd (0,x) | x <- [1..300]]
    putStrLn.show $ foldr1 min [dd (x,0) | x <- [1..300]]
    putStrLn.show $ foldr1 min [dd (400,x) | x <- [1..300]]
    putStrLn.show $ foldr1 min [dd (x,400) | x <- [1..300]]
    putStrLn.show $ length $ filter (<10000) $ [dd (x,y) |x<-[0..400],y<-[0..400]]
    let dfin = fins d
    putStrLn . show $ d
    putStrLn . show $ dfin
    let a = doall dfin (map (join (,)) d) 0 M.empty
        counts = foldl' (\m n -> maybe m (\n -> M.insertWith (+) n 1 m) (nearest$snd n) ) M.empty (M.toList a)
    putStr $ unlines (map (map (chr.(+ 48).(`mod`60).(uncurry (+)).(fromMaybe (0,0)).(>>=nearest))) [[M.lookup (x,y) a | x <- [170..220]] | y <- [70..120]] )
    putStrLn $ unlines [show k ++ " " ++ show (M.lookup k counts) | k <- dfin]
