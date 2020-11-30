from functools import *
from itertools import *
from collections import defaultdict
from math import gcd,atan2
from string import *

lcm = lambda x,y: x*y//gcd(x,y)

f = open("input")

x = f.read()
L = (len(x)-1)
K = L*10000
D = int(x[:7])

assert D>K/2
assert D<K

mod = D%L
div = (K-D)//L

l = list(map(int,x[:-1]))
ll = l[mod:] + l*div
assert len(ll)+D==K

ll.reverse()
for j in range(100):
    nx=[]
    t=0
    for i in ll:
        t+=i
        t%=10
        nx.append(t)
    ll=nx
    print(j)

#5979187

print("".join(map(str,list(reversed(ll))[:8])))
#for i in range(100):
#    print(i,"".join(map(str,l[i*22:(i+1)*22])))
#59522422
