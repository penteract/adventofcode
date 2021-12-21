from collections import defaultdict
import sys
from functools import lru_cache
fname=sys.argv[1] if len(sys.argv)>1 else "input"

f=list(open(fname))

d=defaultdict(int)

r=[]
for y,line in enumerate(f):
    l=list(map(int,"".join(c if c in "1234567890-" else " " for c in line).split()))
    r.append(l)
    #for x,c in enumerate(line.strip()):
    #    d[(x+1j*y)]=int(c)+1

print(l)
            
a=r[0][1]
b=r[1][1]
r=[a,b]
print(a,b)

def d():
    while True:
        for i in range(1,101):
            yield i
ss=[0,0]
#i=1
y=d()
rn=0

@lru_cache(None)
def count(r1,r2,s1,s2,i):
    sst = (s1,s2)
    rrt =(r1,r2)
    #print(rr,ss,i)
    counts=[0,0]
    for r in [3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 9]: #[(3,1),(4,3),(5,6),(6,7),(7,4),(8,3),(9,1)]:
        c=1
        rr,ss=map(list,(rrt,sst))
        rr[i] = (rr[i]+r-1)%10+1
        ss[i]+=rr[i]
        #print(ss)
        if max(ss)>=21:
            counts[i]+=c
        else:
            res=count(*rr,*ss,(i+1)%2)
            counts[0]+=res[0]*c
            counts[1]+=res[1]*c
    return tuple(counts)
"""
while max(ss)<1000:
    i=(i+1)%2
    v = sum(next(y) for j in range(3))
    #print(v)
    rn+=3
    #print(r)
    r[i]=(r[i]+v-1)%10 + 1
    #print(r)
    ss[i]+=r[i]
    #print(r,ss)
print(r,ss,rn,i)
print(ss[1-i]*rn)"""
res=count(*r,0,0,0)
print(res)
print(max(res))
