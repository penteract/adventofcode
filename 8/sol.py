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
    ex = r'[0-9A-Z]+'
    return list(re.findall(ex, x))

def ints_locs(x: str) -> list[int]:
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
print(f)
fgroups = ftext.split("\n\n")

try: xs = lmap(int,f)
except Exception: pass
try: xss = lmap(ints,f)
except Exception: pass


d=defaultdict(int)
tot=0

#print(lmap(ints_locs,f))
print(f[0])

print(xss)
d={}
for a,b,c in xss[2:]:
    d[a]=(b,c)
n="AAA"
ns = [x for x in d if x[-1]=="A"]

l1 = len(f[0])
def path(n):
    s=set()
    pth=[]
    while True:
        for i,c in enumerate(f[0]):
            pth.append((i,n))
            if (i,n) in s:
                break
            s.add((i,n))
            n = d[n]["LR".find(c)]
        else:
            continue
        break
    return pth
print(len(path(ns[0])))
l = [path(x) for x in ns]
import math
lps = [len(k) - k.index(k[-1])-1  for k in l]
print(math.lcm(*lps)-1)
zps = [k.index(v[0])  for k,v in zip(l,[[x for x in k if x[1][-1]=="Z"] for k in l])]
