import Data.Char
import Data.Bits

(.^.) a b = fromEnum a `xor` fromEnum b


proc (x:y:rs) = let p = proc (y:rs) in if p/=[] && head p.^.x==32 then tail p else (x:p)
proc c = c

main = do
    t <- readFile "day5.txt"
    let s = proc t
    putStrLn $ show $ length s
    putStrLn $ show $ [length (proc (filter ((/= c).toLower) s)) | c <-['a'..'z']]
    putStrLn .show $ (head s,last s)
