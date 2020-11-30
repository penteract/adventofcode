from functools import *
from itertools import *

f = open("input")
l = list(f)
#lll = list(map(int,l[0].split(",")) )#+[0 for i in range(3850694)]

r = []

for i in range(165432,707912):
    s=str(i)
    for w,x,y,z in zip("#"+s,s,s[1:],s[2:]+"#"):
        if x==y and x!=w and y!=z:
            break
    else:
        continue
    for x,y in zip(s,s[1:]):
        if x>y:
            break
    else:
        r.append(i)


print(len(r))


##7+2*1+2*3+5*2*2+
##5*3*4*n+
##4*5
##+5
##+5*5
##+2*2*2
##+v
##+1
##k=0
##while k<len(l):
##    if l[k]==l[k-(len(l)//2) ]:
##        tot+=int(l[k])
##    k+=

print(tot)
