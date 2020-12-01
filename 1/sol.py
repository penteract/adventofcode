from functools import *
from itertools import *
from collections import defaultdict

f = open("input")
l=list(f)
l = [int (x) for x in l]
print(l)
n=0
#d=defaultdict(int)

s=set()


for x in l:
    for y in l:
        if 2020-x-y in s:
            print(x*y*(2020-x-y))
    s.add(x)

