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
d=defaultdict(int)
#r=list(map(int,l[0].split()))

def f(s):
    return eval("0b"+s.replace("B","1").replace("F","0").replace("R","1").replace("L","0"))


r=[]

i=iter(l)
ans=set(next(i))
for x in i:
    if x:
        ans=ans.intersection(set(x))
    else:
        r.append(ans)
        ans=set(next(i))
r.append(ans)


print(
    sum(len(set("".join(x))) for x in r))
