from functools import *
from itertools import *
import operator as op
from collections import defaultdict
import re
import sys
sys.setrecursionlimit(100000)
def mint(ns):
    return list(map(int,ns))

ds = [(0,1),(0,-1),(1,0),(-1,0)]
lefts = {t:l for t,l in zip("tblr","lrbt")}
rights = {l:t for t,l in zip("tblr","lrbt")}
getright=[rights,lefts]

f = open("input")
##
##f="""mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
##trh fvjkl sbzzf mxmxvkd (contains dairy)
##sqjhc fvjkl (contains soy)
##sqjhc mxmxvkd sbzzf (contains fish)""".split("\n")

l=[x[:-1] for x in f]

ll=[]

for x in l:
    a,al = x.split("(")
    ll.append((a.split(),[x.strip("), ") for x in al[8:].split()]))
s=set()
ss=set()
ms=defaultdict(list)
for a,b in ll:
    for x in b:
        s.add(x)
        ms[x].append(a)
    for y in a:
        ss.add(y)


m={x:ss.copy() for x in s}

for a,b in ll:
    for y in b:
        mx=m[y]
        for i in mx.copy():
            if i not in a:
                mx.discard(i)

k = ss 

for a in m.values():
    k-=a

r=0
for a,b in ll:
    for x in a:
        if x in k:r+=1

res={}
while [x for x in (m) if len(m[x])>=1]:
    x=[x for x in (m) if len(m[x])==1][0]
    y=list(m[x])[0]
    for a in m:
        m[a].discard(y)
    res[x]=y

for a in sorted(res):
    print(res[a],end=",")
