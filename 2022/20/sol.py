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
xs = [811589153*k for k in xs]
811589153

l = [a+b for a,b in (enumerate(xs))]
l2 =list(l)
print(len(l))
for kk in range(10):
    for k in l2:
        ix = l.index(k)
        #while l[ix][0]!=i:
        #    ix=(ix+1)%len(l)
        v = l[ix] - (l[ix]%811589153)
        np = (ix+v)%(len(l)-1)
        #np = (np+len(l)-1)%(len(l)-1)
        if np==ix:
            continue
        elif np<ix:
            l = l[:np] + [l[ix]] + l[np:ix]+l[ix+1:]
        else:
            np+=1
            l = l[:ix] + l[ix+1:np] + [l[ix]] + l[np:]
        #print(l)
#print(l)    
ix=[j for j,k in enumerate(l) if k//811589153==0][0]

s=0
for i in range(1000,4000,1000):
    print(l[(ix+i)%len(l)])
    a = l[(ix+i)%len(l)]
    a = a - (a%811589153)
    s+=a

print(s)











