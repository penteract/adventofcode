from functools import *
from itertools import *

f = open("input")
l = list(f)
ll = [list(map(int,s.split("\t")) )for s in l]


tot = 0

for k in ll:
    for i,x in enumerate(k):
        for j,y in enumerate(k):
            if j!=i:
                r=x//y
                if r*y==x:
                    tot +=r
                    break
        else:
            continue
        break
    else:
        print(k,"bug")


##k=0
##while k<len(l):
##    if l[k]==l[k-(len(l)//2) ]:
##        tot+=int(l[k])
##    k+=

print(tot)
