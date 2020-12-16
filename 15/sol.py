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
l=mint(l[0].split(","))

#l=[0,3,6]
d=defaultdict(lambda : -1)

i=0
for x in l:
    i+=1
    d[x]=i

last=-1

for i in range(len(l),30000000):
    #print(last,d[last])
    k=d[last]
    d[last]=i
    if k==-1:
        last=0
    else:
        last=i-k
    #print(last,k,d[last])
    
print(last,d[last])
#l=[1068773,"7,13,x,x,59,x,31,19"]


