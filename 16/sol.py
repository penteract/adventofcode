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

fgroups = ftext.split("\n\n")
if len(fgroups)>1:
    fgs = [g.split("\n") for g in fgroups]
    fgns = [lmap(ints,g) for g in fgs]

try: xs = lmap(int,f)
except Exception: pass
try: xss = lmap(ints,f)
except Exception: pass


d=defaultdict(int)
tot=0

print(lmap(ints_locs,f))

for y,line in enumerate(f):
    for x,c in enumerate(line):
        d[x,y]=c

def count(pos,dr):
    beams = [(pos,dr)]
    seen = set()
    s2=set()
    for pos,dr in beams:
        if (pos,dr)not in seen:
            seen.add((pos,dr))
            pos+=dr
            if pos in d:
                s2.add(pos)
                c=d[pos]
                if c=="/":
                    beams.append((pos,(-dr[1],-dr[0])))
                elif c=="\\" :
                    beams.append((pos,(dr[1],dr[0])))
                elif c=="-":
                    if dr[0]==0:
                        beams.append((pos,dirs["L"]))
                        beams.append((pos,dirs["R"]))
                    else:
                        beams.append((pos,dr))
                elif c=="|":
                    if dr[1]==0:
                        beams.append((pos,dirs["U"]))
                        beams.append((pos,dirs["D"]))
                    else:
                        beams.append((pos,dr))
                elif c==".":
                    beams.append((pos,dr))
                else:
                    assert False,c
    return (len(s2))
l=[]
print(len(f),len(f[0]))
for i in range(len(f)):
    l.append((Pt((-1,i)),dirs["R"]))
    l.append((Pt((len(f[0]),i)),dirs["L"]))
    l.append((Pt((i,-1)),dirs["D"]))
    l.append((Pt((i,len(f))),dirs["U"]))
print(max([count(p,dd) for p,dd in l]))
