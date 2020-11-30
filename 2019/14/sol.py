from functools import *
from itertools import *
from collections import defaultdict
from math import gcd,atan2
from string import *

lcm = lambda x,y: x*y//gcd(x,y)

f = open("input")
#contents = list(f)
dat = []
res = {}
for line in f:
    if line:
        ins,out = line.split("=>")
        ins = [e.strip().split(" ") for e in ins.split(",")]
        out = out.strip().split(" ")
        ins = [(int(x),y ) for x,y in ins ]
        a,b = int(out[0]),out[1]
        dat.append((ins,a,b))
        assert b not in res
        res[b]=(a,ins)

for k in res:
    print(k, res[k])

needed = {k:0 for k in res}
def get(n):
    needed = {k:0 for k in res} # did not have this when I gave my answer. that was a bug which fortunately did not matter.
    needed["FUEL"]=n
    needed["ORE"]=0


    while any(needed[k]>0 for k in needed if k != "ORE"):
        for k in needed:
            if needed[k]>0 and k!="ORE":
                a,ins = res[k]
                num = (needed[k]+a-1)//a
                needed[k]-=num*a
                for x,y in ins:
                    needed[y]+=x*num
    return (needed["ORE"])


l=100

r=100000000

while (r-l>1):
    m=(r+l)//2
    if get(m)<10**12:
        l=m
    else:
        r=m

print(l,r,get(l),get(r))
print(list(get(n) for n in range(10)))



def justgetints(line):
    line+="\n"
    i=0
    res=[]
    while i<len(line):
        if (line[i]=="-" and line[i+1] in digits) or line[i] in digits:
            j=i+1
            while line[j] in digits: j+=1
            res.append(int(line[i:j]))
            i=j-1
        i+=1
    return res
        


print()
