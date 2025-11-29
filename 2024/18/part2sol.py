import re
from typing import Tuple, Callable, Iterable, Optional
import sys
import math,functools,itertools
fname=sys.argv[1] if len(sys.argv)>1 else "input"
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

from heapq import *
def ast(start,neighbs,done,h = lambda x:0):
    """Finds the node n such that done(n) with minimal distance from an element of start.
    neighbs(n) = [(nn,edgeweight)]
    assumes h(n)<d(n,end)
    Returns the path as a lisp-style deeply nested tuple"""
    seen=set()
    hq = []
    for x in start:
        heappush(hq,(h(x),(x,None),0))
    while hq:
        c,pth,d = heappop(hq)
        n=pth[0]
        if n not in seen:
            #print(n)
            seen.add(n)
            if done(n):
                return (pth,d)
            for x,dst in neighbs(n):
                if x not in seen:
                    heappush(hq,(d+dst+h(x),(x,pth),d+dst))

tot=0
d=defaultdict(int)
#
#
# for y,line in enumerate(flns):
#     for x,c in enumerate(line):
#         d[x,y]=c

def prgrid(d):
    xs = set(k[0] for k in d)
    ys = set(k[1] for k in d)
    for y in range(min(ys),max(ys)+1):
        for x in range(min(xs),max(xs)+1):
            k=x,y
            print(d[k] if d[k]!=0 else ".",end="")
        print()


#prgrid(d)

mx = 70 if fname=="input" else 6

def neighbs(pt):
    for dr in ods:
        #print(pt,dr)
        p = pt+dr
        if all(x>=0 for x in p) and all(x<=mx for x in p) and d[p]!="#":
            yield (p,1)
def done(pt):
    return pt==(mx,mx)

r = len(xss)
l = 1024 if fname=="input" else 12
while r>l+1:
    #print(l,r)
    m = (r+l)//2
    d = defaultdict(int)
    for g in xss[:m ]:
        x,y =g
        d[x,y]="#"
    rs = ast([Pt((0,0))],neighbs,done)
    if rs is None:
        r = m
    else:
        l=m

print(",".join(map(str,xss[l])))






























