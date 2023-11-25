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
    #xss = [list(map(int(xs.split(",")))) for xs in f]
    #xss=[]
    pass
except Exception:
    pass

s=0
n=0
line=f[0]
while len(set(line[:14]))!=14:
        line=line[1:]
        n+=1
print(n+14)
