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

def search(nvs,glob):
    #print(nvs)
    if len(nvs)==0:
        w="in"
        while w not in "AR":
            for r,dst in d[w]:
                #print(r,dst)
                #print(dd["s"])
                if eval(r,glob):
                    w=dst
                    break
            #if w not in "AR":raise Exception()
        if w=="A": return 1
        else: return 0
    n,vs = nvs[0]
    prev=0
    tot=0
    for x in vs:
        if len(nvs)>2:
            print(prev,x)
        glob[n]=x
        tot+=(x-prev)*search(nvs[1:],glob)
        prev=x
    return tot

l=[]
for k,v in diffs.items():
    l.append((k,sorted(set(v+[4000]))))
print(l)
print(search(l,{}))
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
