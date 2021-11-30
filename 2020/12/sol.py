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


px,py=(0,0)

hx,hy=(10,1)

for x in l:
    ins=x[0]
    v=int(x[1:])
    if ins in "NSEW":
        a,b=ds["NSEW".index(ins)]
        hx+=a*v
        hy+=b*v
    elif ins in "LR":
        if ins=="L":
            v=360-v
        while v>0:
            v-=90
            hx,hy=hy,-hx
    elif ins=="F":
        px+=hx*v
        py+=hy*v
    else:
        print("e")

print(px+py)
    
