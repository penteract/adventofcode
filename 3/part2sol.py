import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"
f=[line.strip() for line in open(fname)]

from collections import defaultdict

d=defaultdict(int)

try:
    xs = map(int,f)
except Exception:
    pass
try:
    xss = [list(map(int(xs.split(",")))) for xs in f]
except Exception:
    pass

xss=[]
s=0
for line in f:
    xs=[]
    for c in line:
        xs.append(ord(c)-65+27 if c<"a" else ord(c)-96)
    l=len(xs)//2
    p=((xs[:l],xs[l:]))
    s+= sum(set(p[0]).intersection(set(p[1])))
    xss.append(xs)
s=0
for a,b,c in zip(xss[::3],xss[1::3],xss[2::3]):
    s+=sum(set(a).intersection(set(b).intersection(set(c))))
print(s)
