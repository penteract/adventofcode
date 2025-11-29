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
d=defaultdict(int)

for y,line in enumerate(flns):    
    for x,c in enumerate(line):
        d[Pt((x,y))]=c
        if c=="S":
            st = Pt((x,y))
        if c=="E":
            ed = Pt((x,y))

from heapq import *
#from collections import frozenset

def ast(start,neighbs,done,h = lambda x:0):
    """Finds the node n such that done(n) with minimal distance from an element of start.
    neighbs(n) = [(nn,edgeweight)]
    assumes h(n)<d(n,end)
    Returns the path as a lisp-style deeply nested tuple"""
    seen={}
    #pths = {x:{x[0]}}
    pths = {None:set()}
    hq = []
    for x in start:
        heappush(hq,(h(x),(x,None),0))
    while hq:
        c,(n,prv),d = heappop(hq)
        #n=pth[0]
        if n not in seen or seen[n]>=d:
            if n not in seen or seen[n]>d:
                pths[n] = pths[prv].union([n])
            else:
                pths[n]=pths[n].union(pths[prv])
            #print(n)
            seen[n] = d
            if done(n):
                yield (pths[n],d)
            for x,dst in neighbs(n):
                heappush(hq,(d+dst+h(x),(x,n),d+dst))

def prgrid(d):
    xs = set(k[0] for k in d)
    ys = set(k[1] for k in d)
    for y in range(min(ys),max(ys)+1):
        for x in range(min(xs),max(xs)+1):
            k=x,y
            print(d[k] if d[k]!=0 else ".",end="")
        print()

start = [(st,dirs["R"])]
done = lambda x:x[0] == ed
mp = d
def neighbs(ps):
    pt,d = ps
    if mp[pt+d]!="#": yield ((pt+d,d),1)
    yield ((pt,d.left()),1000)
    yield ((pt,d.right()),1000)
d=None

def flatten(tup):
    l=[]
    while tup is not None:
        l.append(tup[0])
        tup=tup[1]
    return l
sn={st,ed}
for p,dd in ast(start,neighbs,done):
    #print(p,dd)
    print(dd)
    for a,b in p:
        sn.add(a)
    break
    if d is None:
        d=dd
    elif d!=dd:
        break
    for k in flatten(p):
        sn.add(k[0])
for x in sn:
    #print(x)
    mp[x]="X"
prgrid(mp)

print(len(sn))






























