from collections import defaultdict
import sys
import operator as op
#import sympy
fname=sys.argv[1] if len(sys.argv)>1 else "input"
from random import randrange
from functools import *

f=list(open(fname))

d=defaultdict(int)

r=[]

vs="wxyz"

d={v:0 for v in vs}
for y,line in enumerate(f):
    #l=list(map(int,"".join(c if c in "1234567890-" else " " for c in line).split()))
    i = line.split()
    if len(i)>2:
        if i[2] not in vs:
            #i[2]=int(i[2])
            d[i[2]]=int(i[2])
    r.append(i)
    #for x,c in enumerate(line.strip()):
    #    d[(x+1j*y)]=int(c)+1

print(r[-1])

print(len([x for x in r if x[0]=="inp"]))

f={
    "add":op.add,
    "mul":op.mul,
    "div":op.ifloordiv,
    "mod":op.imod,
    "eql":op.eq
    }

#[4, 6, 6, 3, 8, 4, 6, 7, 9, 9, 9, 9, 9, 9]
#5422502

#[2, 4, 7, 3, 8, 4, 6, 7, 9, 9, 9, 9, 9, 9]
#5422502

#[3, 5, 7, 3, 8, 4, 6, 7, 9, 9, 9, 9, 9, 9]
#5422502

#[4, 6, 7, 3, 8, 4, 6, 7, 9, 9, 9, 9, 9, 9]
#5422502

#[3, 5, 9, 3, 8, 4, 6, 7, 9, 9, 9, 9, 9, 9]
#5422502

def run(inp,i=0,z=0):
    inpt=iter([inp])
    d["z"]=z
    for ins in r[i*18:(i+1)*18]:
        if ins[0]=="inp":
            d[ins[1]]=next(inpt)
        else:
            d[ins[1]]=f[ins[0]](d[ins[1]],d[ins[2]])
    return d["z"]

@cache
def best(i,z):
    """given state z, at input i find the best 
"""
    if i==14:
        if z==0:
            return ""
        else:
            return None
    else:
        if z>26**(6 if i<=6 else 5):
            return None
        for inp in range(1,10):
            v = run(inp,i,z)
            rest = best(i+1,v)
            if rest is not None:
                return str(inp)+rest
    return None
"""
inps=[9]*14
while True:
    for i in range(1,14):
        if i==2:
            if inps[3]-1-3<1:
                inps[3]=1
            continue
        if inps[i]!=1:
            inps[i]-=1
            break
        else:
            inps[i]=9
    inps[0]=inps[1]-2
    inps[2]=inps[3]-3
    if inps[0]<1:
        continue
    print(inps)
    print(rn:=run(reversed(inps)))
    if not rn:
        print("".join(map(str,inps)))
        break
"""


"""
[7, 9, 3, 6, 6, 4, 9, 9, 9, 9, 9, 9, 9, 9]
208612
[6, 8, 3, 6, 6, 4, 9, 9, 9, 9, 9, 9, 9, 9]
208612
[5, 7, 3, 6, 6, 4, 9, 9, 9, 9, 9, 9, 9, 9]
8023
[4, 6, 3, 6, 6, 4, 9, 9, 9, 9, 9, 9, 9, 9]
208612
[3, 5, 3, 6, 6, 4, 9, 9, 9, 9, 9, 9, 9, 9]
208612
[2, 4, 3, 6, 6, 4, 9, 9, 9, 9, 9, 9, 9, 9]
208612
[1, 3, 3, 6, 6, 4, 9, 9, 9, 9, 9, 9, 9, 9]
208612




[7, 9, 2, 5, 6, 4, 9, 9, 9, 9, 9, 9, 9, 9]
208612
[6, 8, 2, 5, 6, 4, 9, 9, 9, 9, 9, 9, 9, 9]
208612
[5, 7, 2, 5, 6, 4, 9, 9, 9, 9, 9, 9, 9, 9]
8023
[4, 6, 2, 5, 6, 4, 9, 9, 9, 9, 9, 9, 9, 9]
208612
[3, 5, 2, 5, 6, 4, 9, 9, 9, 9, 9, 9, 9, 9]
208612
[2, 4, 2, 5, 6, 4, 9, 9, 9, 9, 9, 9, 9, 9]
208612
[1, 3, 2, 5, 6, 4, 9, 9, 9, 9, 9, 9, 9, 9]
208612

"""



