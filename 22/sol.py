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

def f(k):
    k^=k*64
    k%=16777216
    k^=(k//32)
    k%=16777216
    k^=k*2048
    k%=16777216
    return k

r=[]
for k in xs:
    #print(k)
    r.append([k%10])
    for i in range(2000):
        k=f(k)
        r[-1].append(k%10)
    tot+=k


r2=[]
x=r[1]
ds = [b-a for a,b in zip(x,x[1:])]
#print(ds)
print("a")
print(len(ds))
print(len(x))
for x in r:
    r2.append({})
    ds = [b-a for a,b in zip(x,x[1:])]
    for a,b,c,d,k in reversed(list(zip(*[x for x in [ds,ds[1:-2],ds[2:-1],ds[3:],x[1+3:]]]) ) ):
        #if (a,b,c,d) == (-2,1,-1,3):
            #print(k)
        r2[-1][a,b,c,d] = k
r=None
print("b")
mx=0
i=0
for a,b,c,e in itertools.product(*(range(-9,10) for i in range(4))):
    i+=1
    mz = sum(d[a,b,c,e] if (a,b,c,e) in d else 0 for d in r2)
    if i%10000==0:
        print(i)
    if mx<mz:
        r=a,b,c,e
        mx=max(mz,mx)
#print([d[-2,1,-1,3] for d in r2])

#print(r,mx)



print(mx)


























