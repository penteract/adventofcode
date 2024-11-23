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

lastC = [-1]*len(f[0])
for y,line in enumerate(f):
    for x,c in enumerate(line):
        d[x,y]=c
        if c=="#":
            lastC[x]=y
        elif c=="O":
            lastC[x]+=1
            tot+=len(f)-lastC[x]
print(tot)
l=len(f)
assert len(f)==len(f[0])
#north, then west, then south, then east

def tilt(g,dr):
    ng = defaultdict(int)
    sdr = dr[0]+dr[1]
    Cs=[-1]*l if (dr[0]+dr[1]==-1) else [l]*l
    
    for i in range(l):
        for j in range(l) if (dr[0]+dr[1]==-1) else range(l-1,-1,-1):
            pos = i*(dr[0]==0) + j*(dr[0]!=0) , i*(dr[1]==0)+j*(dr[1]!=0)
            if g[pos]=="#":
                Cs[i]=j
                ng[pos]="#"
            elif g[pos]=="O":
                Cs[i]-=sdr
                ng[i*(dr[0]==0) + Cs[i]*(dr[0]!=0) , i*(dr[1]==0)+Cs[i]*(dr[1]!=0)] = "O"
            #g[(i*dr[0]+j*abs(dr[1]),)]
    return ng

n=0
def prgrid(d):
    for i in range(l):
        for j in range(l):
            k=j,i
            print(d[k] if d[k]!=0 else ".",end="")
        print()

d2 = {k:v for k,v in d.items()}
s = {}
while True:
    if str(d) in s:
        r = n-s[str(d)]
        break
    else:
        s[str(d)]=n
    n+=1
    for c in "ULDR":
        d=tilt(d, dirs[c])
print(n,r)
##    for k in d:
##        if d2[k]!=d[k]:
##            break
##    else:
##        break
#cl = m-n
for i in range((1000000000 - n)%r):
    for c in "ULDR":
        d=tilt(d, dirs[c])
#prgrid(d)
tot=0
for i,j in d:
    if d[i,j]=="O":
        tot+=l-j
print(tot)
