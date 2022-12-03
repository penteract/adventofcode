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

s=0
for line in f:
    op,re=line.split()
    op = ord(op)-65
    r = ord(re)-ord("X")
    r = (op+r+2)%3
    s+=r+1+((op==r)+2*(r==(op+1)%3))*3
print(s)
