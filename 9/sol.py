import re
from typing import Tuple, Callable, Iterable, Optional
import sys
import math,functools,itertools
fname=sys.argv[1] if len(sys.argv)>1 else "input1"
f = open(fname)
ftext=f.read()

from collections import defaultdict

#copied from https://github.com/joefarebrother/adventofcode/blob/master/misc_utils.py
def lmap(f: Callable, *xs) -> list:
    return list(map(f, *xs))
def mint(x, default=None):
    try: return int(x)
    except ValueError: return default
def ints(x: str) -> list[int]:
    ex = r'(?:(?<!\d)-)?\d+'
    return lmap(int,re.findall(ex, x))

def ints_locs(x: str) -> list[tuple[int,tuple[int,int]]]:
    ex = r'(?:(?<!\d)-)?\d+'
    return [(int(x.group()),x.span()) for x in re.finditer(ex, x)]

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
    def left(self):
        x,y=self
        return Pt((y,-x))
    def right(self):
        x,y=self
        return Pt((-y,x))
def pt(*args):
    if len(args)==1: return Pt(args[0])
    else: return Pt(args)
dirs = {
    "R":Pt((1,0)),
    "U":Pt((0,-1)),
    "L":Pt((-1,0)),
    "D":Pt((0,1))
    }
ods = list(dirs.values())

#odirs = [(0,1),(1,0),(0,-1),(-1,0)]
ddirs = lmap(Pt,[(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)])

##Input handling
flns=[line.strip() for line in ftext.split("\n")[:-1]]
f=flns

fgroups = ftext.split("\n\n")
if len(fgroups)>1:
    fgs = [g.split("\n") for g in fgroups]
    fgns = [lmap(ints,g) for g in fgs]

try: xs = lmap(int,f)
except Exception: pass
try: xss = lmap(ints,f)
except Exception: pass

tot=0
d=defaultdict(int)

l=[]
for y,line in enumerate(flns):
    ins = pt(ints(line))
    d[ins]=1
    l.append(ins)
xs = sorted(set(p[0] for p in l))
ys = sorted(set(p[1] for p in l))
ps = list(zip(l,l[1:]+l[:1]))
vs = [(a[0],min(a[1],b[1]),max(a[1],b[1])) for (a,b) in ps if a[0]==b[0]]
xi = {x:i for i,x in enumerate(xs)}
yi = {x:i for i,x in enumerate(ys)}
from functools import cache
def online(a,b,p):
    return min(a[0],b[0])<=p[0]<=max(a[0],b[0]) and min(a[1],b[1])<=p[1]<=max(a[1],b[1])
@cache
def inshape(i,j):
    """given is the region xs[i] x ys[j] inside?"""
    x = xs[i//2] + i%2
    y = ys[j//2] + j%2
    p = pt(x,y)
    n=0
    for a,b in ps:
        if online(a,b,p):
            return True
    for a,b,c in vs:
        if b<=y<c and a<x:
            n+=1
    return bool(n%2)
def allin(p,q):
    i0 = xi[p[0]]
    i1 = xi[q[0]]
    if i0>i1:
        i0,i1=i1,i0
    j0 = yi[p[1]]
    j1 = yi[q[1]]
    if j0>j1:
        j0,j1=j1,j0
    for i in range(i0*2,i1*2+1):
        for j in range(j0*2,j1*2+1):
            if not inshape(i,j):
                break
        else:
            continue
        break
    else:
        return True
    return False

for i,a in enumerate(l):
    #ai=xi[a]
    for b in l[i+1:]:
        if allin(a,b):
            tot=max(tot, (1+abs(a[0]-b[0]))*(abs(a[1]-b[1])+1))
            #print(tot,a,b)
print(tot)






























