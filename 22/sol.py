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



#d = {}

#DS=10
#repeat=1

##lines="""deal with increment 7
##deal with increment 9
##cut -2""".split("\n")



opt = []
for line in lines:
    if line.startswith("cut"):
        n = int(line[4:])
        opt.append((n,n+1))
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
        
        opt.append((0,D[1]))
    elif line:
        assert line.startswith("deal into new stack")
        opt.append((DS-1,DS-2))
print(opt)

def f(fst,snd,n):
    """Where does n go when f(0)=fst and f(1)=snd?"""
    return (fst + (snd-fst)*n)%DS

#Turns out I didn't need this
#https://www.geeksforgeeks.org/modular-division/
def modInverse(b,m): 
    g = gcd(b, m)  
    if (g != 1): 
        # print("Inverse doesn't exist")  
        assert False
    else:  
        # If b and m are relatively prime,  
        # then modulo inverse is b^(m-2) mode m  
        return pow(b, m - 2, m)

def unf(fst,snd,r):
    """invert f(fst,snd)"""
    inv = modInverse((snd-fst)%DS,DS)
    return ((r-fst)*inv) % DS
def merge(p1,p2):
    x,y=p1
    z,w=p2
    return (f(x,y,z),f(x,y,w))
    

p  = (0,1)
for x in opt:
    p = merge(p,x)
print(p)

def iter(p,n):
    """(merge(p,_))^n((0,1))"""
    if n==0: return (0,1)
    if n==1: return p
    if n%2==0:
        return iter(merge(p,p),n//2)
    else:
        return merge(iter(merge(p,p),n//2),p)

p = iter(p, repeat)
#for x in opt[:repeat%len(opt)]:
#    p = merge(p,x)
print(p)
print(f(p[0],p[1],2020))

#wrong:
#87719080012285
#30787897520380

