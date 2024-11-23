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
    ">":Pt((1,0)),
    "^":Pt((0,-1)),
    "<":Pt((-1,0)),
    "v":Pt((0,1))
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


d=defaultdict(int)
for y,line in enumerate(f):
    for x,c in enumerate(line):
        if c=="." and y==0:
            p=pt(x,y)
        if c=="." and y==len(f)-1:
            e=pt(x,y)
        d[x,y]=c

        
d2=defaultdict(int)
for k in d:
    if d[k] in dirs:
        d2[k+dirs[d[k]]]+=1
        d2[k-dirs[d[k]]]+=1

cors = [p,e]
for k in d2:
    if d2[k]>1:
        cors.append(k)
g={}
rg=defaultdict(list)



def pth(x):
    for p in [x+dr for dr in ods if d[x+dr] not in ["#",0] ]:
        n=0
        s={x,p}
        while p not in cors:
            #print(p)
            if d[p] in dirs:
                p+=dirs[d[p]]
                if p in s:
                    break
                s.add(p)
            else:
                for dr in ods:
                    q=p+dr
                    if (d[q]in dirs or d[q]==".") and q not in s :
                        s.add(q)
                        p=q
                        break
                else:
                    break
        if p!=x and p in cors:
            yield (p,len(s))

for x in cors:
    #print(x,flush=True)
    g[x] = list(pth(x))
    for k,dst in g[x]:
        rg[k].append((x,dst))
    print(x, "->", g[x])
best= defaultdict(int)
best[p]=0
for i in range(len(g)):
    for k in g:
        if k!=p:
            best[k]=max(ds+best[n]-1 for (n,ds) in rg[k])

print(best[e])
def prgrid(d):
    xs = set(k[0] for k in d)
    ys = set(k[1] for k in d)
    for y in range(min(ys),max(ys)+1):
        for x in range(min(xs),max(xs)+1):
            k=x,y
            print(d[k] if d[k]!=0 else ".",end="")
        print()
for x in cors:
    d[x]=str(x)
#prgrid(d)


#print(ast([(p,frozenset())],neighbs,done=lambda x:x[0]==len(f)-1)[1])
#tot=0

#print(lmap(ints_locs,f))

#print(tot)
