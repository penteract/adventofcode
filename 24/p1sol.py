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
    def wrap(self):
        x,y=self
        return Pt((x%wid, y%height))
dirs = {
    "v":Pt((0,1)),
    ">":Pt((1,0)),
    "^":Pt((0,-1)),
    "<":Pt((-1,0))
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
    pass

print("hello")
height = len(f)-2
wid = len(f[0])-2
print(height,wid)
pr = wid*height
if not( wid%5 or height%5):
    pr//=5
print(wid*height,pr)
bs = set()
for y,line in enumerate(f[1:-1]):
    line=line[1:-1]
    for x,c in enumerate(line):
        if c in dirs:
            bs.add(((x,y),dirs[c]))

prev=bs
mp_ = []
for t in range(pr ):
    if t%10==0:print(t)
    nx = set()
    mp_.append(set())
    for k in prev:
        mp_[-1].add(k[0])
        nx.add(((k[0]+k[1]).wrap(), k[1]))
    prev = (nx)
print("genmp")
from  heapq import *

print(wid*height)


init = (0,Pt((0,-1)))#negated time

def h(pt):
    t,(x,y)=pt
    return (abs(x-wid+1)+abs(y-height) - t, pt)
    
hq=[h(init)]
seen = {init}
i=0
while True:
    i+=1
    hh,(t,p) = heappop(hq)
    if i%100000==0:
        print(i,":",hh,t,p)
    if hh==-t:
        print(hh)
        break
    for dr in ods+[Pt((0,0))]:
        pt = p+dr
        #print(pt)
        if pt not in mp_[(1-t)%pr] and (pt==pt.wrap() or pt==init[1] or pt==(wid-1,height)):
            nx = h((t-1, pt))
            if nx[1] not in seen:# (pt not in best) or best[pt] > nx[0]:
                seen.add(nx[1])
                heappush(hq,nx)
            #    best[pt]=nx[0]








