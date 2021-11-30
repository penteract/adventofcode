from functools import *
from itertools import *
import operator as op
from collections import defaultdict
import re
import sys
#sys.setrecursionlimit(100000)
def mint(ns):
    return list(map(int,ns))

ds = [(0,1),(0,-1),(1,0),(-1,0)]

f = open("input")
##f=iter("""Player 1:
##9
##2
##6
##3
##1
##
##Player 2:
##5
##8
##4
##7
##10""".split("\n"))
##
p1=[]
p2=[]
next(f)

while(k:=next(f).strip()):
    p1.append(int(k))

next(f)
p2=[int(x) for x in f]

def ply(p1,p2):
    #print("call",p2,p2)
    seen=set()
    while p1 and p2:
        k=str(p1)+str(p2)
        if k in seen:
            #print(len(p1)+len(p2))
            return 1
        else:
            seen.add(k)
            #print(k)
        a=p1.pop(0)
        b=p2.pop(0)
        #print(a,b,p1,p2,len(p1),len(p2),a>=len(p1) , b>=len(p2))
        if a<=len(p1) and b<=len(p2):
            #print("huh")
            winner = ply(p1[:a],p2[:b])
        else:
            winner=a>b
        if winner:
            p1.append(a)
            p1.append(b)
        else:
            p2.append(b)
            p2.append(a)
    return bool(p1)


print(ply(p1,p2))
#sum([(i+1)*x for i,x in enumerate(reversed(p1))])
