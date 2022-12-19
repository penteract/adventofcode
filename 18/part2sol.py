import re
from typing import Tuple, Callable, Iterable, Optional
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"
f = open(fname)
ftext=f.read()
f=[line.strip() for line in ftext.split("\n")[:-1]]

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
for (line,ints) in zip(f,xss):
    d[Pt(ints)]=1
pts = list(d)
bounds = [(min(pt[i] for pt in pts),max(pt[i] for pt in pts)) for i in range(3)]
print(bounds)
bb={}
def internal(pt):
    print("int",pt)
    if d[pt]==1:
        return True
    if pt in bb:
        return bb[pt]
    else:
        ch = {pt}
        nx = [pt]
    for p in nx:
        if hash(p)%10000==0:
            print(p)
        for a in [(1,0,0),(0,1,0),(0,0,1)]:
            for b in [1,-1]:
                kk = p+b*Pt(a)
                if pt==(2,2,5):
                    print(kk)
                if d[kk]==1 or kk in ch:
                    continue
                ch.add(kk)
                if any(kk[i]<=bounds[i][0] for i in range(3)) or any(kk[i]>=bounds[i][1] for i in range(3)):
                    for x in ch:
                        bb[x]=False
                    return bb[kk]
                if kk in bb:
                    for x in ch:
                        bb[x]=bb[kk]
                    return bb[kk]
                nx.append(kk)
    for x in ch:
        bb[x]=True
    return bb[pt]
    

for k in list(d):
    for a in [(1,0,0),(0,1,0),(0,0,1)]:
        for b in [1,-1]:
            kk = b*Pt(a)
            #print(kk)
            if d[k+kk]!=1 and not internal(k+kk):
                s+=1
    
print(s)
