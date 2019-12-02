import Control.Arrow
import qualified Data.Map.Strict as M


n = 424
l = 7114400

type Cyc = ([Integer],Integer,[Integer])

compose = foldl (.) id

cw :: Cyc -> Cyc
cw (l,x,y:ys) = (x:l,y,ys)
cw (l,x,[]) = let (y:ys) = reverse (x:l) in ([],y,ys)

swp3 (a,b,c) = (c,b,a)

ccw = swp3 . cw . swp3

insert n (a,b,c) = (b:a,n,c)j

remove (a,b,(c:cs)) = (b,(a,c,cs))
remove (a,b,[]) = remove ([],b,reverse a)



step n
  | n `mod` 23 == 0 = first (+n) . remove . compose (replicate 7 ccw)
  | otherwise   = (,) 0 . insert n . cw

proc scores t cyc n l = if t > l then scores else
                      let (a,nxt) = step t cyc in proc (M.insertWith (+) (t `mod` n) a scores) (t+1) nxt n l

main = do
   putStrLn . show $ foldl1 max $ map snd $ M.toList $ proc M.empty 1 ([],0,[]) n l
  
