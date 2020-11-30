{-# LANGUAGE MonadComprehensions, LambdaCase, BlockArguments, DeriveGeneric #-}

module AbsInt where
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
import Monad
import Generics.Deriving.Functor
import Generics.Deriving
import Data.Functor.Identity

data Expr = I Int | Var String | (:+) Expr Expr | (:*) Expr Expr | Ref Expr deriving (Generic)

instance Show Expr where
  show (I n) = show n
  show (Var s) = s
  show (x:+ y) = "("++show x ++ "+"++ show y++")"
  show (Ref e) = "{"++show e++"}"
  show (x:* y) = show x ++ "*"++ show y

intom :: Applicative f => (Expr -> f Expr) -> Expr -> f Expr
intom f (x :+ y) = liftA2 (:+) (f x) (f y)
intom f (x :* y) = liftA2 (:*) (f x) (f y)
intom f (Ref x) = Ref <$> f x
intom f x = pure x



into f x = runIdentity ((Identity . f) `intom`  x)

simp (I x :+ I y) = I (x+y)
simp (I x :* I y) = I (x*y)
simp (x :+ I y) = simp (I y :+ x)
simp (x :* I y) = simp (I y :* x)
simp (x:+(y:+z)) = simp ((x:+y) :+z)
simp (x:*(y:*z)) = simp ((x:*y) :*z)
simp (x:*(y:+z)) = simp ((x:*y) :+ (x:* z))
simp a = simp `into` a

instance Value Expr where
  add = simp .: (:+)
  mul = simp .: (:*)
  op = \case I 1 -> Just Add
             I 2 -> Just Mul
             I 99 -> Just Halt
             _ -> Nothing
  ref (I n) = Right n
  ref x = Left (Ref x)
