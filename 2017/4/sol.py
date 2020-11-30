from functools import *
from itertools import *
from collections import defaultdict

f = open("input")
l = list(f)
n=0
for p in l:
    s=p.split()
    if len(s)==len(set(map((lambda a:"".join(sorted(a))),s))):
        n+=1

print(n)
