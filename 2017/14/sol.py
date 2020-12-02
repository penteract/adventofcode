from functools import *
from itertools import *
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)

f = open("input")
l=[x for x in f]
d=defaultdict(int)
#r=list(map(int,l[0].split()))



def kh(st):
    r=list(range(256))
    p=0
    s=0
    #l=[int(x) for x in l[0].split(",")]
    l=list(map(ord,st))+[17, 31, 73, 47, 23]
    #print(l)
    n=0
    for i in range(64):
        for x in l:
            r=r[x:]+list(reversed(r[:x]))
            r=r[s:]+r[:s]
            n+=x+s
            s=(1+s)%256
    k=256-n%256
    r=r[k:]+r[:k]
    res=[]
    for i in range(16):
        k=0
        for x in r[i*16:(i+1)*16]:
            k^=x
        res.append(k)
        #print(hex(k)[2:].rjust(2,"0"),end="")
    return res

def popcount(n):
    return sum(bin(x).count("1") for x in n)

n=0
res=[]
for i in range(128):
    #l=["flqrgnkx "]
    res.append(kh(l[0][:-1]+"-"+str(i)))
def get(x,y):
    if 128>x>=0 and 128>y>=0:
        return bool(res[x][y//8]& 1<<(7-y%8))
    else:
        return False
s=set()

def fill(x,y):
    if get(x,y) and (x,y) not in s:
        s.add((x,y))
        for d in [1,-1]:
            fill(x+d,y)
            fill(x,y+d)
        
n=0
for i in range(128):
    for j in range(128):
        if get(i,j) and (i,j) not in s:
            fill(i,j)
            n+=1

#print([get(2,y) for y in range(8)])
