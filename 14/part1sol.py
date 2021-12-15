from collections import defaultdict
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"

f=list(open(fname))

d={} #defaultdict(int)

r=[]
for y,line in enumerate(f):
    if "-" in line:
        a,b=map(lambda x:x.strip("> \n&gt;"), line.split("-"))
        d[a]=b

k = f[0].strip()
ik=k
for i in range(10):
    o=[k[0]]
    for a,b in zip(k,k[1:]):
        s=a+b
        if s in d:
            o.append(d[s])
        o.append(b)
    k="".join(o)
    print(k)

mx=0
mn=10**10
for c in set(k):
    a=k.count(c)
    if a>mx:
        mx=a
    if a<mn:
        mn=a
    
        
print(mx,mn,mx-mn)
