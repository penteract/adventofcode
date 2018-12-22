import Data.Set as M

r2 s = 

loop :: M.Set (Integer,Integer) -> IO ()
loop m = do
  l <- getLine
  let ((n,s):_) = reads $ Prelude.drop 8 l
  print n
  if M.member n m then print n else loop (M.insert n  m)
  

main :: IO ()
main =
  loop M.empty
