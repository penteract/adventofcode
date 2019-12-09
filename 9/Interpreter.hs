{-# LANGUAGE MonadComprehensions, LambdaCase, BlockArguments, FlexibleContexts #-}
module Interpreter where
import Data.Char
import Control.Arrow
import Data.List
import Data.Maybe
import Control.Monad
import Control.Monad.State hiding (get)
import Control.Monad.Except
import Control.Monad.Writer
import Control.Applicative
import qualified Data.Map as M
import Data.Bits
import System.IO.Unsafe
import Data.Monoid
import System.Process
import Monad


data BinOp = Add | Mul | Lt | Eq deriving (Eq, Show)
data Op = BinOp BinOp | In | Out | Jnz | Jz | ARl | Halt deriving (Eq,Show)

struct :: Op -> (Int,Int) --Number read, number written
struct Halt = (0,0)
struct In = (0,1)
struct Out = (1,0)
struct Jnz = (2,0)
struct Jz = (2,0)
struct ARl = (1,0)
struct (BinOp b) = (2,1)
len :: Op -> Int
len = (+ 1) . uncurry (+) . struct

{-
instance Enum Op where
  fromEnum (BinOp Add) = 1
  fromEnum (BinOp Mul) = 2
  fromEnum (BinOp Lt) = 7
  fromEnum (BinOp Eq) = 8
  fromEnum In = 3
  fromEnum Out = 4
  fromEnum Jnz = 5
  fromEnum Jz = 6
  fromEnum Halt = 99

  toEnum 1  = BinOp Add
  toEnum 2  = BinOp Mul
  toEnum 7  = BinOp Lt
  toEnum 8  = BinOp Eq
  toEnum 3  = In
  toEnum 4  = Out
  toEnum 5  = Jnz
  toEnum 6  = Jz
  toEnum 99 = Halt -}

toOp :: Int -> Maybe Op
toOp 1  = Just (BinOp Add)
toOp 2  = Just (BinOp Mul)
toOp 7  = Just (BinOp Lt)
toOp 8  = Just (BinOp Eq)
toOp 3  = Just In
toOp 4  = Just Out
toOp 5  = Just Jnz
toOp 6  = Just Jz
toOp 9  = Just ARl
toOp 99 = Just Halt
toOp _ = Nothing


fn :: BinOp -> Int -> Int -> Int
fn Add = (+)
fn Mul = (*)
fn Lt = fromEnum .: (<)
fn Eq = fromEnum .: (==)

data Mode = Ind | Imm | Rel deriving (Eq,Show)

see :: Mode -> Int -> String
see Ind x = '@':show x
see Imm x = '#':show x

seeOp (BinOp x) = show x
seeOp x = show x

toMode '0' = Just Ind
toMode '1' = Just Imm
toMode '2' = Just Rel
toMode _ = Nothing

getMode :: MonadError String m => Char -> m Mode
getMode x = maybe (throwError ("bad Mode : "++show x)) return (toMode x)

readMode :: Mode -> Int -> M Int
readMode Ind = getAt
readMode Imm = return
readMode Rel = getRelOff


writeMode :: Mode -> Int -> Int -> M ()
writeMode Ind = setAt
writeMode Imm = error "bad mode"
writeMode Rel = setRelOff

getOp :: MonadError String m => Int -> m Op
getOp x = case toOp x of
  Just o -> return o
  Nothing -> throwError ("bad op: "++show x)

(^⸴^) :: Applicative f => f b -> f c -> f (b,c)
(^⸴^) = liftA2 (,) -- Really, I'd like to use ^,^ or ^‚^ , but haskell doesn't allow either

getOpModes :: MonadError String m => Int -> m (Op,[Mode])
getOpModes n = do
  let (q,r) = n `divMod` 100
  getOp r ^⸴^ mapM getMode (take 10 $ reverse (show q) ++ repeat '0')

step :: M Bool
step = getI >>= getOpModes >>= uncurry applyOp

-- indirect :: Int -> M Int
-- indirect n = do
--   p <- getRel n
--   either return (getAt) p

rd :: Mode -> Int -> M (Mode,Int)
rd m x = (,) m <$> getRel x  --readMode m

applyOp :: Op -> [Mode] -> M Bool
applyOp Halt _ = return True
applyOp op modes = do
  a <- sequence$ zipWith rd modes [1..(len op - 1)]
  inps <- sequence$ map (uncurry readMode) (take (fst$ struct op) a)
  let outs = drop (fst$ struct op) a
  applyWith op inps outs
  modify (incIP $ len op)
  return False

-- Jump instructions are responsible for decreasing ip by their length
applyWith :: Op -> [Int] -> [(Mode,Int)] -> M ()
applyWith (BinOp b) [x,y] [z] = do
  uncurry writeMode z (fn b x y)
applyWith In [] [z] = do
  readInp >>= uncurry writeMode z
applyWith Out [x] [] = tell [x]
applyWith Jnz [x,y] [] = when (x/=0) (modify (setIP (y-3) ))
applyWith Jz [x,y] [] = when (x==0) (modify (setIP (y-3) ))
applyWith ARl [x] [] = (modify (adjRel x))
applyWith x y z = throwError ("Wrong number of args for "++ show x ++":"++ show y++ show z)

runProg :: M ()
runProg = do
  stop <- step
  if stop then return () else runProg

examine :: M a -> PState -> ((Either String a,[Int]),PState)
examine x s = runState (runWriterT (runExceptT x)) s
