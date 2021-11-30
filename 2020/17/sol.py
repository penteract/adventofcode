from functools import *
from itertools import *
import operator as op
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)
def mint(ns):
    return list(map(int,ns))

ds = [(0,1),(0,-1),(1,0),(-1,0)]

f = open("input")
#d=(int)

#l=[int(x) for x in f]
l=[x[:-1] for x in f]


def mkmap(xss):
    m=set()
    for y,row in enumerate(xss):
        for x,c in enumerate(row):
            if c=="#":
                m.add((x,y,0,0))
    return m



d=mkmap(l)
print(len(d))

for i in range(6):
    c=defaultdict(int)
    for (x,y,z,w) in d:
        for i in range(-1,2):
            for j in range(-1,2):
                for k in range(-1,2):
                    for kk in range(-1,2):
                        c[x+i,y+j,z+k,w+kk]+=1
    print(c)
    nx=set()
    for p in c:
        if c[p]==3 or c[p]==4 and p in d:
            nx.add(p)
    d=nx

print(len(d)
      )
