from functools import *
from itertools import *
from collections import defaultdict
from math import gcd,atan2

f = open("input")
contents = list(f)
print(len(contents))
print(len(contents[28]))
print(contents[28])


def gcdd(x,y):
    if x==0 and y==0: return (0,0)
    if x*y==0: g = max(abs(x),abs(y))
    else: g = gcd(abs(x),abs(y))
    return (x//g,y//g)
d = {}

assert gcdd(0,0)==(0,0)
assert gcdd(3,9)==(1,3)
assert gcdd(6,2)==(3,1)
assert gcdd(6,0)==(1,0)

def sign(x):
    return 1 if x>0 else (-1)

res=(0,{})
for y,l in enumerate(contents):
    for x,c in enumerate(l[:-1]):
        poss = defaultdict(list)
        if c=="#":
            for w,l in enumerate(contents):
                for z,c in enumerate(l):
                    if c=="#" and (w-y,z-x)!=(0,0):
                        poss[gcdd(w-y,z-x)].append((w,z,w-y,z-x))
            k = len(poss)
            if k>res[0]:
                print(y,x)
                res = (k,poss)

print(res[0])

poss=res[1]

kys = list(poss.keys())

def ordr(t):
    dy,dx=t
    return atan2(dx,dy)

kys.sort(key=ordr,reverse=True)
print(list(k for k in kys if k[0]*k[1]==0))
print(list(k for k in kys))
l = list(list(x[:-1]) for x in contents)

def sr(t):
    a,b,c,d=t
    return abs(c)+abs(d)

poss = {k:sorted(poss[k],key=sr) for k in poss }

vap = 0
while True:
    print("loop")
    for k in kys:
        if poss[k]:
            val = poss[k].pop(0)
            vap+=1
            if vap==200:
                print(val)
                break
        else:
            print("skip")
    else:
        continue
    break
