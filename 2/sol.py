from functools import *
from itertools import *
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)
def mint(ns):
    return list(map(int,ns))

f = open("input")
l=[x.split() for x in f]
d=defaultdict(int)
#r=list(map(int,l[0].split()))
n=0




for a,b,c in l:
    r,m=list(map(int,a.split("-")))
    #if len(c)<=r+1 or len(c)<=m+1 :
        #>print(a,b,c)
    if (c[r-1]==b[0])^( c[m-1]==b[0] ):
        n+=1
    #if r<=c.count(b[0])<=m: n+=1
print(n)
