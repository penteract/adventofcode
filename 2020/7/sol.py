from functools import *
from itertools import *
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)
def mint(ns):
    return list(map(int,ns))

def isprime(p):
    if p%2==0: return False
    k=3
    while k*k<=p:
        if p%k==0:
            return False
        k+=2
    return True

ds = [(0,1),(1,0),(0,-1),(-1,0)]

f = open("input")
l = [x[:-1] for x in f]
d=defaultdict(list)
d2=defaultdict(list)
#r=list(map(int,l[0].split()))

res = []
for x in l:
    n=x.split()
    col = n[:2]
    oth=[]
    i=4
    while(n[i-1][-1]!="." and n[i]!="no"):
        k=int(n[i])
        co = n[i+1:i+3]
        i+=4
        oth.append((k," ".join(co)))
    res.append((" ".join(col),oth))


for c,rs in res:
    d2[c]=rs
    for a,b in rs:
        d[b].append(c)

s=set()

nx=["shiny gold"]

while nx:
    k=nx.pop()
    for x in d[k]:
        if x not in s:
            s.add(x)
            nx.append(x)

def count(b):
    res=0
    for n,c in d2[b]:
        res+=n
        res+=n*count(c)
    return res

print(count("shiny gold"))

print(res[0])
print(len(s))
