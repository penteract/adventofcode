import re
from typing import Tuple, Callable, Iterable, Optional
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"
f = open(fname)
ftext=f.read()
flns=[line.strip() for line in ftext.split("\n")[:-1]]
f=flns

fgroups = ftext.split("\n\n")
if len(fgroups)>1:
    f=fgroups

from collections import defaultdict

d={} #defaultdict(int)

#copied from https://github.com/joefarebrother/adventofcode/blob/master/misc_utils.py
def lmap(f: Callable, *xs) -> list:
    """Like map but returns a list"""
    return list(map(f, *xs))

def ints(xs: Iterable) -> list[int]:
    """Casts each element of xs to an int"""
    return lmap(int, xs)

def mint(x, default=None):
    """Maybe int - casts to int and returns default on failure"""
    try:
        return int(x)
    except ValueError:
        return default

def ints_in(x: str) -> list[int]:
    """Finds and parses all integers in the string x"""
    ex = r'(?:(?<!\d)-)?\d+'
    return ints(re.findall(ex, x))


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
dirs = {
    "R":Pt((0,1)),
    "U":Pt((1,0)),
    "L":Pt((0,-1)),
    "D":Pt((-1,0))
    }
ods = list(dirs.values())

#odirs = [(0,1),(1,0),(0,-1),(-1,0)]
ddirs = lmap(Pt,[(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)])


try:
    xs = ints(f)
except Exception:
    pass
try:
    xss = lmap(ints_in,f)
except Exception:
    pass

s=0
left = None

lns = f[0].split("\n")
sz = max([len(lns)]+lmap(len,lns))//4

for y,l in enumerate(f[0].split("\n")):
    left=None
    for x,c in enumerate(l):
        if c in ".#":
            d[x,y] = c
            if left is None:
                left = x
    if y==0:
        p=Pt((left,0))
        
dr = Pt((1,0))
sp = p,dr
edge = [(p,dr.left())]
dr = Pt((1,0))
p+=dr
edge.append(2)
while (p,dr)!=sp:
    edge.append((p,dr.left()))
    if (lt := p+dr+dr.left()) in d:
        p=lt
        edge.append(3)
        dr=dr.left()
    elif p+dr in d:
        p+=dr
        edge.append(2)
    else:
        edge.append(1)
        dr=dr.right()




def r(p):
    (a,(x,y))=p
    return (a,(-x,-y))

loop = {}
def addloop(p1,p2):
    loop[p1]=r(p2)
    loop[p2]=r(p1)

while edge:
    for i in range(-1,len(edge)-1,2):
        if edge[i]>=3:
            while edge and edge[i]>=3:
                print(edge[i],end=" ")
                addloop(edge[i+1],edge[i-1])
                edge[i-2] += edge[i+2]
                if i==-1:
                    edge[i-1:]=[]
                    edge[:i+3]=[]
                else:
                    edge[i-1:i+3]=[]
                    i-=2
            print()
            break
    else:
        crash
    
"""
es = [edge[i:i+2*sz] for i in range(0,len(edge),2*sz)]    
while es:
    #every tree with at least 2 nodes has at least 2 leaves, so we don't need to worry
    for i in range(len(es)-1):
        # if we've got 3 squares around a corner:
        if es[i][-1]==3:
            prev = es[i-1]
            nx = es.pop(i+1)
            ei = es.pop(i)
            #join 
            lmap(addloop,nx[::2],reversed(ei[::2]))
            if es:
                prev[-1] += nx[-1] # join the corners together
            break
    else:
        print("err",len(es),es)
        exit()
"""

d2 = {}
for n,k in enumerate(loop):
    d2[k[0]]=n
for y,l in enumerate(f[0].split("\n")):
    #left=None
    for x,c in enumerate(l):        
        if (x,y) in d2:
            print((d2[x,y]//2)%8,end="")
        else:
            print(c,end="")
    print()
dr = Pt((1,0))
for ss in f[1].split("R"):
    ss.split("L")
    for s in ss.split("L"):
        k = int(s)
        for i in range(k):
            #nx = p+dr
            if (p,dr) in loop:
                nx,dr_=loop[p,dr]
            else:
                nx = Pt(p)+dr
                dr_=dr
            if d[nx]=="#":
                break
            p=nx
            dr=dr_
        x,y = dr
        dr = Pt((y,-x))
    dr = (-1)*dr
x,y = dr
dr = Pt((y,-x))
x,y = p
x+=1
y+=1
dx,dy=dr
print(x,y,dr)
print(x*4+y*1000+(-dx-dy)+bool(dy)+1)




#print(s)









