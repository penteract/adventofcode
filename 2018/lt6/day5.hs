import Data.Char
import Data.Bits

(.^.) a b = fromEnum a `xor` fromEnum b

proc( x:y:rs) = if x.^.y == 32 then proc rs else x:proc (y:rs)
proc c = c

f ss = let s = proc ss in if s == ss then s else f s



main = do
    t <- readFile "tmp5.txt"
    let s = f t
    putStrLn $ show $ [length (f (filter ((/= c).toLower) s)) | c <-['a'..'z']]
    putStrLn .show $ (head s,last s)