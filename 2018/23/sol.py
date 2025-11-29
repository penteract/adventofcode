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

tot=0
d=defaultdict(int)
octfaces = [[1,1,1],[1,-1,-1],[-1,-1,1],[-1,1,-1]]
bots = []
for y,line in enumerate(flns):
    x,y,z,r = ints(line)
    intervals=[]
    for a,b,c in octfaces:
        intervals.append( (x*a+y*b+z*c - r, x*a+y*b+z*c + r))
    bots.append(intervals)

def empty(a,b,c,d):
    return a[0]>a[1] or b[0]>b[1] or c[0]>c[1] or d[0]>d[1] or a[0]+b[0]+c[0]+d[0]>0 or a[1]+b[1]+c[1]+d[1]<0
def inter(xs,ys):
    return [(max(x[0],y[0]), min(x[1],y[1])) for x,y in zip(xs,ys)]
best = 0
def search(cur,nx,cl=0):
    global best
    nxs = [x for x in nx if not empty(*inter(cur,x))]
    if cl+len(nxs)<best:
        return
    if len(nxs)==0:
        best=cl
        print(cl, cur)
    for i in range(len(nxs)):
        if len(nxs)+cl+1<best: break
        search(inter(cur,nxs[i]), nxs[i+1:], cl+1)

bots.sort(key=lambda x:x[0][1] - x[0][0] ) # negative, biggest at front
mx = max([x for b in bots for c in b for x in c])
mn = min([x for b in bots for c in b for x in c])
print(search([(mn,mx)]*4 ,bots))
def getpt(a,b,c,d):
    for w in range(a[0],a[1]+1):
        for x in range(b[0],b[1]+1):
            for y in range(c[0],c[1]+1):
                for z in range(d[0],d[1]+1):
                    if w+x+y+z==0:
                        yield ((w+x)//2,(w+y)//2,(w+z)//2)




