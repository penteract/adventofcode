from functools import *
from itertools import *
import operator as op
from collections import defaultdict
import re
import sys
sys.setrecursionlimit(100000)
def mint(ns):
    return list(map(int,ns))

ds = [(0,1),(0,-1),(1,0),(-1,0)]

f = open("input")
l=[x[:-1] for x in f]



#l=[mint(x.split(",")) for x in f]
d=defaultdict(int)
m={}
f=iter(l)


while (x:=next(f)):
    n,r = x.split(":")
    if "\"" in r:
        r1,c,r2=r.split('"')
        assert len(c)==1
        m[int(n)]=c
    else:
        m[int(n)]= [mint(k.split()) for k in r.split("|")]

l = list(f)

#for k in m:
 #   a=m[k]
  #  assert all(len(a[0])==len(b) for b in a)


#@lru_cache(None)
def count(n):
    if n==8:
        return ("("+"("+count(42)+")"+"+"+")")
    elif n==11:
        a=count(42)+count(31)
        s=a
        for  i in range(16):
            a=count(42)+a+count(31)
            s=s+"|"+"("+a+")"
        return "("+s+")"
    if(isinstance(m[n],str)):
       return m[n]
    else:
        return "("+"|".join(("(" +"".join(count(x) for x in y) +")")for y in m[n])+")"

e=re.compile(count(0)+"$")
n=0
for x in l:
    if e.match(x):
        print(x)
        n+=1
print(n)
