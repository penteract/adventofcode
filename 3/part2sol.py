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

try:
    xs = lmap(int,f)
except Exception:
    pass
try:
    xss = lmap(ints,f)
except Exception:
    pass

d=defaultdict(list)

tot=0

l=[]
s=set()
for y,line in enumerate(f):
    k=False
    r=0
    for x,c in enumerate(line):
        p=Pt((x,y))
        d[x,y]=c
        
        if c in "1234567890":
            if not k:
                r=0
                l.append([])
                k=True
            l[-1].append(p)
            r=r*10+int(c)
        else:
            if k:
                l[-1]=(l[-1],r)
            k=False
            r=0
        if c in "*":
            s.add(p)
    
    if k:
        l[-1]=(l[-1],r)
        k=False

d={k:set() for k in s}

print(l[-1])
for i,(x,n) in enumerate(l):
    for p in x:
        for dr in ddirs:
            if (p+dr) in d:
                d[p+dr].add(i)
for k in d:
    if len(d[k])==2:
        i=1
        for j in d[k]:
            i*=l[j][1]
        tot+=i

print(tot)
