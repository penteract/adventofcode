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

try:
    xs = ints(f)
except Exception:
    pass
try:
    xss = lmap(ints_in,f)
except Exception:
    pass
dirs = {
    "R":(0,1),
    "U":(1,0),
    "L":(0,-1),
    "D":(-1,0)
    }
seen=set()

xs = [[0,0] for i in range(10)] # xs[0] is head, xs[9] is last tail
h=xs[0]
t=xs[9]
for line in f:
    d=dirs[line[0]]
    n=int(line[2:])
    for i in range(n):
        xs[0][0]+=d[0]
        xs[0][1]+=d[1]
        for j in range(9):
            h=xs[j]
            t=xs[j+1]
            if abs(t[0]-h[0])>=2:
                t[0]+=(h[0]-t[0])//2
                if abs(t[1]-h[1])>=1:
                    t[1]+=(h[1]-t[1])//abs(h[1]-t[1])
            elif abs(t[1]-h[1])>=2:
                t[1]+=(h[1]-t[1])//2
                if abs(t[0]-h[0])>=1:
                    t[0]+=(h[0]-t[0])//abs(h[0]-t[0])
        seen.add(tuple(xs[9]))
print(len(seen))
