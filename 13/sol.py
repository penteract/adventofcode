import re
from typing import Tuple, Callable, Iterable, Optional
import sys
import math,functools,itertools
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
from heapq import *


def Nf(pt):
    return (pt[0]%N,pt[1]%N, pt[0]//N - pt[1]//2)
def ast(start,neighbs,done,h = lambda x:0):
    """Finds the node n such that done(n) with minimal distance from an element of start.
    neighbs(n) = [(nn,edgeweight)]
    assumes h(n)<d(n,end)
    Returns the path as a lisp-style deeply nested tuple"""
    time=0
    seen=set()
    hq = []
    for x in start:
        heappush(hq,(h(x),(x,None),0))
    while hq:
        time+=1
        c,pth,d = heappop(hq)
        n=pth[0]
        nn = Nf(n)
        if nn not in seen:
            #print(n)
            seen.add(nn)
            if done(n):
                return (pth,d)
            for x,dst in neighbs(n):
                if Nf(x) not in seen:
                    heappush(hq,(d+dst+h(x),(x,pth),d+dst))

d=defaultdict(int)

prbs = []
flns = xss
tot=0

def sgn(a):
    if a<0:
        return -1
    elif a>0:
        return 1
    else:
        return 0
import sympy
from sympy.solvers.solveset import linsolve

#def find(da,db,target):
flns.append("")
for a,b,p,uu in zip(flns[0::4],flns[1::4],flns[2::4],flns[3::4]):
    print(a,b,p)
    da = Pt(a)
    db = Pt(b)
    #if sgn(da[0]-da[1]) == sgn(db[0]-db[1]) and sgn(da[0]-da[1]) !=0:
    #    print("unreach")
    #    continue#can't work
    #vs = "An,Bn".split(",")
    p = Pt(p)+(10000000000000,10000000000000) #if fname=="input" else Pt(p)
    s = sympy.symbols("An Bn")
    An,Bn = s
    es = [da[0]*An+db[0]*Bn - p[0], da[1]*An + db[1]*Bn - p[1]]
    l = list(linsolve(es,s))
    print(l,  "   l")
    if l:
        #assert(len(l)==1)
        #k=False
        #[x.denominator for x in l[0]]
        if all(x.denominator==1 for x in l[0]):
            print(l[0])
            assert all(x>=0 for x in l[0])
            tot+=l[0][1]+l[0][0]*3
        else:
            print(l,"reason")
    else:
        print(l,"reason")

    #print(l[0])

    #try:
        #[x.denominator for x in l[0]]

    """
    l = list(linsolve(es,s))[0]
    dv = math.lcm(*[x.denominator for x in l] )
    an = int(l[0]*dv)
    bn = int(l[1]*dv)
    #print(fname)
    p = Pt(p)+(10000000000000,10000000000000) if fname=="input" else Pt(p)
    if any ( p[i]%math.gcd(da[i],db[i]) != 0 for i in [0,1]):
        print("gcd")
        continue

    print(z := an*da + bn*db)
    assert z[0]==z[1]
    N=z[0]
    #k = (10000000000000 - 0) // z[0] ## change 0 to fix
    #cost = (an*3 + bn)*k
    #p -= k*z
    #if p[0]< or p

    print(p)
    fn = lambda x: x[0]+x[1]
    mn = min(fn(da)/3, fn(db))
    #p = Pt(p) + (10000000000000,10000000000000)
    h = lambda x: (fn(p-x) / mn)

    nbs = (lambda pt: [x for x in [(pt+da,3), (pt+db,1)] if x[0][0]<=p[0] and x[0][1]<=p[1]])
    def done(x):
        pp = p-x
        return pp[0]%N==0 and pp[1]%N==0 and pp[0]//N == pp[1]//N

    #done = lambda x: (p-x)[1] == p-x
    cost = 0
    while abs(p[0] - p[1])>100:
        if sgn(p[0]-p[1]) == sgn(da[0] - da[1]):
            p -=da
            cost+=3
        else:
            p -=db
            cost+=1
    print(p)
    start = [Pt((0,0))]
    r = ast(start,nbs,done)
    if r is not None:
        pth,dst = r
        print(dst)
        #print(pth[0])
        k = (p[0] - pth[0][0]) //z[0]
        cost += (an*3 + bn)*k
        print("cost",cost)
        tot+=dst+cost
    else:
        print(a,b,p,"uncertain")
    """
#print(lmap(ints_locs,f))






print(tot)






























