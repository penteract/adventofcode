from functools import *
from itertools import *
import operator as op
from collections import defaultdict
import re
#import sys
#sys.setrecursionlimit(1000)
def mint(ns):
    return list(map(int,ns))

ds = [(0,1),(0,-1),(1,0),(-1,0)]

m={"n":(0,1),"s":(0,-1),"w":(2,0),"e":(-2,0)}

f = open("input")

l = [x.strip() for x in f]
d=defaultdict(int)

res=[]
for x in l:
    dd=iter(x)
    r=[]
    px,py=0,0
    for k in dd:
        a,b=m[k]
        px+=a
        py+=b
        if k in "ns":
            j=next(dd)
            a,b=m[j]
            px+=a//2
            py+=b//2
            r.append(k+j)
        else:
            r.append(k)
    d[px,py]^=1
    #print(r)
    res.append(r)

for i in range(100):
    ns=defaultdict(int)
    for k in d:
        if d[k]:
            x,y=k
            for a,b in [m["e"],m["w"],(1,1),(-1,-1),(1,-1),(-1,1)]:
                ns[x+a,y+b]+=1
            ns[x,y]+=0
    for k in ns:
        if (d[k] and ns[k]==1) or (ns[k]==2):
            d[k]=1
        else:
            d[k]=0
print(sum(d.values()))
