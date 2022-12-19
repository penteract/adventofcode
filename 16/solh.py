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
ll = list(reversed(sorted(m[k][0] for k in m)))

mx = sum(ll)
mxs = [0]
k=0
t=0
ll=iter(ll+[0]*30)
for i in range(15):
    t+=k
    mxs.append(t)
    t+=k
    mxs.append(t)
    k+=next(ll)
    k+=next(ll)
mxs = [(k-mxs[26]) for k in mxs]
    
print(mx)
d[(26,"AA","AA",())] = mxs[0] # best
h=[(mxs[0],26,mxs[0],"AA","AA",())]# h(n),t,place,opens


def opts(p):
    if m[p][0]>0:
        yield (p, [p])
    for e in m[p][1]:
        yield (e,[])

ll2 = list(reversed(sorted((m[k][0],k) for k in m))) #+[(0,"abc")]*30
def geth(nds,left,ln=0):
    l = iter((x[0] for x in ll2 if x[1] not in nds))
    k=sum(m[k][0] for k in nds)
    t=0
    for i in range(left):
        t+=k
        if i%2==(ln==2): #if i%2: also works for my input, but I'm not convinced it's universally correct
            k+=next(l)
            k+=next(l)
    return -t

i=0
while h:
    rel,n,he,p1,p2,st=heappop(h)
    i+=1

    #print(i)
    if (i%100000==0):
        print(i,len(h),rel,n,p1,p2,st)
    if n==0:
        print(-(rel-he))
        break
    rel-=he
    he2 = mxs[len(st)+2] - mxs[len(st)+2+n]
    nxrel = rel-sum(m[k][0] for k in st)
    for a,ps in opts(p1):
        for b,ps2 in opts(p2):
            tt = tuple(sorted(set(st+tuple(ps+ps2))))
            he2 = geth(tt,n-1,len(ps)+len(ps2)) #mxs[len(tt)+1] - mxs[len(tt)+n]
            t = (nxrel+he2, n-1,he2, max(a,b),min(a,b), tt)
            if d[t[1:]]>t[0]:
                d[t[1:]]=t[0]
                heappush(h, t)













