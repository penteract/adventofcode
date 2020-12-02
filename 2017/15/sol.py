from functools import *
from itertools import *
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)

f = open("input")
l=[x for x in f]
d=defaultdict(int)
#r=list(map(int,l[0].split()))

A=16807
B=48271
N=2147483647

a=289
b=629

n=0

for i in range(5000000):
    a=(a*A)%N
    while a&3:
        a=(a*A)%N
    b=(B*b)%N
    while b&7:
        b=(B*b)%N
    if (a^b)&((1<<16) - 1)==0:
        n+=1
print(n)

