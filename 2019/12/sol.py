from functools import *
from itertools import *
from collections import defaultdict
from math import gcd,atan2

f = open("input")
contents = list(f)
moons = [[-14, -4, -11],
[-9,6,-7],
[4, 1, 4],
[2, -14, -9]]

moons = [[p,[0,0,0]] for p in moons]

def adjvel (m,n):
    for i in range(3):
        if m[0][i]!=n[0][i]:
            d = (m[0][i]-n[0][i])
            d//=abs(d)
            assert abs(d)==1
            n[1][i]+=d
            m[1][i]-=d

def adjpos(m):
    for i in range(3):
        m[0][i]+=m[1][i]

def te(m):
    return sum(abs(x) for x in m[0])*sum(abs(x) for x in m[1])

d=set()

dxyz = {},{},{}

t=0
flag=0
res=[None,None,None]
while flag!=7:
    for i in range(3):
        dat = tuple(v[i] for m in moons for v in m)
        if dat not in dxyz[i] : dxyz[i][dat]=t
        elif not (flag&(1<<i)):
            flag|=1<<i
            print(i,dxyz[i][dat],"delta:", t-dxyz[i][dat])
            print(flag)
            res[i]=t,t-dxyz[i][dat]
    for m in range(len(moons)):
        for n in range(m+1,len(moons)):
            adjvel(moons[m],moons[n])
        adjpos(moons[m])
    t+=1
    if (t%1000000)==0: print(t,moons)


lcm = lambda x,y: x*y//gcd(x,y)
x,y,z = [r[1] for r in res]
print(lcm(lcm(x,y),z))
