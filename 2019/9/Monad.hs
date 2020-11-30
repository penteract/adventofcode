{-# LANGUAGE MonadComprehensions, LambdaCase, BlockArguments #-}

module Monad where
import Data.Char
import Control.Arrow
import Data.List
import Data.Maybe
import Control.Monad
import Control.Monad.State.Strict
import Control.Monad.Writer.Strict
import Control.Monad.Except
import Control.Applicative
import qualified Data.Map.Strict as M
import Data.Bits
import System.IO.Unsafe
import Data.Monoid
import System.Process

(.:) = (.)(.)(.)

data PState = S {ip :: Int, mem :: M.Map Int Int, inp :: [Int], reloff :: Int} deriving Show

incIP :: Int -> PState -> PState
incIP n (S ip mem inp off) = S (ip+n) mem inp off

setIP :: Int -> PState -> PState
setIP n (S _ mem inp off) = S n mem inp off


adjRel :: Int -> PState -> PState
adjRel n (S ip mem inp off) = S ip mem inp (off+n)

psSetAt :: Int -> Int -> PState -> PState
psSetAt n x (S ip mem inp off) = S ip (M.insert n x mem) inp off

newState :: [Int] -> [Int] -> PState
newState xs inp = S 0 (M.fromList (zip [0..] xs))  inp 0

readInp :: M Int
readInp = do
  S ip m inp off <- get
  case inp of
    (x:xs) -> put (S ip m xs off) >> return x
    [] -> throwError "Out of input"


type M a = (ExceptT String (WriterT [Int] (State PState))) a

(?) :: MonadError e m => Maybe a -> e -> m a
Nothing ? s = throwError s
Just a ? _ = return a

getAt :: Int -> M Int
getAt n = gets (M.lookup n . mem) >>= \case
  Nothing ->  return 0-- throwError "Out of Bounds"
  (Just a) -> return a

getRel :: Int -> M Int
getRel d = gets ((d+) . ip) >>= getAt

getI = getRel 0

getRelOff :: Int -> M Int
getRelOff d = gets reloff >>= (\ off -> getAt (off+d)  )

setAt' :: Int -> Int -> M ()
setAt' n x = modify (psSetAt n x)

setAt :: Int -> Int -> M ()
setAt n x = getAt n >> setAt' n x -- Bounds check


setRelOff :: Int -> Int -> M ()
setRelOff d x = gets reloff >>= (\ off -> setAt (off+d)  x)

-- setRel :: Int -> a -> M ()
-- setRel d x = gets ((d+) . ip) >>= flip setAt x
