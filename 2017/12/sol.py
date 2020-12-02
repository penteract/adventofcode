from functools import *
from itertools import *
from collections import defaultdict

f = open("input")
l=[x.split("<->") for x in f]
d=defaultdict(int)

d={}
for a,b in l:
    d[int(a)] = list (map(int,b.split(",")))

s=set()
def get(n):
    if n not in s:
        s.add(n)
        for k in d[n]:
            get(k)

n=0
for k in d:
    if k not in s:
        get(k)
        n+=1

print(len(s))
print(n)
