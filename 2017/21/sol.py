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


def rot(s):
    #print(s)
    l=len(s)
    return tuple( tuple(s[j][l-1-i] for j in range((l)))
        for i in range((l)))

d={}
for line in f:
    a,b=line.split("=>")
    rs = a.strip().split("/")
    bb = b.strip().split("/")
    for i in range(2):
        for k in range(4):
            rs = rot(rs)
            d[sum(rs,start=())]=bb
        rs = list(reversed(rs))
print(d)
#import numpy as np
g = """.#.
..#
###""".split("\n")


for i in range(18):
    ng=[]
    if len(g)%2==0:
        for a,b in zip(g[::2],g[1::2]):
            nrs = [[],[],[]]
            #print(a,b)
            for tup in zip(a[::2],a[1::2],b[::2],b[1::2]):
                #print(tup)
                for x,y in zip(nrs,d[tup]):
                    x.append(y)
            for x in nrs:
                ng.append("".join(x))
    else:
        assert len(g)%3==0
        for a,b,c in zip(g[::3],g[1::3],g[2::3]):
            nrs = [[],[],[],[]]
            #print(a,b)
            for tup in zip(a[::3],a[1::3],a[2::3],b[::3],b[1::3],b[2::3],c[::3],c[1::3],c[2::3]):
                #print(tup)
                for x,y in zip(nrs,d[tup]):
                    x.append(y)
            for x in nrs:
                ng.append("".join(x))
    g=ng

for line in g:
    print(line)
