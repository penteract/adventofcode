from functools import *
from itertools import *
from collections import defaultdict
from math import gcd,atan2
from string import *
import sys
from heapq import *

lcm = lambda x,y: x*y//gcd(x,y)
DS=10007
f = open("input")
lines = list(f)
print("lines:",len(lines),"firstlinelength:",len(lines[0]))
DS = 119315717514047
repeat=101741582076661

pos = 2020
d = {}

#DS=100
#pos=8
#lines="""deal with increment 3
#deal into new stack""".split("\n")

opt = []
for line in reversed(lines):
    if line.startswith("cut"):
        n = int(line[4:])
        opt.append((0,n))
    elif line.startswith("deal with increment"):
        n = int(line[20:])
        assert gcd(n,DS)==1
        k = DS%n
        D=[0]*(k+n)
        dl=0
        for i in range(k+n):
            D[(i*n)%(k+n)]=i+dl
            if ((i+1)*n)%(k+n)<(i*n)%(k+n):
                dl+=(DS-n-k)//n
        #print(D)
        opt.append((1,n,D))
    elif line:
        assert line.startswith("deal into new stack")
        opt.append((2,0))
print(opt)
while True:
    oldpos=pos
    for line in opt:
        if line[0]==0:
            pos = (pos+line[1])%DS
        elif line[0]==1:
            n = line[1]
            q = pos//n
            #print(n,q,line[2][pos%n])
            pos=(q+line[2][pos%n])%DS
            
        elif line[0]==2:
            pos=(DS-1-pos)
    d[oldpos]=pos
    if pos in d: break

#print(deck)
#print(deck.index(2019))
#for i in range(DS):
#    assert i in deck
print(pos,d[pos])
