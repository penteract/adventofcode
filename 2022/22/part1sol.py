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

d={} #defaultdict(int)

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

s=0
tops = {}
bots = {}
left = None
right = None
loop = {}
for y,l in enumerate(f[0].split("\n")):
    left=None
    for x,c in enumerate(l):
        if c in ".#":
            d[x,y] = c
            if left is None:
                left = x
            right=x
            bots[x]=y
            if x not in tops:
                tops[x] = y
    if y==0:
        p=Pt((left,0))
    loop[left-1,y] = (right,y)
    loop[right+1,y] = left,y
for x in bots:
    loop[x,tops[x]-1] = x,bots[x]
    loop[x,bots[x]+1] = x,tops[x]


dr = Pt((1,0))
for ss in f[1].split("R"):
    ss.split("L")
    for s in ss.split("L"):
        k = int(s)
        print(p,k)
        for i in range(k):
            nx = p+dr
            if nx not in d:
                print("l",nx,loop[nx])
                nx = loop[nx]
            if d[nx]=="#":
                break
            p=nx
        x,y = dr
        dr = Pt((y,-x))
    dr = (-1)*dr
x,y = dr
dr = Pt((y,-x)   )
x,y = p
x+=1
y+=1
dx,dy=dr
print(x,y,dr)
print(x*4+y*1000+(-dx-dy)+bool(dy)+1)


#print(s)









