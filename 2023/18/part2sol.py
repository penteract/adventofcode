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

fgroups = ftext.split("\n\n")
if len(fgroups)>1:
    fgs = [g.split("\n") for g in fgroups]
    fgns = [lmap(ints,g) for g in fgs]

try: xs = lmap(int,f)
except Exception: pass
try: xss = lmap(ints,f)
except Exception: pass


d=defaultdict(list)

tot=0

pos=pt(0,0)
corners = []
vedges=[]
hedges=[]
for line in f:
    dr,n,h=line.split()
    dr = "RDLU"[int(h[-2])]
    n=int(h[2:-2],16)
    print(dr,n)
    dr = dirs[dr]
    n=int(n)
    last=pos
    pos+=n*dr
    corners.append(pos)
    [vedges,hedges][dr[0]!=0].append((pos,last) if sum(dr)==-1 else (last,pos))
class I:
    """half open intervals of integers """
    __slots__ = ["s","e"]
    def __init__(self,start,end=None,len=None):
        assert (end is None) != (len is None)
        if end is None:
            end = start + len
        if end<start:
            end=start
        self.s=start
        self.e=end
    def __len__(self):
        return self.e-self.s
    def __iter__(self):
        return range(self.s,self.e)
    def __and__(self,other):
        x,e = self.s,self.e
        a,b = other.s,other.e
        return I(max(x,a),min(e,b))
    def __or__(self,other):
        x,e = self.s,self.e
        a,b = other.s,other.e
        return I(min(x,a),max(e,b))
    def __add__(self,k):
        return I(self.s+k,self.e+k)
    def __str__(self):
        return f"I({self.s},{self.e})"
    def __sub__(self,k):
        if isinstance(k,I):
            x,e = self.s,self.e
            a,b = k.s,k.e
            if a>=b:
                return [self] # could argue that it should split using empty intervals
            res=[]
            if x<a:
                res.append(I(x,min(a,e)))
            if e>b:
                res.append(I(x,max(x,b)))
            return res
        else:
            raise TypeError("Set difference must be between two intervals")
            #return I(self.s-k,self.e-k)


def count(y):
    #print(y)
    ls = [(v[0][0],v[1][1]) for v in vedges if v[0][1]<=y<v[1][1]]
    hs = [I(x[0][0],x[1][0]+1) for x in hedges if x[0][1]<=y<=x[1][1]]#eq
    #print(ls)
    ll=sorted(ls)
    #print(y,ll,)
    n=False
    tt=0
    prev=-1
    for x in ll:
        if n:
            hs.append(I(prev,x[0]+1))
        else:
            prev=x[0]
        n = not n
    hs = sorted(hs,key=lambda x:x.s)
    i=None
    while hs:
        nx=hs.pop(0)
        if i is None:
            i=nx
        if len(nx&i)>0:
            i=i|nx
        else:
            tt+=len(i)
            print(y,i)
            i=nx
    tt+=len(i)
    print(y,i)
    print("result:",tt)
    return tt
print(hedges)
print(vedges)
ys = sorted(set(x[1] for h in hedges for x in h ))
print(ys)
for y1,y2 in zip(ys,ys[1:]):
    print(y1,y2)
    tot+=count(y1+1)*(y2-y1-1)

for y in ys:
    tot+=count(y)
print(tot)
print(corners)
import matplotlib.pyplot as plt
plt.plot([c[0] for c in corners],[c[1] for c in corners],marker="o")
plt.show()
