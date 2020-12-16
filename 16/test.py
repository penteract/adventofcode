from functools import *
from itertools import *
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)
def mint(ns):
    return list(map(int,ns))

ds = [(0,1),(0,-1),(1,0),(-1,0)]

f = open("input")


l = [x[:-1] for x in f]

i=iter(l)

flds=[]

while (n:=next(i)):
    nm,rng=n.split(":")
    r1,r2=rng.split("or")
    a,b=mint(r1.split("-"))
    c,d=mint(r2.split("-"))
    flds.append((nm,(a,b),(c,d)))

assert next(i).startswith("your ")
yt=mint(next(i).split(","))

assert not next(i)
assert next(i).startswith("near")

l = [mint(x.split(",")) for x in i if x]

tot=0

r=[]

for a in l:
    for b in a:
        for (n,(w,x),(y,z)) in flds:
            if w<=b<=x or y<=b<=z:
                break
        else:
            break
    else:
        r.append(a)
        
d=defaultdict(lambda : set(range(len(r[0]))) )

for a in r:
    for i,b in enumerate(a):
        for (n,(w,x),(y,z)) in flds:
            if not (w<=b<=x or y<=b<=z):
                d[n].remove(i)

res={}
while True:
    for n in d:
        if len(d[n])==1:
            a=list(d[n])[0]
            if n in res:
                print(n,"err")
            res[n]=a
            for k in d:
                if a in d[k]:
                    d[k].discard(a)
            break
    else:
        break
    
tot=1
for n,ax,y in flds:
    if n.startswith("departure"):
        tot*=yt[res[n]]
print(tot)
