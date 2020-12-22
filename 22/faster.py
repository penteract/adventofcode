from functools import *
from itertools import *
import operator as op
from collections import defaultdict
import re
import sys
#sys.setrecursionlimit(1000)
def mint(ns):
    return list(map(int,ns))

ds = [(0,1),(0,-1),(1,0),(-1,0)]

f = open("input")


f=iter("""Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10""".split("\n"))
p1=[]
p2=[]
next(f)

while(k:=(next(f).strip())):
    p1.append(int(k))

next(f)
p2=[int(x) for x in f]
print("hi")
def ply(p1,p2):
    seen=set()
    i=0
    while len(p1)>i and len(p2)>i:
        k=str(p1[i:])+str(p2[i:])
        if k in seen:
            return 1
        else:
            seen.add(k)
        a=p1[i]
        b=p2[i]
        i+=1
        if i+a>=len(p1) and i+b>=len(p2):
            winner = ply(p1[i:i+a],p2[i:i+b])
        else:
            winner=a>b
        if winner:
            p1.append(a)
            p1.append(b)
        else:
            p2.append(b)
            p2.append(a)
    return len(p1)>i


print(ply(p1,p2))
#sum([(i+1)*x for i,x in enumerate(reversed(p1))])
