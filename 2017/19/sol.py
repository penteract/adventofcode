from functools import *
from itertools import *
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)

f = open("input")

l=[x[:-1] for x in f]

d=defaultdict(int)


def mkmap(xss):
    m={}
    for y,row in enumerate(xss):
        for x,c in enumerate(row):
            m[x,y]=c
    return m


m = mkmap(l)

x=0
while m[x,0]==" ":
    x+=1
y=0

dx=0
dy=1
res=""
c=0
while True:
    c+=1
    for dx,dy in [(dx,dy),(dy,dx),(-dy,-dx)]:
        px,py=x+dx,y+dy
        if (px,py) in m and m[px,py]!=" ":
            x,y=px,py
            if m[px,py] not in "+-|":
                res+=m[px,py]
            break
    else:
        break



print(res,c)
