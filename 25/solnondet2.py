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

def ufdsget(x,st):
    k = st[x]
    if k==x:
        return x
    else:
        k=ufdsget(k,st)
        st[x]=k
        return k

def ufdsjoin(x,y,st):
    st[ufdsget(x,st)]=ufdsget(y,st)

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
es = [(k,e) for k in m for e in m[k] if k>e]

import random
def trial():
    v = random.choice(list(m))
    st={v}
    nes = [x for x in m[v]]
    def isLoop(e):
        return e in st
    def popAt(ix):
        if len(nes)>ix+1:
            nes[ix]=nes.pop()
        else:
            nes.pop()
    while nes:
        count=0
        while count<=3 and count<len(nes):
            if isLoop(nes[count]):
                popAt(count)
            else:
                count+=1
        if count<=3:
            return count
        while isLoop(nes[ix:=random.randrange(len(nes))]):
            popAt(ix)
        st.add(nes[ix])
        for k in m[nes[ix]]:
            nes.append(k)
r=0
iters=100000
print(
f"""{len(m)} verts
{len(es)} edges
{len(es)*2/len(m)} average degree
guess at the runtime {(2*len(m))**(3/(len(es)*2/len(m)))}
""")
for i in range(iters):
    if trial():
        #e=ufdsget(next(iter(m)),res)
        #r = sum(ufdsget(x,res)==e for x in m)
        #print(r*(len(m)-r))
        r+=1
        #print(i,r)
    if bin(i).count("1")==1:
        print(i,r,end="")
        if r>0:
            print("",i/r,end="")
        print()
print(
f"""{len(m)} verts
{len(es)} edges
{len(es)*2/len(m)} average degree
{r} successes in {iters} iterations
{iters/r} mean iterations per success""")
