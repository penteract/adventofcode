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

s1 = """789
456
123
 0A"""

s2 = """ ^A
<v>"""

d={}
for y,line in enumerate(s1.split("\n")):
    for x,c in enumerate(line):
        d[c]=x,y
d2={}
for y,line in enumerate(s2.split("\n")):
    for x,c in enumerate(line):
        d2[c]=x,y

def mkN(l):
    pos = d["A"]
    s=""
    for c in l:
        p2 = d[c]
        if p2[1]<pos[1]:
            s+=("^"*abs(pos[1]-p2[1]))
            s+=(">" if p2[0]>pos[0] else "<")*abs(p2[0]-pos[0])
        else:
            s+=(">" if p2[0]>pos[0] else "<")*abs(p2[0]-pos[0])
            s+=("v"*abs(p2[1]-pos[1]))
        s+="A"
        pos=p2
    print(s)
    return s
def mkAr(l):
    pos = d2["A"]
    s=""
    for c in l:
        p2 = d2[c]
        if p2[1]>pos[1]:
            s+=(">" if p2[0]>pos[0] else "<")*abs(p2[0]-pos[0])
            s+=("^"*abs(pos[1]-p2[1]))
        else:
            s+=("v"*abs(p2[1]-pos[1]))
            s+=(">" if p2[0]>pos[0] else "<")*abs(p2[0]-pos[0])
        pos=p2
        s+="A"
    print(s)
    return s

    return s

for xs,l in zip(xss,flns):
    l = len(mkAr(mkAr(mkN(l))))
    print(l)
    tot+=l*xs[0]


print(tot)






























