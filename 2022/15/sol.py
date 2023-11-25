import re
from typing import Tuple, Callable, Iterable, Optional
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"
f = open(fname)
ftext=f.read()
f=[line.strip() for line in ftext.split("\n")]

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

s=set()
yy=2000000
#yy=111810
if len(f)<20:
    yy=10

r = []

def addrange(ranges,sx,ex):
    rn=iter(ranges)
    nr = []
    for r in rn:
        if r[0]>ex+1:
            nr.append((sx,ex))
            nr.append(r)
            for k in rn:
                nr.append(k)
            return nr
        elif r[1]+1<sx:
            nr.append(r)
        else:
            s = min(sx,r[0])
            e = max(ex,r[1])
            for k in rn:
                if k[0]>e+1:
                    nr.append((s,e))
                    nr.append(k)
                    break
                elif k[1]>e:
                    e=k[1]
            else:
                nr.append((s,e))
            for k in rn:
                nr.append(k)
            return nr
    nr.append((sx,ex))
    return nr
            
ranges = [[] for i in range(2*yy)]


for (line,ints) in zip(f,xss):
    print(line,ints,yy)
    if line:
        sx,sy,bx,by = ints
        dd = abs(sx-bx)+abs(sy-by)
        for y in range(max(0,sy-dd-1),min(2*yy,sy+dd+2)):
            diff = dd - abs(sy-y) 
            if diff<0:
                continue
            ranges[y] = addrange(ranges[y],sx-diff,sx+diff)
            if y==yy:
                print(-diff,diff+1,ranges[y])

for y,r in enumerate(ranges):
    for a,b in zip(r,r[1:]):
        if a[1]+1<b[0] and (a[1]+1)>0 and (a[1]+1)<4000000:
            print(4000000*(a[1]+1)+y)
            #pass
#print(ranges[10])
#print(len(d)-len(s))










