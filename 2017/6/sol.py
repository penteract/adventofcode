from functools import *
from itertools import *
from collections import defaultdict

f = open("input")
l=list(f)
l = [int (x) for x in l[0].split()]
print(l)


s={tuple(l):0}
n=0

while True:
    s[tuple(l)]=n
    n+=1
    m=max(l)
    i=l.index(m)
    l[i]=0
    for j in range(m):
        l[(i+j+1)%len(l)]+=1
    t=tuple(l)
    if t in s:
        break
    

print(n)
print(n-s[t])
