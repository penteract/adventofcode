from functools import *
from itertools import *
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)
def mint(ns):
    return list(map(int,ns))

f = open("input")
l=[x for x in f]
d=defaultdict(int)
#r=list(map(int,l[0].split()))

def f(dx,dy):
    x=0
    y=0
    n=0
    while y<len(l):
        if l[y][x%(len(l[y])-1)]=="#":n+=1
        x+=dx
        y+=dy
        #print(l[y][x])
    return n
print(f(1,1)*f(3,1)*f(5,1)*f(7,1)*f(1,2))
