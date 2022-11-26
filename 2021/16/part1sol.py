from collections import defaultdict
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"

f=list(open(fname))

d=defaultdict(int)

r=[]
for y,line in enumerate(f):
    #line="620080001611562C8802118E34"
    n = bin(int(line,base=16))[2:].rjust(4*len(line.strip()),"0")
    break
    #l=list(map(int,"".join(c if c in "1234567890-" else " " for c in line).split()))
    #r.append(l)
    #for x,c in enumerate(line.strip()):
    #    d[(x+1j*y)]=int(c)+1

i=0

def b(x):
    return int(x,base=2)
    

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
            val+=b(n[i:i+4])
            i+=5
        val*=16
        val+=b(n[i:i+4])
        i+=5
    else:
        I=n[i]
        i+=1
        if I=="0":
            i+=15
        else:
            i+=11
    print(n[ii:i])
    return b(v),i

i=0
while (k:=p(i)) is not None:
    tot+=k[0]
    i=k[1]

#print(n)
print(tot)
