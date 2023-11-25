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
    xss = lmap(lambda x:lmap(int,x),f)
except Exception:
    pass


print(xss[0])
s=0
vis = [[False for x in r] for r in xss]
h=len(xss)
w=len(xss[0])

for i in range(h):
    mx=-1
    for j in range(w):
        if xss[i][j]>mx:
            vis[i][j]=True
            mx=xss[i][j]
            
    mx=-1
    for j in reversed(range(w)):
        if xss[i][j]>mx:
            vis[i][j]=True
            mx=xss[i][j]


for j in range(w):
    mx=-1
    for i in range(h):
        if xss[i][j]>mx:
            vis[i][j]=True
            mx=xss[i][j]
            
    mx=-1
    for i in reversed(range(h)):
        if xss[i][j]>mx:
            vis[i][j]=True
            mx=xss[i][j]
print(sum(map(sum,vis)))
