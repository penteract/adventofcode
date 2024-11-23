import re
from typing import Tuple, Callable, Iterable, Optional
import sys
from functools import cache
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

#print(lmap(ints_locs,f))

print("hello")

@cache
def tst(s,args,start=False):
    #print(s,args)
    #if k is not None:
        #print(s,args)
    if len(s)==0:
        return 1 if len(args)==0 or args==(0,) else 0
    if s[0]=="." and start==False:
        return tst(s[1:],args)
    elif s[0]==".":
        if args[-1]==0:
            r=tst(s[1:],args[:-1])
            return r
        else:
            return 0
    if s[0]=="#":
        if len(args)==0:
            return 0
        ags = args[:-1] + (args[-1]-1,)
        #args[-1]-=1
        r=tst(s[1:],ags,start=True)
        #args[-1]+=1
        return r
    if s[0]=="?":
        return tst("."+s[1:],args,start) + tst("#"+s[1:],args,start)
        

for l in f:
    x,ns = l.split()
    ns = ints(ns)
    tot+=tst(((x+"?")*5)[:-1],tuple(reversed(ns))*5)
    print(x,ns,tot)
    

print(max([l.count("?") for l in open("input")]))
print(tot)
