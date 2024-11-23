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


#d=defaultdict(int)
d={}
print(fgs)
diffs = defaultdict(list)
for line in fgs[0]:
    w,rs = line.split("{")
    rs = rs[:-1].split(",")
    rs = [x.split(":") for x in rs]
    rs = [x if len(x)>1 else ("True",x[0]) for x in rs]
    for k,__ in rs:
        if k!="True":
            diffs[k[0]].append(int(k[2:]) - (k[1]=="<") )
    d[w]=rs
print(diffs)
parts = []
for line in fgs[1]:
    if line:
        #rs = line[1:-1].split(",")
        parts.append(line[1:-1].replace(",",";"))
tot=0
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
import math
def search():
    #print(nvs)
    intervals=[(tuple( (x,I(1,4001)) for x in "xmas" ),"in")]
    tot=0
    whole = I(1,4001)
    while intervals:
        xs,w = intervals.pop()
        if w=="R" or math.prod(len(x[1]) for x in xs)==0:
            continue
        if w=="A":
            tot+=math.prod(len(x[1]) for x in xs)
            continue
        for r,dst in d[w]:
            print(w,xs,r,dst)
            if r=="True":
                intervals.append((xs,dst))
            elif r[1]==">":
                n=int(r[2:])
                intervals.append((tuple((a,b&(I(n+1,4001) if a==r[0] else whole)) for a,b in xs) ,dst))
                xs = (tuple((a,b&(I(1,n+1) if a==r[0] else whole)) for a,b in xs))
            else:
                assert r[1]=="<"
                n=int(r[2:])
                intervals.append((tuple((a,b&(I(1,n) if a==r[0] else whole)) for a,b in xs) ,dst))
                xs = (tuple((a,b&(I(n,4001) if a==r[0] else whole)) for a,b in xs))
    return tot

l=[]
for k,v in diffs.items():
    l.append((k,sorted(set(v+[4000]))))
print(l)
print(search())
##for part in parts:
##    w = "in"
##    dd={}
##    #print("p",part)
##    exec(part,dd)
##    while w not in "AR":
##        for r,dst in d[w]:
##            #print(r,dst)
##            #print(dd["s"])
##            if eval(r,dd):
##                w=dst
##                break
##        #print(w)
##    if w=="A":
##        tot+=sum(ints(part))
#print(tot)
