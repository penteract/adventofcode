from functools import *
from itertools import *
from collections import defaultdict
from math import gcd,atan2
from string import *
import sys
from heapq import *

lcm = lambda x,y: x*y//gcd(x,y)

f = open("input")
lines = list(f)
print("lines:",len(lines),"firstlinelength:",len(lines[0]))
m=lines
keys = {} # key:pos
doors = {} # key:doorpos

for y,l in enumerate(lines):
    for x,r in enumerate(l):
        if r=="@":pos=(x,y)
        if r in ascii_lowercase: keys[r]=(x,y)
        if r in ascii_uppercase: doors[r.lower()]=(x,y)


par = {}
startpos = pos
tricky = [(pos[0]+dx,pos[1]+dy) for dx in [-1,1] for dy in [-1,1]]
def neighbs(p):
    x,y=p
    for dx in [1,-1]: yield (x+dx,y)
    for dy in [1,-1]: yield (x,y+dy)

fr = [(p,2,pos) for p in tricky]
seen=set()
while fr:
    ps,d,pr = fr.pop(0)
    if ps  in seen: print(ps)
    seen.add(ps)
    l = [x for x in neighbs(ps) if x not in seen and m[x[1]][x[0]]!="#"]
    if len(l)>1 or m[ps[1]][ps[0]]!=".":
        #print(m[ps[1]][ps[0]],ps)
        par[ps]=(pr,d)
        for x in l: fr.append((x,1,ps))
    else:
        for x in l: fr.append((x,d+1,pr))
chld = defaultdict(list)
for k in par:
    if k!= startpos:
        chld[par[k][0]].append(k)


keysowned = []
def available(owned):
    """lists available keys given that certain keys are owned,"""
    for k in keys:
        if k in owned: continue
        p = keys[k]
        d=0
        while p!=startpos:
            pr=par[p]
            d+=pr[1]
            p=pr[0]
            c = m[p[1]][p[0]]
            if c in ascii_letters and c.lower() not in owned:
                break
        else:
            yield k


def dist(p1,rbots):
    
    d1=0
    ds = {}
    while p1 not in tricky:
        ds[p1]=d1
        pr=par[p1]
        d1+=pr[1]
        p1=pr[0]
    ds[p1]=d1
    i = tricky.index(p1)
    p2=rbots[i]
    d2=0
    while p2 not in tricky and p2 not in ds:
        pr=par[p2]
        d2+=pr[1]
        p2=pr[0]
    if p2 in ds:
        return i,d2+ds[p2]
    else:
        assert False
        return i,d1+d2+abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
        

#A* search where states consist of a set of keys and position
#Dijkstra's is technically a form of A*, right?

fr = [(0,"",tuple(tricky))]
bd = {}

while fr:
    d,got,rbs = heappop(fr)
    a=False
    for k in available(got):
        a=True
        ps=keys[k]
        i,ds = dist(ps,rbs)
        ds+=d
        st=("".join(sorted(k+got)), rbs[:i]+(ps,)+rbs[i+1:])
        if st not in bd or bd[st]>ds:
            bd[st]=ds
            heappush(fr,(ds,st[0],st[1]))
    if not a:
        print("done",got,rbs,d)
        break
    if len(fr)%1000==0: print(len(fr),len(fr[0][1]))
    




