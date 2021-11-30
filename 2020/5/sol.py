from functools import *
from itertools import *
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)
def mint(ns):
    return list(map(int,ns))

ds = [(0,1),(1,0),(0,-1),(-1,0)]

f = open("input")
l=[x for x in f]
d=defaultdict(int)
#r=list(map(int,l[0].split()))

def f(s):
    return eval("0b"+s.replace("B","1").replace("F","0").replace("R","1").replace("L","0"))

s= set([f(x)for x in l])
for k in s:
    if k+2 in s and k+1 not in s:
        print(k+1)


print(v)
