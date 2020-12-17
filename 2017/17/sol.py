from functools import *
from itertools import *
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)

f = open("input")
l=[int(x) for x in f][0]
d=defaultdict(int)

buf=[0]
k=0

##class Tree():
##    def __init__(self,val,right=None):
##        self.isBranch=False
##        self.val=val
##        self.count=1
##    def insertafter(self,n):
##        if self.isBranch(

a0=0
for i in range(1,50000001):
    k=((k+l)%i)+1
    if k==1:
        a0=i


print(a0)
    
