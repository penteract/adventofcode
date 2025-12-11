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

def bfs(neighbs,init,end):
    frontier=[(init,0)]
    seen=set(frontier)
    i=0
    if init==end:
        return 0
    while i<len(frontier):
        x,a=frontier[i]
        for k in neighbs(x):
            if k not in seen:
                frontier.append((k,a+1))
                #print(k,a,end)
                if k==end:
                    return a+1
                seen.add(k)
        i+=1
import random
from heapq import *
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
        if random.random()<0.000005:
            print(c,n,d)
        if n not in seen:
            #print(n)
            seen.add(n)
            if done(n):
                return (pth,d)
            for x in neighbs(n):
                dst=1#h(x)
                if x not in seen:
                    heappush(hq,(d+dst+h(x),(x,pth),d+dst))
def flatten(tup):
    l=[]
    while tup is not None:
        l.append(tup[0])
        tup=tup[1]
    return l

import z3
l=[]
#Configuring the first machine's counters requires a minimum of 10 button presses. One way to do this is by pressing (3) once, (1,3) three times, (2,3) three times, (0,2) once, and (0,1) twice.

xs = [z3.Int("x"+str(i)) for i in range(20)]
ys = [z3.Int("y"+str(i)) for i in range(20)]
for y,line in enumerate(flns):
    print(tot,line)
    stuff = line.split()
    #pat = tuple([c=="#" for c in stuff[0][1:-1]])
    bs = lmap(ints, stuff[1:-1])
    o = z3.Optimize()
    jolts = ints(stuff[-1])
    
    for i,j in enumerate(jolts):
        o.add( sum(xs[k] for k,b in enumerate(bs) if i in b) == j)
        
        #o.add(sum( [x[i] for i in b] = )
    for x in xs:
        o.add(x>=0)
    ooa = o.minimize(sum(xs[i] for i in range(len(bs))))
    print(o.check())
    print(ooa.value())
    tot+=int(str(ooa.value()))
    #pat=pt(tuple(jolts))
    #init = pt(tuple(0 for c in pat))
    #bs = [pt(1 if i in b else 0 for i in range(len(pat))) for b in bs]
    #l.append((pat,bs))
   

#print(max(len(a[0]) for a in l) )
#print(max(len(a[1]) for a in l) )
print(tot)






























