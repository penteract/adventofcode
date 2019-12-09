from functools import *
from itertools import *
from collections import defaultdict

f = open("input")
contents = list(f)
print(len(contents))
head = contents[0]
print(len(contents[0]))

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


