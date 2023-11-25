import re
from typing import Tuple, Callable, Iterable, Optional
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"
f = open(fname)
ftext=f.read()
flns=[line.strip() for line in ftext.split("\n")[:-1]]
f=flns

fgroups = ftext.split("\n\n")
if len(fgroups)>1:
    f=fgroups

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
        return Pt([x+y for x,y in zip(self,other,strict=True)])
    def __sub__(self,other):
        return Pt([x-y for x,y in zip(self,other,strict=True)])
    def __rsub__(self,other):
        return Pt([y-x for x,y in zip(self,other,strict=True)])
    def __radd__(self,other):
        return Pt([y+x for x,y in zip(self,other,strict=True)])
    def __rmul__(self,other):
        return Pt([other*x for x in self])
dirs = {
    "R":Pt((1,0)),
    "U":Pt((0,1)),
    "L":Pt((-1,0)),
    "D":Pt((0,-1))
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

#grid = [[(Pt(x,y),c) for x,c in enumerate(line)] for y,line in enumerate(f)]

s=0
hh="=-012"
for (line,ints) in zip(f,xss):
    l = len(line)
    os=s
    for k,c in enumerate(reversed(line)):
        s+=(hh.index(c)-2)*(5**k)
    print(line,s-os)



print(s)
i=0
while (5**i)*2.5<abs(s):
    i+=1

res = ""
while i>=0:
    s+= 2.5*(5**i)
    print(s,2*(5**i),s//(5**i))
    res+= hh[int(s//(5**i))]
    s%=5**i
    s=int(s-0.5*(5**i))
    i-=1
print(res)






