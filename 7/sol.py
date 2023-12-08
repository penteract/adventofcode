import re
from typing import Tuple, Callable, Iterable, Optional
import sys
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
dirs = {
    "R":Pt((0,1)),
    "U":Pt((1,0)),
    "L":Pt((0,-1)),
    "D":Pt((-1,0))
    }
ods = list(dirs.values())

#odirs = [(0,1),(1,0),(0,-1),(-1,0)]
ddirs = lmap(Pt,[(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)])

##Input handling
flns=[line.strip() for line in ftext.split("\n")[:-1]]
f=flns

fgroups = ftext.split("\n\n")
if len(fgroups)>1:
    f=[g.split("\n") for g in fgroups]

try: xs = lmap(int,f)
except Exception: pass
try: xss = lmap(ints,f)
except Exception: pass


def fn(c):
    if c=="J":
        return -1
    if c in "TJQKA":
        return 10+"TJQKA".find(c)
    else:
        return int(c)
r=[]
for line in f:
    cc,n=line.split()
    l = [fn(x) for x in list(cc)]
    d = [(l.count(c),c) for c in set(l)]
    k = sorted(d,reverse=True)
    if len(k)>1 and (-1) in set(l):
        m = [c[1] for c in k if c[1]!=-1][0]
        ll=[x if x!=-1 else m for x in l]
        d = [(ll.count(c),c) for c in set(ll)]
        k = sorted(d,reverse=True)
        print(k)
    #r.append( (list(zip(*k)),int(n)) )
    r.append( (([x[0]for x in k],l,line),int(n)) )

print(f)
for k in r: print(k)
tot=0
for i,k in enumerate(sorted(r)):
    print(i,k,(i+1)*k[1])
    tot+=(i+1)*k[1]
#d=defaultdict(int)

print(tot)
