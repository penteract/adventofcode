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
d=defaultdict(int)
#l=[1068773,"7,13,x,x,59,x,31,19"]

k=int(l[0])

l=[(i,int(x)) for i,x in enumerate(l[1].split(",")) if x!="x"]

d=1
i=0
while True:
    while i<len(l):
        n,a = l[i]
        if k%a!=-n%a:
            break
        else:
            d*=a
            i+=1
    else: break
    k+=d
    

print(k)
