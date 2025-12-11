import re
from typing import Tuple, Callable, Iterable, Optional
import sys
import math,functools,itertools
fname=sys.argv[1] if len(sys.argv)>1 else "input"
f = open(fname)
#copied from https://github.com/joefarebrother/adventofcode/blob/master/misc_utils.py
def lmap(f: Callable, *xs) -> list:
    return list(map(f, *xs))
def mint(x, default=None):
    try: return int(x)
    except ValueError: return default
def ints(x: str) -> list[int]:
    ex = r'(?:(?<!\d)-)?\d+'
    return lmap(int,re.findall(ex, x))

s="<svg viewpo> "
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
def ptbound(bounds,p):
    """bounds is a list of 2 points giving the min and max"""
    if len(bounds)==0:
        for x in p:
            bounds.append(x)
    bounds[0] = pt(min(bounds[0][i],p[i]) for i in range(len(p)))
    bounds[1] = pt(max(bounds[1][i],p[i]) for i in range(len(p)))
bnds=[ints(next(f))]*2
s=f"M {','.join(str(x) for x in bnds[0])}"
p=bnds[0]
rs=f'<rect x="{p[0]}" y="{p[1]}" width="1" height="1" fill="red" /> '
#print(s)
for line in f:
    p = pt(ints(line))
    ptbound(bnds,p)
    #l.append(p)
    s+=f"L {','.join(str(x) for x in p)}"
    rs+=f'<circle cx="{p[0]}" cy="{p[1]}" r="200" fill="red" /> '
print(f'''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg  xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="100pt" height="100pt" viewBox="{" ".join(map(str,tuple(bnds[0])+tuple(bnds[1])))}">
<path fill="green" stroke="green" d="{s} Z"></path>
{rs}</svg>''')

    
