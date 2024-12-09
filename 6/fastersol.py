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

def Pt(args):
    return complex(*args)
class Pt3(complex):
    def __new__(cls,args):
        re,im = args
        return super(re,im)
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
def rt(x):
    return x*1j
class Pt2(tuple):
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

xs=[]
ys=[]#
d=defaultdict(int)
for y,line in enumerate(flns):    
    for x,c in enumerate(line):
        d[Pt((x,y))]=c
        if c=="^":
            start=Pt((x,y))
#d[start]="."
sd = dirs["U"]

p = start


tot=0
d2 = d
d = {**d2}
#print(p,sd)
while p+sd in d:
    #tot+=(d[p]!="X")
    d[p]="X"
    if d[p+sd] !="#":
        p = p+sd
        #print(p)
    else:
        sd = rt(sd) #.right()
d[p]="X"
d3=d
#print(sys.argv)
k = int(sys.argv[2])
for ip in d:
    #print(ip.real)
    if abs(ip.real+0.5-k) < 3: #sys.argv[2]:
        #print(ip)
        if d3[ip]=="X":
            d = {**d2}
            lp = set()
            d[ip]="#"
            p = start
            sd = dirs["U"]
            #print(ip,p,sd)
            while (p+sd in d) and ((p,sd) not in lp):
                lp.add((p,sd))
                if d[p+sd] !="#":
                    p = p+sd
                    #print(p)
                else:
                    sd = rt(sd) #.right()
                #print(p,sd)
            #print(len(lp))
            if (p,sd) in lp:
                #print(ip)
                tot+=1
#print("?")
    
#print(lmap(ints_locs,f))

print(tot)




# how to run this in parrallel
#seq 1 6 140 | xargs -P 30 -n 1 python3 fastersol.py input | awk '{sum+=$0;} END{print sum;}'



















