import re
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

try:
    xs = ints(f)
except Exception:
    pass
try:
    xss = lmap(ints_in,f)
except Exception:
    pass

s=0

print("hi")

for ints in xss:
    pts = lmap(Pt,zip(ints[0::2],ints[1::2]))
    #d[pts[0]]=1
    for l,r in zip(pts,pts[1:]):
        a=l[0]
        for x in range(min(l[0],r[0]),max(l[0],r[0])+1):
            for y in range(min(l[1],r[1]),max(l[1],r[1])+1):
                d[(x,y)]=1

mx = max(p[1] for p in d)
n=0
while True:
    x=500
    y=0
    #print(x,y)
    while y<=mx:
        if d[x,y+1]==0:
            y+=1
        elif d[x-1,y+1]==0:
            y+=1
            x-=1
        elif d[x+1,y+1]==0:
            y+=1
            x+=1
        else:
            break
    n+=1
    d[x,y]=2
    if (x,y)==(500,0):
        break

print(n)











