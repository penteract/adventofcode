import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"
f=[line[:-1] for line in open(fname)]

from collections import defaultdict

d=defaultdict(lambda : [])

try:
    xs = map(int,f)
except Exception:
    pass
try:
    xss = [list(map(int(xs.split(",")))) for xs in f]
except Exception:
    pass

s=0

ns = []

for line in f:
    if "[" in line:
        n=0
        while line:
            n+=1
            l=line[1]
            if l!=" ":
                d[n].append(l)
            line=line[4:]
    elif line.startswith(" 1"):
        for k in d:
            d[k].reverse()
    elif line.startswith("move"):
        ___,n,__,fr,_,to = line.split()
        n=int(n)
        f=int(fr)
        t=int(to)
        k=d[f][-n:]
        d[f][-n:]=[]
        for x in k:
            d[t].append(x)
s=""
for k in range(1,len(d)+1):
    print(k,d[k])
    s+=d[k][-1]
print(s)
