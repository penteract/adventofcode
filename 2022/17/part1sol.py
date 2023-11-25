import re
from typing import Tuple, Callable, Iterable, Optional
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"
f = open(fname)
ftext=f.read()
f=[line.strip() for line in ftext.split("\n")[:-1]]

from collections import defaultdict

d=defaultdict(int)

#copied from https://github.com/joefarebrother/adventofcode/blob/master/misc_utils.py
def lmap(f: Callable, *xs) -> list:
    """Like map but returns a list"""
    return list(map(f, *xs))

def ints(xs: Iterable) -> list[int]:
    """Casts each element of xs to an int"""
    return lmap(int, xs)

def mint(x, default=None):
    """Maybe int - casts to int and returns default on failure"""
    try:
        return int(x)
    except ValueError:
        return default

def ints_in(x: str) -> list[int]:
    """Finds and parses all integers in the string x"""
    ex = r'(?:(?<!\d)-)?\d+'
    return ints(re.findall(ex, x))


class Pt(tuple):
    def __add__(self,other):
        return Pt([x+y for x,y in zip(self,other)])
    def __sub__(self,other):
        return Pt([x-y for x,y in zip(self,other)])
    def __rsub__(self,other):
        return Pt([y-x for x,y in zip(self,other)])
    def __radd__(self,other):
        return Pt([y+x for x,y in zip(self,other)])
    def __rmul__(self,other):
        return Pt([other*x for x in self])
dirs = {
    "R":Pt((0,1)),
    "U":Pt((1,0)),
    "L":Pt((0,-1)),
    "D":Pt((-1,0))
    }
ods = list(dirs.values())

#odirs = [(0,1),(1,0),(0,-1),(-1,0)]
ddirs = lmap(Pt,[(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)])

try:
    xs = ints(f)
except Exception:
    pass
try:
    xss = lmap(ints_in,f)
except Exception:
    pass



ps = """####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##"""
ps = [x.split("\n") for x in ps.split("\n\n")]
pss = []
for k in ps:
    p = set()
    for i,row in enumerate(k):
        for j,c in enumerate(row):
            if c=="#":
                p.add(Pt((j,len(k)-1-i)))
    mxx = max(x[0] for x in p)
    pss.append((p,mxx))


h = 0
for i in range(7):
    d[(i,0)] = 1

from itertools import cycle

def canmove(p,dr):
    for c in p:
        if c+dr in d or not 0<=(c+dr)[0]<7:
            break
    else:
        return True
    return False
    

ps = cycle(pss)
dirs = cycle(f[0])
for i in range(2022):
    p,mx = next(ps)
    ll = Pt((2,h+4))
    while True:
        c = next(dirs)
        if c=="<":
            if canmove(p,ll+(-1,0)):
                ll+=(-1,0)
        elif c==">":
            if canmove(p,ll+(1,0)):
                ll+=(1,0)
        if canmove(p,ll+(0,-1)):
            ll+=(0,-1)
        else:
            for c in p:
                d[c+ll]=1
                h=max(h,(c+ll)[1])
            break


s=0
for (line,ints) in zip(f,xss):
    pass
print(h)











