import re
from typing import Tuple, Callable, Iterable, Optional
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"
f = open(fname)
ftext=f.read()
flns=[line.strip() for line in ftext.split("\n")[:-1]]
f=flns

fgroups = ftext.split("\n\n")
if len(fgroups)>1:
    f=fgroups

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
for y,line in enumerate(f):
    for x,c in enumerate(line):
        if c=="#":
            s.add((x,y))


ds = list("LRDU")

for i in range(100000000):
    xs = [x for x,y in s]
    ys = [y for x,y in s]
    """print(len(s),min(xs),min(ys))
    for y in range(min(ys),max(ys)+1):
        for x in range(min(xs),max(xs)+1):
            print(("#" if (x,y) in s else "."),end="")
        print()
    print()"""
    d=defaultdict(list)
    flag=True
    for e in s:
        if not any(e+c in s for c in ddirs):
            d[e].append(e)
            continue
        flag=False
        for cc in ds:
            c=dirs[cc]
            for k in [c,c+c.left(),c+c.right()]:
                if e+k in s:
                    break
            else:
                #if e[1]==0:
                    #print("***",e,c)
                d[e+c].append(e)
                break
        else:
            d[e].append(e)
    ns=set()
    if flag:
        print(i+1)
        break
    for k in d:
        if len(d[k])==1:
            ns.add(k)
        else:
            for e in d[k]:
                ns.add(e)
    ds = ds[1:]+ds[:1]
    s=ns

xs = [x for x,y in s]
ys = [y for x,y in s]

#print((max(xs)-min(xs)+1)*(max(ys)-min(ys)+1)-len(s) )









