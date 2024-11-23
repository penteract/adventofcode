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

def mapn(f,xs,n): # map a depth n nested list
    if n==0:
        return f(xs)
    else:
        k=n-1
        return lmap(lambda x:mapn(f,x,k), xs)
def splitby(txt,*splits):
    result = txt
    for i,c in enumerate(splits):
        result = mapn(lambda x:x.split(c),result, i)
    return result

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
    f=[g.strip().split("\n") for g in fgroups]

try:
    xs = lmap(int,f)
except Exception:
    pass
try:
    xss = lmap(ints,f)
except Exception:
    pass

d=defaultdict(int)

tot=0

seeds = ints(f[0][0])
seeds = list(zip(seeds[::2],seeds[1::2]))
seeds = [(a,a+b) for a,b in seeds]
print(seeds)
f=f[1:]
maps=[]
for g in f:
    maps.append([])
    print(g[1:])
    for ds,ss,rl in map(ints,g[1:]):
        maps[-1].append([ss,ss+rl,ds])
    #x.split("-to-")
    #print(x)
def get(sd,mp):
    left = [sd]
    res = []
    for a,b,ds in mp:
        nl = []
        for (x,e) in left:
            if a<=x<b:
                if e>b:
                    nl.append((b,e))
                    res.append((ds+(x-a),ds+(b-a)))
                else:
                    res.append((ds+(x-a),ds+(e-a)))
            elif x<=a<e:
                nl.append((x,a))
                if e>b:
                    res.append((ds,ds+(b-a)))
                    nl.append((b,e))
                else:
                    res.append((ds,ds+(e-a)))
            else:
                nl.append((x,e))
        left=nl
    return res+left
r = []
for mp in maps:
    seeds=[x for s in seeds for x in get(s,mp)]
    print(seeds)
#print(sorted(seeds)[:10])
print(min(x[0] for x in seeds))
#print(f,xss)
