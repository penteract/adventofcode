from functools import *
from itertools import *
from collections import defaultdict

f = open("input")
l=[x.split("if") for x in f]
#l = [int (x) for x in l]
#print(l)

d=defaultdict(int)
m=0
for a,b in l:
    if eval(b,d):
        k=a.replace("inc","+=")
        k=k.replace("dec","-=")
        exec(k,d)
    m=max(m,max([v for v in d.values() if isinstance(v,int)]))
print(m)
