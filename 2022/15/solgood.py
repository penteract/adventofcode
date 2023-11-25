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

s=set()
yy=2000000
#yy=111810
if len(f)<20:
    yy=10

r = []


sqs = []
es1 = []
es2 = []
for (line,ints) in zip(f,xss):
    #print(line,ints,yy)
    if line:
        sx,sy,bx,by = ints
        dd = abs(sx-bx)+abs(sy-by)
        sqs.append(((sx,sy),dd))
        es1.append((sy-(sx+dd))*2-1)
        es1.append((sy-(sx-dd))*2+1)
        es2.append((sy+(sx+dd))*2+1)
        es2.append((sy+(sx-dd))*2-1)

es1.sort()
es2.sort()
e2 = [y+k for y,z in zip(es2,es2[1:]) for k in [1,3] if y+k<z and y+7>z]
e1 = [y+k for y,z in zip(es1,es1[1:]) for k in [1,3] if y+k<z and y+7>z]
for y1 in e1:
    for y2 in e2:
        py = (y1+y2)//4
        px = (y2-y1)//4
        if 0<py<2*yy and 0<px<2*yy:
            for cen,d in sqs:
                if abs(cen[0]-px)+abs(cen[1]-py) <=d:
                    break
            else:
                print(px*4000000+py)
            

#|#|#|#|#|#|#|#
#|#|#|/|#|#|#|#
#|#|/| | |#|#|#
#|/| | | | |#|#
#|#| | | |#|#|#
#|#|#| |#|#|#|#
            

