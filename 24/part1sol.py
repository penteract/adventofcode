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
for y,line in enumerate(f):
    for x,c in enumerate(line):
        d[x,y]=c

testmn=7
testmx=27

if fname=="input":
    testmn=200000000000000
    testmx=400000000000000

l=[]
for a,b,c,d,e,f in xss:
    l.append((pt(a,b,c),pt(d,e,f)))
import fractions
def yi(p,v):
    t = -p[0]/v[0]
    m = v[1]/v[0]
    zm = v[2]/v[0]
    return p+t*v,m,zm
tot=0
e=10**-7
for i,(pa,va) in enumerate(l):
    for (pb,vb) in l[:i]:
        print(pa,va,pb,vb)
        ya,ma,mza=yi(pa,va)
        yb,mb,mzb=yi(pb,vb)
        print(ya,yb)
        if mb-ma==0:
            continue
        xc = (ya[1]-yb[1])/(mb-ma)
        yc = ma*xc+ya[1]
        print(xc,yc)
        zc = mza*xc+ya[2]
        zcb = mzb*xc+yb[2]
        if testmn-e<=yc<=testmx+e:
            print("y in range")
            #if zc-e<=zcb<=zc+e:
            if testmn-e<=xc<=testmx+e:
                print("x in range")
                if (pa[0]-xc)*va[0]<e and (pb[0]-xc)*vb[0]<e:
                    tot+=1
        else:
            print(yc,"y not in range",testmn-e<=yc<=testmx+e,testmn-e,testmx+e)
        
#print(lmap(ints_locs,f))

print(tot)
