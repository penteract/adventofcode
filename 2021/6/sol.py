from collections import defaultdict
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"

f=list(open(fname))

d=defaultdict(int)

for y,line in enumerate(f):
    s = map(int,line.strip().split(","))
    break

s=list(s)
print(s)
cs={i:s.count(i) for i in range(9)}
for x in range(256):
    d={}
    for i in range(9):
        k=i-1 if i>0 else 6
        d[k]=cs[i]
        if i==0:
            d[8]=cs[0]
    d[6]=cs[7]+cs[0]
    cs=d

print(sum(cs.values()))
