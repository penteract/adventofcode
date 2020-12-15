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
#l=[1068773,"7,13,x,x,59,x,31,19"]


def fl(mask):
    x=1
    yield 0
    while x<=mask:
        if x&mask:
            for k in fl(mask&(x-1)):
                yield x|k
        x<<=1

for x in l:
    if(x.startswith("mask = ")):
        msk=x[7:]
        mk=msk.replace("1","0")
        mk=mk.replace("X","1")
        msk=msk.replace("X","0")
        mask=int(mk,2)
        vals=int(msk,2)
    else:
        assert x.startswith("mem[")
        x=x[4:]
        n=""
        while x[0].isdecimal():
            n=n+x[0]
            x=x[1:]
        loc=int(n)
        assert x.startswith("] = ")
        x=x[4:]
        val=int(x)
        #print(loc,val)
        for f in fl(mask):
            #print(mask,loc,vals,f)
            d[(~mask&loc)|vals|f]=val
    
print(sum(d[k] for k in d))
