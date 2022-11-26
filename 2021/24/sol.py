from collections import defaultdict
import sys
import operator as op
fname=sys.argv[1] if len(sys.argv)>1 else "input"
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



