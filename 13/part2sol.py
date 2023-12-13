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

fgroups = ftext.strip().split("\n\n")
if len(fgroups)>1:
    fgs = [g.split("\n") for g in fgroups]
    fgns = [lmap(ints,g) for g in fgs]

try: xs = lmap(int,f)
except Exception: pass
try: xss = lmap(ints,f)
except Exception: pass


d=defaultdict(int)
tot=0

print(lmap(ints_locs,f),fgs)

for g in fgs:
    hors = [0]*(len(g)-1)
    vers = [0]*(len(g[0])-1)
    for y,line in enumerate(g):
        for x,c in enumerate(line):
            d[(x,y)]=c
            for i in range((y+1)//2):
                #refl through line after (y-1-i)
                if d[(x,y-i*2-1)]!=c:
                    hors[(y-1-i)] += 1
            for j in range((x+1)//2):
                #refl through line after (x-1-i)
                print((x,y),j,x-1-j,(x-j*2-1,y))
                if d[(x-j*2-1,y)]!=c:
                    print(x,y,j)
                    vers[(x-1-j)] += 1
                    if (x-1-j)==4:
                        print("*")
    print(hors,vers)
    hors = [x==1 for x in hors]
    vers = [x==1 for x in vers]
    assert sum(hors+vers)==1,(hors,vers)
    for i,x in enumerate(hors):
        if x:
            tot+=100*(i+1)
    for i,x in enumerate(vers):
        if x:
            tot+=(1+i)
print(tot)
