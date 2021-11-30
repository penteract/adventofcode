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

val=1
sn=7
for i in count():
    val=(val*sn)%20201227
    if val==ck:
        print(i,"card")
        cpk=i
        break
    elif val==dk:
        print(i)
        dpk=i
        aa=val

sn=val
val=1
for j in range(dpk+1):
    val=(val*sn)%20201227

print(val)
val=1
sn=dk
for j in range(cpk+1):
    val=(val*sn)%20201227
print(val)
