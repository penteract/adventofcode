{-# LANGUAGE MonadComprehensions, LambdaCase, BlockArguments #-}

module Monad where
import Data.Char
import Control.Arrow
import Data.List
import Data.Maybe
import Control.Monad
import Control.Monad.State hiding (get)
import Control.Monad.Except
import Control.Applicative
import qualified Data.Map as M
import Data.Bits
import System.IO.Unsafe
import Data.Monoid
import System.Process

(.:) = (.)(.)(.)

data Op = Add | Mul | Halt

len :: Op -> Int
len Halt = 1
len Add = 4
len Mul = 4

class Show a => Value a where
  add :: a -> a -> a
  mul :: a -> a -> a
  op :: a -> Maybe Op
  ref :: a -> Either a Int

instance Value Int where
  add = (+)
  mul = (*)
  op = \case 1 -> Just Add
             2 -> Just Mul
             99 -> Just Halt
             _ -> Nothing
  ref = Right
data PState a = S {ip :: Int, mem :: M.Map Int a} deriving Show

incIP :: Int -> PState a -> PState a
incIP n (S ip mem) = S (ip+n) mem

psSetAt :: Int -> a -> PState a -> PState a
psSetAt n x (S ip mem) = S ip (M.insert n x mem)

newState :: [a] -> PState a
newState xs = S 0 $ M.fromList (zip [0..] xs)



type M v a = ExceptT String (State (PState v))  a

(?) :: MonadError e m => Maybe a -> e -> m a
Nothing ? s = throwError s
Just a ? _ = return a

getAt :: Int -> M a a
getAt n = gets (M.lookup n . mem) >>= \case
  Nothing -> throwError "Out of Bounds"
  (Just a) -> return a

getRel :: Int -> M a a
getRel d = gets ((d+) . ip) >>= getAt

getI = getRel 0

setAt' :: Int -> a -> M a ()
setAt' n x = modify (psSetAt n x)

setAt :: Int -> a -> M a ()
setAt n x = getAt n >> setAt' n x -- Bounds check

-- setRel :: Int -> a -> M a ()
-- setRel d x = gets ((d+) . ip) >>= flip setAt x

getOp :: Value a => a -> M a Op
getOp x = case op x of
  Just o -> return o
  Nothing -> throwError ("bad op: "++show x)
