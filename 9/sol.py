from functools import *
from itertools import *
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)
def mint(ns):
    return list(map(int,ns))


ds = [(0,1),(1,0),(0,-1),(-1,0)]

f = open("input")
l = [int(x[:-1]) for x in f]
d=defaultdict(int)
#r=list(map(int,l[0].split()))

for i in range(25,len(l)):
    for x in range(i-25,i):
        for y in range(x,i):
            if x>=0 and y>=0 and l[x]+l[y]==l[i]:
                break
        else:
            continue
        break
    else:
        print(i,l[i])
        break
        
for i in range(len(l)):
    s=0
    for j in range(i,len(l)):
        s+=l[j]
        if 22406676==s:
            print(i,j,max(l[i:j+1])+min(l[i:j+1]))
        if s>2406676:
            pass
            #if i%100==0:print(j)
            #break
