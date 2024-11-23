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
    "R":Pt((0,1)),
    "U":Pt((-1,0)),
    "L":Pt((0,-1)),
    "D":Pt((1,0))
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


# nsew = 1234
ddd={c[0]:[dirs[x] for x in c[1:]] for c in ["|UD","-RL","LUR","JUL","7DL","FDR"]}
guide = defaultdict(list)
for c in ddd:
    guide[c]=ddd[c]
print(guide)
m = defaultdict(list)

r=None
for y,line in enumerate(f):
    for x,c in enumerate(line):
        m[Pt((y,x))]=guide[c]
        if c=="S":
            r=Pt((y,x))
s=r
loop=[s]
for dd in ods:
    print(s)
    if len(m[s+dd])>0 and ((0,0)-dd) in m[s+dd]:
        nx=s+dd
        ld=(0,0)-dd
        break
while nx!=s:
    loop.append(nx)
    print(nx,ld,m[nx]) #[x for x in m[nx] if x!=ld])
    [ld] = [x for x in m[nx] if x!=ld]
    nx=nx+ld
    ld=(0,0)-ld
            

print(len(loop)//2)
