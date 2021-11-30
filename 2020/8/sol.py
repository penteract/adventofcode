from functools import *
from itertools import *
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)
def mint(ns):
    return list(map(int,ns))


ds = [(0,1),(1,0),(0,-1),(-1,0)]

f = open("input")
l = [x[:-1] for x in f]
d=defaultdict(int)
#r=list(map(int,l[0].split()))


for j in range(len(l)):
    i=0
    s=set()
    acc=0

    while i<len(l):
        if i in s:
            break
        s.add(i)
        r=l[i].split(" ")
        n = eval(r[1])
        if (r[0]=="nop") ^( i==j):
            i+=1
        elif r[0]=="acc":
            acc+=n
            i+=1
        elif( r[0]=="jmp") ^ (i==j):
            i+=n
    else:
        print(j)
        print(acc)
    

print(acc)
