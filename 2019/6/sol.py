from functools import *
from itertools import *

f = open("input")
l = list(f)
inp = [(s[:3],s[4:7]) for s in l]

d={"COM":[]}

for a,b in inp:#b orbits a
    if a not in d:
        d[a]=[]
    d[a].append(b)
    if b not in d:
        d[b]=[]

def f(c,n=0):
    tot=n
    for x in d[c]:
        tot += f(x,n+1)
    return tot
print (f("COM"))


def dist(x,y):
    if x==y:
        return 0
    return min([10000]+[1+dist(z,y) for z in d[x]])

print(min(dist(x,"SAN")+dist(x,"YOU")-2 for x in d))



#lll = list(map(int,l[0].split(",")) )#+[0 for i in range(3850694)]
