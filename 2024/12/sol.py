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


d=defaultdict(int)
for y,line in enumerate(flns):    
    for x,c in enumerate(line):
        d[x,y]=c
tot=0

seen = set()
l = list(d)
regs = []
for p in l:
    ar = 1
    pm = 0
    c = d[p]
    if p not in seen:
        nx = [p]
        seen.add(Pt(p))
        regs.append(set())
        while nx:
            pt = nx.pop()
            for dr in ods:
                if d[pt+dr]!=c:
                    regs[-1].add((dr,pt))
                    pm+=1
                    continue
                elif pt+dr in seen:
                    continue
                nx.append(pt+dr)
                seen.add(pt+dr)
                ar+=1
                #regs[-1].add(pt+dr)
        print(ar,pm)
        tot+=ar*pm
        regs[-1] = (ar,regs[-1])


print(tot)
tot=0
#flood fill each edge
for ar,es in regs:
    #pt = list(es)[0]
    #c = d[pt]
    seen = set()
    ec = 0
    for k in list(es):
        print("k")
        if k not in seen:
            print("k not seen")
            ec+=1
            nx = [k]
            seen.add(k)
            while nx:
                print("nx")
                #print("nx",len(seen),len(nx))
                dd,b = nx.pop()
                for dr in [dd.left(),dd.right()]:
                    if (dd, b+dr) in es:
                        if (dd,b+dr) not in seen:
                            seen.add((dd,b+dr))
                            nx.append((dd,b+dr))
    print(ar,ec)
    tot+=ar*ec
print(tot)



























