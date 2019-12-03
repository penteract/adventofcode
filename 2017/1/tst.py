from functools import *
from itertools import *

f = open("input")
l = list(f)[0].strip()
#l="1111"
tot = 0


k=0
while k<len(l):
    if l[k]==l[k-(len(l)//2) ]:
        tot+=int(l[k])
    k+=1

print(tot)
