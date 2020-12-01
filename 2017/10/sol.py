from functools import *
from itertools import *
from collections import defaultdict

f = open("input")
l=[x for x in f]
d=defaultdict(int)
#l = [int (x) for x in l]
#print(l)
#l=["1,2,3 "]


r=list(range(256))
p=0
s=0
#l=[int(x) for x in l[0].split(",")]
l=list(map(ord,l[0][:-1]))+[17, 31, 73, 47, 23]
print(l)
n=0
for i in range(64):
    for x in l:
        r=r[x:]+list(reversed(r[:x]))
        r=r[s:]+r[:s]
        n+=x+s
        s=(1+s)%256
k=256-n%256
r=r[k:]+r[:k]
for i in range(16):
    k=0
    for x in r[i*16:(i+1)*16]:
        k^=x
    print(hex(k)[2:].rjust(2,"0"),end="")
