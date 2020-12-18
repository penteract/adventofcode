from functools import *
from itertools import *
import operator as op
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)
def mint(ns):
    return list(map(int,ns))

ds = [(0,1),(0,-1),(1,0),(-1,0)]

f = open("input")
#d=(int)


def evl(x):
    val=None
    op=None
    while x:
        if op=="*":
            v,x=evl(x)
        elif x[0]=="(":
            v,x = evl(x[1:])
            x=x[1:]
        elif x[0] in "1234567890":
            v=int(x[0])
            x=x[1:]
        x=x.strip()
        if op is None:
            val=v
        else:
            #print(x,val,op)
            if op=="*":
                val*=v
            if op=="+":
                val+=v
        if not x:
            break
        if x[0]==")":
            return val,x
        else:
            assert x[0] in "+*"
            op=x[0]
            x=x[1:]
        x=x.strip()
    return val,x
s=0
for line in f:
    
    s+=evl(line)[0]

print(s)
