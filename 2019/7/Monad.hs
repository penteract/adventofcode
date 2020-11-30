{-# LANGUAGE MonadComprehensions, LambdaCase, BlockArguments #-}

module Monad where
import Data.Char
import Control.Arrow
import Data.List
import Data.Maybe
import Control.Monad
import Control.Monad.State
import Control.Monad.Writer
import Control.Monad.Except
import Control.Applicative
import qualified Data.Map as M
import Data.Bits
import System.IO.Unsafe
import Data.Monoid
import System.Process

(.:) = (.)(.)(.)

data PState = S {ip :: Int, mem :: M.Map Int Int, inp :: [Int]} deriving Show

incIP :: Int -> PState -> PState
incIP n (S ip mem inp) = S (ip+n) mem inp

setIP :: Int -> PState -> PState
setIP n (S _ mem inp) = S n mem inp

psSetAt :: Int -> Int -> PState -> PState
psSetAt n x (S ip mem inp) = S ip (M.insert n x mem) inp

newState :: [Int] -> [Int] -> PState
newState xs inp = S 0 (M.fromList (zip [0..] xs))  inp

readInp :: M Int
readInp = do
  S ip m inp <- get
  case inp of
    (x:xs) -> put (S ip m xs) >> return x
    [] -> throwError "Out of input"


type M a = (ExceptT String (WriterT [Int] (State PState))) a

(?) :: MonadError e m => Maybe a -> e -> m a
Nothing ? s = throwError s
Just a ? _ = return a

getAt :: Int -> M Int
getAt n = gets (M.lookup n . mem) >>= \case
  Nothing -> throwError "Out of Bounds"
  (Just a) -> return a

getRel :: Int -> M Int
getRel d = gets ((d+) . ip) >>= getAt

getI = getRel 0

setAt' :: Int -> Int -> M ()
setAt' n x = modify (psSetAt n x)

setAt :: Int -> Int -> M ()
setAt n x = getAt n >> setAt' n x -- Bounds check

-- setRel :: Int -> a -> M ()
-- setRel d x = gets ((d+) . ip) >>= flip setAt x
