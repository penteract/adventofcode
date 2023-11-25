import re,math
from typing import Tuple, Callable, Iterable, Optional
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"
f=[line.strip() for line in open(fname)]

from collections import defaultdict

d=defaultdict(int)

#copied from https://github.com/joefarebrother/adventofcode/blob/master/misc_utils.py
def lmap(f: Callable, *xs) -> list:
    """Like map but returns a list"""
    return list(map(f, *xs))

def ints(xs: Iterable) -> list[int]:
    """Casts each element of xs to an int"""
    return lmap(int, xs)

def mint(x, default=None):
    """Maybe int - casts to int and returns default on failure"""
    try:
        return int(x)
    except ValueError:
        return default

def ints_in(x: str) -> list[int]:
    """Finds and parses all integers in the string x"""
    ex = r'(?:(?<!\d)-)?\d+'
    return ints(re.findall(ex, x))


class Pt(tuple):
    def __add__(self,other):
        return Pt([x+y for x,y in zip(self,other)])
    def __sub__(self,other):
        return Pt([x-y for x,y in zip(self,other)])
    def __rsub__(self,other):
        return Pt([y-x for x,y in zip(self,other)])
    def __radd__(self,other):
        return Pt([y+x for x,y in zip(self,other)])
    def __rmul__(self,other):
        return Pt([other*x for x in self])
dirs = {
    "R":Pt((0,1)),
    "U":Pt((1,0)),
    "L":Pt((0,-1)),
    "D":Pt((-1,0))
    }
ods = list(dirs.values())

#odirs = [(0,1),(1,0),(0,-1),(-1,0)]
ddirs = lmap(Pt,[(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)])

def cmp(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return 0 if a==b else -1 if a<b else 1
    if isinstance(a,int):
        a=[a]
    if isinstance(b,int):
        b=[b]
    for x,y in zip(a,b):
        if (k:=cmp(x,y))!=0:
            return k
    return cmp(len(a),len(b))
f=iter(f)
i=1
s=0

s1=[[2]]
s2=[[6]]
aa=[s1,s2]
for l in f:
    if l=="":
        l=next(f)
    l2=next(f)
    l=eval(l)
    r=eval(l2)
    if cmp(l,r)==-1:
        s+=i
    i+=1
    aa.append(l)
    aa.append(r)

#key=lambda x,y:cmp(x,y)<0
def fst(xs):
    if isinstance(xs,int):
        return xs
    if len(xs)<1:
        return -1
    else:
        return fst(xs[0])
ls = [fst(a) for a in aa]
print( ls)
ls.sort()
#ss=sorted(aa,)
a=ls.index(2)
b=ls.index(6)


print((a+1)*(b+1))














