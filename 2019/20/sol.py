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

def mkmap(xss):
    m={}
    for y,row in enumerate(xss):
        for x,c in enumerate(row):
            m[x,y]=c
    return m

m = mkmap(lines)


def neighbs(p):
    """neighbours in a 2D grid"""
    x,y=p
    for dx in [1,-1]: yield (x+dx,y)
    for dy in [1,-1]: yield (x,y+dy)

def available(p):
    #print(p)
    for x in neighbs(p[0]):
        if m[x]==".": yield (x,p[1])
    if p[0] in tp:
        yield (tp[p[0]][0],tp[p[0]][1]+p[1])
        
ls={}
tp={}

def isouter(p):
    return p[0]<10 or p[1]<10 or max(p[0],p[1])>110

for k in m:
    if m[k]==".":
        for x in neighbs(k):
            if m[x] in ascii_uppercase:
                dx=x[0]-k[0]
                dy=x[1]-k[1]
                t = m[x]+m[x[0]+dx,x[1]+dy]
                if dx+dy>0: t="".join(reversed(t))
                if t in ls:
                    print(t)
                    o = -1 if isouter(k) else 1
                    tp[k]=ls[t],o
                    tp[ls[t]]=k,-o
                else:
                    ls[t]=k
                

print(tp)
pos = ls["AA"]


fr = [(0,(pos,0))]
seen = set()

while fr:
    d,nxp = heappop(fr)

    for k in available(nxp):
        if k not in seen and k[1]>=0:
            seen.add(k)
            heappush(fr,(d+1,k))
    if nxp==(ls["ZZ"],0):
        print("done",d,nxp)
    #if len(fr)%10==0: print(len(fr),len(fr[0][1]))
print(d,nxp)
