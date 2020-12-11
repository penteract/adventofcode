from functools import *
from itertools import *
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)
def mint(ns):
    return list(map(int,ns))

ds = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

f = open("input")

l = [x[:-1] for x in f]
d=defaultdict(int)

def mkmap(xss):
    m=defaultdict(lambda : ";")
    for y,row in enumerate(xss):
        for x,c in enumerate(row):
            m[x,y]=c
    return m


m=mkmap(l)
ch=True
while ch:
    print(len([k for k in m if m[k]=="#"]))
    ch=False
    nx=defaultdict(lambda : ";")
    for k in list(m):
        x,y=k
        n=0
        for dx,dy in ds:
            z=1
            while m[x+z*dx,y+z*dy]==".":
                z+=1
            if m[x+z*dx,y+z*dy]=="#":
                n+=1
        if m[k]=="L":
            if n==0:
                nx[k]="#"
                ch=True
            else:
                nx[k]="L"
        if m[k]=="#":
            if n>=5:
                nx[k]="L"
                ch=True
            else:
                nx[k]="#"
        elif m[k]==".":
            nx[k]=m[k]
    m=nx


print(len([k for k in m if m[k]=="#"]))
