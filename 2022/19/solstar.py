import re
from typing import Tuple, Callable, Iterable, Optional
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input2"
f = open(fname)
ftext=f.read()
f=[line.strip() for line in ftext.split("Blueprint")[1:]]

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
bps = []
for (line,ints) in zip(f,xss):
    ints=ints[1:]
    if (len(ints)!=6):
        print(line)
    assert (len(ints)==6)
    bps.append(((ints[0],0,0),(ints[1],0,0),(ints[2],ints[3],0),(ints[4],0,ints[5])))

from functools import cache

def getposs(costs,mm):
    if len(costs)==0:
        yield (tuple(),mm)
    else:
        c=costs[0]
        #print(mm,c)
        for n in range(min(a//b for a,b in zip(mm,c) if b!=0)+1):
            for (nn,x) in getposs( costs[1:],tuple(mmm-cc*n for mmm,cc in zip(mm,c))):
                yield ((n,)+nn, x)
        

# time,amounts,robs
cache = {}
def best(costs, t=32,mm=Pt((0,0,0)),rs=Pt((1,0,0))):
    if (t,mm,rs) in cache:
        return cache[(t,mm,rs)]
    if t>20:
        print(t,costs,mm,rs)
    if t<=1:#robots built now don't count
        return 0
    mx = 0
    #if all(a<b for a,b in zip(costs[ix],mm)):
    #    mn-costs[ix]
    for ix in range(4):
        if ix==0 and rs[0]>=max(costs[i][0] for i in range(1,4)):
            continue
        if 5-ix>t:
            continue
        if any (costs[ix][i]>0 and rs[i]==0 for i in range(1,3)):
            continue
        #print(costs[ix],ix,rs,mm)
        tt = 1 + max( 1+((max(0,costs[ix][i]-mm[i])-1)//rs[i]) for i in range(3) if costs[ix][i]>0)
        rs_ = Pt(x+(j==ix) for j,x in enumerate(rs))
        #print(tt)
        #if t>12:
            #print(t,tt,ix,costs[ix], )
            #print(t-tt,mm+(tt*rs)-costs[ix],rs_)
            #print(best(costs,t-tt,mm+(tt*rs)-costs[ix],rs_) + (t-tt)*(ix==4))
        mx = max(mx, best(costs,t-tt,mm+(tt*rs)-costs[ix],rs_) + (t-tt)*(ix==3))

    cache[(t,mm,rs)]=mx
    return mx


l=[]
for a,cs in enumerate(bps):
    if a<3:
        l.append(best(cs))
    print(l[-1])
    cache={}
p=1
for x in l:
    p*=x
print(p)
















