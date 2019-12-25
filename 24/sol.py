from functools import *
from itertools import *
from collections import defaultdict
from math import gcd,atan2
from string import *
import sys
from heapq import *
def neighbs(p):
    """neighbours in a 2D grid"""
    x,y=p
    for dx in [1,-1]: yield (x+dx,y)
    for dy in [1,-1]: yield (x,y+dy)

def ns2(x,y,z):
    for a,b in neighbs((x,y)):
        if (a,b)==(2,2):
            dx=x-2
            dy=y-2
            for i in range(5):
                if dx==0:
                    yield (i,2+2*dy,z+1)
                elif dy==0:
                    yield (2+2*dx,i,z+1)
        elif a==-1:
            yield (1,2,z-1)
        elif a==5:
            yield (3,2,z-1)
        elif b==-1:
            yield (2,1,z-1)
        elif b==5:
            yield (2,3,z-1)
        else: yield (a,b,z)
    
lcm = lambda x,y: x*y//gcd(x,y)
DS=10007
f = open("input")
##f="""....#
###..#.
###.?##
##..#..
###....""".split()
lines = [x.strip() for x in f]
print("lines:",len(lines),"firstlinelength:",len(lines[0]))

e = [["."]*5]*5
m = [e]*105+[lines] +[e]*105

#()
def step(m):
    r=[]
    for z,g in enumerate(m[:-1]):
        r.append([])
        for x,l in enumerate(g):
            r[-1].append([])
            for y,c in enumerate(l):
                if (x,y)!=(2,2):
                    t=0
                    for (a,b,cz)in ns2(x,y,z):
                        #print(a,b,c)
                        #print(m[c][a])
                        if m[cz][a][b]=="#":
                            #print("counted")
                            t+=1
                        else: assert m[cz][a][b]=="."
##                    if (x,y,z)==(2,3,100):
##                        print(r[z])
##                        print(m[z],g,l)
##                        print(c,t)
                    if (c=="#" and t==1) or ((t==2 or t==1) and c=="."):
                        r[-1][-1].append("#")
                        #print("new")
                    else:
                        r[-1][-1].append(".")
                    #if t>0:
                        #print(x,y,z,t)
                else: r[-1][-1].append("?")
    return r+[e]
    
            
for l in m:
    if any(any(c=="#" for c in r) for r in l):
        for r in l:  print("".join(r))
        print()    

for i in range(200):
    #k = "".join(m)
    #print()
    m=step(m)
##    for l in m:
##        if any(any(c=="#" for c in r) for r in l):
##            for r in l:  print("".join(r))
##            print()

for l in m:
    if any(any(c=="#" for c in r) for r in l):
        for r in l:  print("".join(r))
    print()  
print(sum(sum(sum(x=="#" for x in r) for r in l) for l in m))
# WRONG:
# 1922 (test input)
