import re
from typing import Tuple, Callable, Iterable, Optional
import sys
##from utils.interval import I
##
##def ri(r1,r2):
##    """Given 2 cuboids described as tuples of intervals, find their intersection"""
##    return tuple((a&b) for a,b in zip(r1,r2))

fname=sys.argv[1] if len(sys.argv)>1 else "input"
if fname!="input":
    steps=int(open(fname).read())
    fname="input1"
else:
    steps=26501365
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
#print(f)
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
        if c=="S":
            start=Pt((x,y))
            d[x,y]="."
#print(f)
maxx = len(f[0])
maxy=len(f)
mp=dict(d)
#from collections import frozenset as f

from functools import cache

def countPerStep(starts):
    l=set(starts)
    r={0:len(l)}
    for i in range(maxx*2):
        ll=stp(l)
        r[i+1]=len(ll)
        l=ll
    return r

def stp(l):
    #print("stp")
    ll=set()
    for x in l:
        for dr in ods:
            #print(x,dr)
            if d[x+dr]==".":
                ll.add(x+dr)
    return ll


csDiags = {}
for x in (0,start[0],maxx-1):
    for y in (0,start[1],maxy-1):
        p=(x,y)
        print(p)
        csDiags[p]=countPerStep([p])
