from collections import defaultdict
from random import choice
import sys
import time
fname=sys.argv[1] if len(sys.argv)>1 else "input"
s = "9781111300071111130004111116540311116328331111522803111152220521114233004338835060900760802500009894"
f=list(open(fname))

d=defaultdict(int)

r=[]
"""
for y,line in enumerate(f):
    #l=list(map(int,"".join(c if c in "1234567890-" else " " for c in line).split()))
    #r.append(l)
    for x,c in enumerate(line.strip()): """
s="""024
676
400"""
lines=s.split()
w=len(lines)
h=len(lines[0])
for y in range(w):
    for x in range(h):
        d[(x+1j*y)]= ord(lines[y][x])-48  #int(c) #choice(range(10))#int(c)

#print(l)

compass={"N" : -1j,
    "E" : 1,
    "S" : 1j,
    "W" : -1
    }

def n8(x):
    return [x+v*k for v in compass.values() for k in [1,1+1j]]


dd=list(d)
#print(dd)
def prgrid(d):
    for k in dd:
        print(d[k],end="")
        if k.real==9:
            print()
#prgrid(d)
#cyclefinder={}

def draw(d):
    cyclefinder={}
    dd=list(d)
    ss=set(dd)
    tot=0
    found=False
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
        s="\n".join("".join(" ▁▂▃▄▅▆▇█▒"[d[k]] for k in dd[j::h]) for j in range(h))
        print(s)
        print()
        time.sleep(0.1)

        if not found:
            if s in cyclefinder:
                #prgrid(d)
                oi,otot = cyclefinder[s]
                print(oi,i-oi,tot-otot)
                input("cycle found")
                found=True
            else:
                cyclefinder[s]=(i,tot)

draw(d)
