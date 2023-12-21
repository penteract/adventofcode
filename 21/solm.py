import re
from typing import Tuple, Callable, Iterable, Optional
import sys
##from utils.interval import I
##
##def ri(r1,r2):
##    """Given 2 cuboids described as tuples of intervals, find their intersection"""
##    return tuple((a&b) for a,b in zip(r1,r2))

fname=sys.argv[1] if len(sys.argv)>1 else "input"
if fname!="input":
    steps=int(open(fname).read())
    fname="input1"
else:
    steps=26501365
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
#print(f)
fgroups = ftext.split("\n\n")
if len(fgroups)>1:
    fgs = [g.split("\n") for g in fgroups]
    fgns = [lmap(ints,g) for g in fgs]

try: xs = lmap(int,f)
except Exception: pass
try: xss = lmap(ints,f)
except Exception: pass



d=defaultdict(int)
for y,line in enumerate(f):
    for x,c in enumerate(line):
        d[x,y]=c
        if c=="S":
            p=Pt((x,y))
            d[x,y]="."
#print(f)
maxx = len(f[0])
maxy=len(f)
mp=dict(d)
#from collections import frozenset as f

minT = min(steps,1)
class MinSection:
    ALL={}
    def __init__(self,fs):
        self.scale=0
        self.fs=fs
        assert fs not in MinSection.ALL
        MinSection.ALL[fs]=self
        self.l=len(fs)
        self.chs={}
        self.edges = [frozenset((x,y) for (x,y) in fs if x==a or y==b) for a,b in [("",0),(0,""),(maxx,""),("",maxy)]]
        self.size=maxx
    def __hash__(self):
        return hash(self.fs)
    def __eq__(self,other):
        #return self.fs==other.fs
        return self is other
    def step(self,nbs,steps=1):
        #print(steps,len(nbs),flush=True)
        #print("minS",steps,self.l)
        if steps==0:
            return self
        nx=set()
        k = tuple(sorted(nbs.items()))
        if (k,steps) in self.chs:
            return self.chs[k,steps]
        l = set()
        for x in self.fs:
            l.add(x)
        for nb in nbs:
            for x in nbs[nb].fs:
                l.add(maxx*nb+x)
        #print("")
        for i in range(steps):
            #print(len(l))
            ll=set()
            for x in l:
                for dr in ods:
                    if mp[tuple(a%maxx for a in (x+dr))]==".":
                        ll.add(x+dr)
            l=set(ll)
##        for y in range(maxy):
##            for x in range(maxx):
##                if (x,y) in mp:
##                    if d[x,y]!="#":
##                        for dr in ods:
##                            nx,ny = (x,y)+dr
##                            if nx<0:
##                                if (maxx+nx,ny) in nbs[nx,0].fs:
##                                    break
##                            elif nx>=maxx:
##                                if (nx-maxx,ny) in nbs[1,0].fs:
##                                    break
##                            if ny<0:
##                                if (nx,maxy+ny) in nbs[0,-1].fs:
##                                    break
##                            elif ny>=maxy:
##                                if (nx,ny-maxy) in nbs[0,1].fs:
##                                    break
##                            else:
##                                continue
##                            nx.add((x,y))
##                            break
        fs = frozenset(x for x in l if all(0<=c<maxx for c in x))
        #print(len(fs))
        if fs in MinSection.ALL:
            r= MinSection.ALL[fs]
        else:
            r= MinSection(fs)
        self.chs[(k,steps)]=r
        return r
    def nxt(self,nbs,steps):
        assert steps<=maxx
        return self.step(nbs,steps)
            
def getmst(n):
    k=1
    while (k:=(k*3))<=n:
        pass
    return k//3

maxx3 = getmst(maxx)
class Section:
    ALL={}
    def __init__(self,parts):
        """parts is a dict with keys in ddirs+[(0,0)]"""
        #assert scale>0
        self.parts = parts
        self.scale=self.parts[0,0].scale+1
        self.size=minT*(3**self.scale)
        self.l = sum(parts[k].l for k in parts)
        kk = tuple(self.parts[k] for k in ddirs+[(0,0)])
        self.h = hash(kk)
        assert kk not in Section.ALL
        Section.ALL[kk]=self
        self.chs={}
    def __hash__(self):
        return self.h
    def __eq__(self,other):
        #return self.fs==other.fs
        return self is other
    def nxt(self,nbs,steps):
        key = tuple(nbs[dr] for dr in ddirs)
        istp = steps
        if (key,steps) in self.chs:
            #if self.scale>2:
                #print(steps,self.scale,self.size,"fast")
            return self.chs[key,steps]
        if self.scale>2:
            print(steps,self.scale,self.size, [nbs[k].l for k in nbs],self.l)
        assert steps<=self.size
        dd = {**self.parts}
        for k in nbs:
            for p in nbs[k].parts:
                dd[3*k+p]=nbs[k].parts[p]
        stepsize = self.parts[0,0].size
        while steps>0:
            if steps<stepsize:
                stepsize=steps
            nd={}
            for k in dd:
                if all(dr+k in dd for dr in ddirs):
                    nd[k] = dd[k].nxt({dr:dd[dr+k] for dr in ddirs},stepsize)
            steps-=stepsize
            dd=nd
        r=getSec({k:dd[k] for k in self.parts})
        self.chs[key,istp]=r
        return r
        
        
        

def getSec(parts):
    t=tuple(parts[k] for k in ddirs+[(0,0)])
    if t in Section.ALL:
        return Section.ALL[t]
    else:
        return Section(parts)

center = MinSection(frozenset([p]))
e1 = MinSection(frozenset())
empty = e1
import math
for i in range(int(math.log(steps,3))+2):
    nd = {k:empty for k in ddirs}
    center = getSec({(0,0):center,**nd})
    empty = getSec({(0,0):empty,**nd})
    #getSec({k:empty for k in ddirs+[(0,0)]})
print(lmap(ints_locs,f))
#print(len(l))
nd = {k:empty for k in ddirs}
#steps = 26501365 if fname=="input" else 6
print(center.nxt(nd,steps).l)
