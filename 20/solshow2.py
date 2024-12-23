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


from heapq import *

dists = {}
path = []
def ast(start,neighbs,done,h = lambda x:0):
    """Finds the node n such that done(n) with minimal distance from an element of start.
    neighbs(n) = [(nn,edgeweight)]
    assumes h(n)<d(n,end)
    Returns the path as a lisp-style deeply nested tuple"""
    seen=set()
    hq = []
    for x in start:
        heappush(hq,(h(x),(x,None),0))
    while hq:
        c,pth,d = heappop(hq)
        n=pth[0]
        dists[n] = d
        if n not in seen:
            #print(n)
            seen.add(n)
            if mp[n]!="#":
                path.append(n)
            if done(n):
                return (pth,d)
            for x,dst in neighbs(n):
                if x not in seen:
                    heappush(hq,(d+dst+h(x),(x,pth),d+dst))

for y,line in enumerate(flns):
    for x,c in enumerate(line):
        d[x,y]=c
        if c=="S":
            start = x,y
        if c=="E":
            end = (x,y)

mp=d
l = [x for x in d if d[x] in list(".SE")]

def neighbs(p):
    if d[p] in list(".SE"):
        for dr in ods:
            yield (p+dr,1)

#ast([end],neighbs,done = lambda x:False)
#dEnd=dists
#dists={}
ast([start],neighbs,done = lambda x:False)
#dStart=dists
#print (dists)
#ds = dEnd[start]
#print(dists[start])

mnchk= 100 # minimum time save
chsz = 20 # cheat size

sz = (len(flns)-1 )*2+1
#print([(x,dists[x]) for x in path])
#raise Exception()
result = 0
for i,k1 in enumerate(path):
    for j,k2 in enumerate(path):
        ds = abs(k1[0]-k2[0])+abs(k1[1]-k2[1])
        print(  chr((ds*128)//sz),end=""  )
    print("\x00\x00")
#print(result)
















