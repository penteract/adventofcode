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

m = {}
for (line,ints) in zip(f,xss):
    k = line[6:8]
    if "valves" in line:
        es = line[line.index("valves")+6:].split(",")
    else:
        es = line[line.index("valve")+5:].split(",")
    m[k] = (ints[0],[x.strip()for x in es])
from  heapq import *

ll = list(reversed(sorted(m[k][0] for k in m)))

mx = sum(ll)
mxs = []
k=0
t=0
ll=iter(ll+[0]*20)
for i in range(15):
    t+=k
    mxs.append(t)
    t+=k
    mxs.append(t)
    k+=next(ll)
    

d[(30,"AA",())] = -mx*30 # best
h=[(-mx*30,30,"AA",())]# h(n),t,place,opens

i=0
while h:
    rel,n,p,st=heappop(h)
    i+=1
    if (i%100000==0):
        print(i,len(h),rel,n,p,st)
    if n==0:
        print(-rel)
        break
    rel+=mx
    if m[p][0]>0 and p not in st:
        heappush(h,
                 (rel-sum(m[k][0] for k in st), n-1, p, tuple(sorted(st+(p,))))
                  )
    for e in m[p][1]:
        t = (rel-sum(m[k][0] for k in st), n-1, e, st+(p,))
        if d[t[1:]]>t[0]:
            d[t[1:]]=t[0]
            heappush(h,
                 (rel-sum(m[k][0] for k in st), n-1, e, tuple(sorted(st)))
                  )
    













