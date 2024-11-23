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


m=defaultdict(list)
for y,line in enumerate(f):
    #print(line.split(":"))
    a,b = line.split(":")
    for k in b.split():
        k=k.strip()
        if k:
            m[a].append(k)
            m[k].append(a)
        #print(f"{a} --find  {k}")

k=list(m)[0]#tnc?
import random
k2=random.choice(list(m))#zvp st
print(k2)

es = defaultdict(int)
def flatten(tup):
    l=[]
    while tup is not None:
        l.append(tup[0])
        tup=tup[1]
    return l

from collections import deque
#es2=set()
while True:
    #find path k to k2
    print("st")
    q=deque()
    q.append((k,None))
    seen={k}
    while q:
        p=q.popleft()
        n=p[0]
        for n2 in m[n]:
            if n2==k2:
                break
            if es[(n,n2)]<1 and n2 not in seen:
                seen.add(n2)
                q.append((n2,p))
        else:
            continue
        t=flatten(p)
        for a,b in zip(t,t[1:]):
            es[a,b]-=1
            es[b,a]+=1
        break
    else:
        break


tot=0

#print(lmap(ints_locs,f))

print(tot)
