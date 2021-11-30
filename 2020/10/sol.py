from functools import *
from itertools import *
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)
def mint(ns):
    return list(map(int,ns))


ds = [(0,1),(1,0),(0,-1),(-1,0)]

f = open("input")

l = [int(x) for x in f]
d=defaultdict(int)
#r=list(map(int,l[0].split()))

ll=l.sort()

l+=[l[-1]+3]

px=0
n3=0
n1=0
i=0

d[0]=1

for x in l:
    d[x]=d[x-1]+d[x-2]+d[x-3]
    
"""part 1
while i<len(l):
    x=l[i]
    if x-px==3:
        n3+=1
    elif x-px==1:
        n1+=1
    elif x-px>3:
        print("problem")
        break
    px=x
    i+=1
"""

print(d[l[-1]])
    
