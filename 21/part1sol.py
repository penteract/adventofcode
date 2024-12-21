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
dd={}
for y,line in enumerate(s1.split("\n")):
    for x,c in enumerate(line):
        d[c]=x,y
        dd[x,y]=c
d2={}
dd2={}
for y,line in enumerate(s2.split("\n")):
    for x,c in enumerate(line):
        d2[c]=x,y
        dd2[x,y]=c

def mkN(c,prevc="A"):
    pos = d[prevc]
    s=""
    p2 = d[c]
    if dd[pos[0],p2[1]]==" " or dd[p2[0],pos[1]]==" " or pos[0]==p2[0] or pos[1]==p2[1]:
        if p2[1]<pos[1]:
            s+=("^"*abs(pos[1]-p2[1]))
            s+=(">" if p2[0]>pos[0] else "<")*abs(p2[0]-pos[0])
        else:
            s+=(">" if p2[0]>pos[0] else "<")*abs(p2[0]-pos[0])
            s+=("v"*abs(p2[1]-pos[1]))
        s+="A"
        yield s
    else:
        for x in mkNd(Pt(pos) - p2):
            yield x
        #yield (("^" if p2[1]<pos[1] else "v") *abs(pos[1]-p2[1])) + (">" if p2[0]>pos[0] else "<")*abs(p2[0]-pos[0])
        #yield (">" if p2[0]>pos[0] else "<")*abs(p2[0]-pos[0]) + (("^" if p2[1]<pos[1] else "v") *abs(pos[1]-p2[1]))
    #pos=p2
    #print(s)
    #return s
def mkNd(pos,p2=(0,0)):
    l= [(("^" if p2[1]<pos[1] else "v") *abs(pos[1]-p2[1])) + (">" if p2[0]>pos[0] else "<")*abs(p2[0]-pos[0])]
    l.append((">" if p2[0]>pos[0] else "<")*abs(p2[0]-pos[0]) + (("^" if p2[1]<pos[1] else "v") *abs(pos[1]-p2[1])))
    return [x+"A" for x in l]

def mkAr1(l):
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
    #print(s)
    return s

@functools.cache
def bestR(c,pc):
    l = [mkAr1(s) for s in mkAr(c,pc)]
    return min((len(x),x) for x in l)[1]

def arFull(l):
    s=""
    for pc,c in zip("A"+l,l):
        s+=bestR(c,pc)
    #print("full",s)
    return s


def mkAr(c,prevc="A"):
    d=d2
    pos = d[prevc]
    s=""
    p2 = d[c]
    if dd2[pos[0],p2[1]]==" " or dd2[p2[0],pos[1]]==" " or pos[0]==p2[0] or pos[1]==p2[1]:
        if p2[1]<pos[1]:
            s+=(">" if p2[0]>pos[0] else "<")*abs(p2[0]-pos[0])
            s+=("^"*abs(pos[1]-p2[1]))
        else:
            s+=("v"*abs(p2[1]-pos[1]))
            s+=(">" if p2[0]>pos[0] else "<")*abs(p2[0]-pos[0])
        s+="A"
        yield s
    else:
        for x in mkNd(Pt(pos) - p2):
            yield x


def mkArFull(l):
    n=0
    for pc,c in zip("A"+l,l):
        n+=len(bestR(pc,c))
    return n

for xs,l in zip(xss,flns):
    n=0
    ss=""
    ss1=""
    for pc,c in zip("A"+l,l):
        nn,s,s1 = min((len(arFull(s)),arFull(s),s) for s in mkN(c,pc))
        n+=nn
        ss+=s
        ss1+=s1
    print(ss1)
    print(ss)
        #n+=min(len(arFull(s)) for s in mkN(c,pc))
    #l = len(mkAr(mkAr(mkN(l))))
    #print(l)
    tot+=n*xs[0]


print(tot)






























