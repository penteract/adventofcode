import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"
f=[line.strip() for line in open(fname)]

from collections import defaultdict

d=defaultdict(int)

try:
    xs = list(map(int,f))
except Exception:
    pass
try:
    xss = [list(map(int(xs.split(",")))) for xs in f]
except Exception:
    pass

s=0
for line in f:
    op,re=line.split(",")
    a=list(map(int,op.split("-")))
    b=list(map(int,re.split("-")))
    if (a[0]<=b[0] and a[1]>=b[0]) or (a[0]>=b[0] and a[0]<=b[1]):
        #print(a,b)
        s+=1
print(s)
