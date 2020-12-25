from functools import *
from itertools import *
import operator as op
from collections import defaultdict
import re
#import sys
#sys.setrecursionlimit(1000)
def mint(ns):
    return list(map(int,ns))

ds = [(0,1),(0,-1),(1,0),(-1,0)]

m={"n":(0,1),"s":(0,-1),"w":(2,0),"e":(-2,0)}

f = open("input")

l = [int(x.strip()) for x in f]
#l = [mint(x.split(",")) for x in f]
d=defaultdict(int)

ck,dk=l
md=20201227

i7=pow(7,md-2,md)
print((ck*dk*i7)%md)






