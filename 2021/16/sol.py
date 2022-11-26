from collections import defaultdict
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"

f=list(open(fname))

d=defaultdict(int)

r=[]
for y,line in enumerate(f):
    #line="C200B40A82"
    n = bin(int(line,base=16))[2:].rjust(4*len(line.strip()),"0")
    break
    #l=list(map(int,"".join(c if c in "1234567890-" else " " for c in line).split()))
    #r.append(l)
    #for x,c in enumerate(line.strip()):
    #    d[(x+1j*y)]=int(c)+1

i=0

def b(x):
    return int(x,base=2)
    
def prod(ns):
    x=1
    for k in ns:
        x*=k
    return x

f={
    "000":sum,
    "001":prod,
    "010":min,
    "011":max,
    "101":lambda x:x[0]>x[1],#gt
    "110":lambda x:x[0]<x[1],#gt
    "111":lambda x:x[0]==x[1],#gt
    }

tot=0
def p(i):
    ii=i
    v=n[i:i+3]
    t=n[i+3:i+6]
    i+=6
    if i>len(n):
        return None
    if t=="100":
        val=0
        while n[i]!="0":
            val*=16
            val+=b(n[i+1:i+5])
            i+=5
        val*=16
        val+=b(n[i+1:i+5])
        i+=5
        print(n[ii:i])
        print(val)
        return val,i
    else:
        I=n[i]
        i+=1
        ch=[]
        if I=="0":
            k=i+15+b(n[i:i+15])
            i+=15
            while i<k:
                vv,i=p(i)
                ch.append(vv)
        else:
            k=b(n[i:i+11])
            i+=11
            for h in range(k):
                vv,i=p(i)
                ch.append(vv)
    print(n[ii:i])
    print(t,ch)
    return f[t](ch),i

i=0

print(p(0))
#while (k:=p(i)) is not None:
#    tot+=k[0]
#    i=k[1]

#print(n)
#print(tot)
