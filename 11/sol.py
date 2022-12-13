import re
from typing import Tuple, Callable, Iterable, Optional
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"
f=[line.strip() for line in open(fname)]

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

s=0
monkeys = []
ns = iter(zip(f,xss))
for (line,ints) in ns:
    assert ints[0]==len(monkeys)
    line,ints=next(ns)
    mk=[ints,"",-1,-1,-1,0]
    line,ints=next(ns)
    mk[1]=eval("lambda old:"+line.split("=")[1])
    line,ints=next(ns)
    mk[2]=ints[0]
    line,ints=next(ns)
    mk[3]=ints[0]
    line,ints=next(ns)
    mk[4]=ints[0]
    monkeys.append(mk)
    try:
        line,ints=next(ns)
    except Exception:
        break
mcounts = [0 for m in monkeys]
p=1
for m in monkeys:
    p*=m[2]
print(p)
for i in range(10000):
    for m in monkeys:
        while m[0]:
            m[5]+=1
            x = m[1](m[0].pop())%p
            monkeys[m[4-(x%m[2]==0)]][0].append(x)

s=sorted([m[5] for m in monkeys])

print(s[-1]*s[-2])








