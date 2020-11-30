from functools import *
from itertools import *
from collections import defaultdict

f = open("input")
l = [int (x) for x in f]

p=0
n=0
while p<len(l):
    n+=1
    k=l[p]
    l[p]=k+1
    if k>=3:
         l[p]=k-1
    p+=k
print(n)



