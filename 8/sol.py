from functools import *
from itertools import *
from collections import defaultdict
print ("hi")


f = open("input")
l = list(f)
print(len(l))
print(len(l[0]))

dat = l[0][:-1]

x=0
lays=[]
while x<len(dat):
    lays.append(dat[x:x+25*6])
    x+=25*6
    print(x)

print("here")
print(min([(l.count("0"),l.count("1")*l.count("2")) for l in lays ]))

dd=["2" for i in range(25*6)]
for l in lays:
    for i,x in enumerate(l):
        if dd[i]=="2": dd[i]=x

for i in range(6):
    print("".join(dd[25*i:25*(i+1)]))

for i in range(6):
    print("".join(" " if c== "0" else "#" for c in dd[25*i:25*(i+1)]))
##d={"COM":[]}
##
##for a,b in inp:#b orbits a
##    if a not in d:
##        d[a]=[]
##    d[a].append(b)
##    if b not in d:
##        d[b]=[]
##
##def f(c,n=0):
##    tot=n
##    for x in d[c]:
##        tot += f(x,n+1)
##    return tot
##print (f("COM"))
##
##
##def dist(x,y):
##    if x==y:
##        return 0
##    return min([10000]+[1+dist(z,y) for z in d[x]])
##
##print(min(dist(x,"SAN")+dist(x,"YOU")-2 for x in d))



#lll = list(map(int,l[0].split(",")) )#+[0 for i in range(3850694)]
