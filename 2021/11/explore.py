from collections import defaultdict
from random import choice
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"

f=list(open(fname))

d=defaultdict(int)

r=[]
for y,line in enumerate(f):
    #l=list(map(int,"".join(c if c in "1234567890-" else " " for c in line).split()))
    #r.append(l)
    for x,c in enumerate(line.strip()):
        d[(x+1j*y)]=int(c) #choice(range(10))#int(c)

#print(l)

compass={"N" : -1j,
    "E" : 1,
    "S" : 1j,
    "W" : -1
    }

def n8(x):
    return [x+v*k for v in compass.values() for k in [1,1+1j]]


dd=list(d)
print(dd)
def prgrid(d):
    for k in dd:
        print(d[k],end="")
        if k.real==9:
            print()
prgrid(d)
#cyclefinder={}
def fc(d):
    cyclefinder={}
    dd=list(d)
    ss=set(dd)
    tot=0
    for i in range(10**9):
        told=tot
        boost=[]
        for k in dd:
            d[k]+=1
            if d[k]==10:
                boost.append(k)
        for k in boost:
            if d[k]!=-1:
                d[k]=-1
                for q in n8(k):
                    if d[q]!=-1 and q in ss:
                        d[q]+=1
                        if d[q]>9:
                            boost.append(q)
        for k in dd:
            if d[k]==-1:
                tot+=1
                d[k]=0
        s="".join(chr(48+d[k]) for k in dd)
        if s in cyclefinder:
            #prgrid(d)
            return (cyclefinder[s],i,tot,s)
        else:
            cyclefinder[s]=(i,tot)

with open("cycles",mode="a") as ff:
    while True:
        d=defaultdict(int)
        for y,line in enumerate(f):
            for x,c in enumerate(line.strip()):
                d[(x+1j*y)]=choice(range(10))#int(c)
        (si,st),fi,ft,s = fc(d)
        k=fi-si
        if k!=10 and k%7 !=0:
            print(s)
            print()
        print(fi-si,ft-st,file=ff)
    
