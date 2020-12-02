from functools import *
from itertools import *
from collections import defaultdict

f = open("input")
l=[x for x in f]
d=defaultdict(int)
#r=list(map(int,l[0].split()))
l = [list(map(int,x.split(":"))) for x in l]

for n in range(100000000):
    for a,b in l:
        if (a+n)%(b*2-2)==0:
            break
    else:
        print(n)
        break

print(n)
