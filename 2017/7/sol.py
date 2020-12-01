from functools import *
from itertools import *
from collections import defaultdict

f = open("input")
l=list(f)
#l = [int (x) for x in l]
#print(l)

d=defaultdict(int)

for line in l:
    ns=line.split()
    d[ns[0]]=(eval(ns[1]),[x.strip(",")for x in ns[3:]])
    #for x in ns[3:]:
    #    d[x.strip(",")]-=1



base = "azqje"
def f(k):
    w,ch = d[k]
    cws = [f(c) for c in ch]
    a=[c[0] for c in cws]
    if len(set(a))>1:
        print(cws)
    return (sum(a)+w,w)
f(base)
