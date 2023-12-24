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
        return iter(range(self.s,self.e))
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
    def __repr__(self):
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
def mkI(a,b):
    return I(min(a,b),max(a,b)+1)
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

szs=[]

for a,b,c,d,e,f in xss:
    szs.append(tuple(map(mkI,(a,b,c),(d,e,f))))
##    if any(x>y for x,y in zip((a,b,c),(d,e,f))):
##        print("a,b,c,d,e,f")
##    sz=1
##    for k in zip((a,b,c),(d,e,f)):
##        sz*=len(mkI(*k))
##        print(len(mkI(*k)))
##    print("sz",sz)
szs.sort(key = lambda k:k[2].s)
mp = defaultdict(int) # highest brick on ground
d = {}

resting = defaultdict(list)

r2 = defaultdict(list)

for i,k in enumerate(szs):
    bz = max(mp[x,y] for x in k[0] for y in k[1])
    resting
    for x in k[0]:
        for y in k[1]:
            if mp[x,y]==bz and bz>0:
                resting[i].append(d[x,y])
                r2[d[x,y]].append(i)
            mp[x,y]=bz+len(k[2])
            d[x,y]=i

print(len(szs) - len(set(resting[k][0] for k in resting if len(set(resting[k]))==1)))
def prgrid(d):
    xs = set(k[0] for k in d)
    ys = set(k[1] for k in d)
    for y in range(min(ys),max(ys)+1):
        for x in range(min(xs),max(xs)+1):
            k=x,y
            print(d[k] if d[k]!=0 else ".",end="")
        print()
tot =0
for i,b in enumerate(szs):
    fl=set()
    unchecked=[i]
    while unchecked:
        j=unchecked.pop()
        if j not in fl:
            fl.add(j)
            for x in r2[j]:
                if all(k in fl for k in resting[x]):
                    #resting.add(x)
                    unchecked.append(x)
    print(i,len(fl))
    tot+=len(fl)-1
print(tot)
#prgrid(d)
