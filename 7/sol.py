from collections import defaultdict
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"

f=list(open(fname))

d=defaultdict(int)

r=[]
for y,line in enumerate(f):
    l=list(map(int,"".join(c if c in "1234567890-" else " " for c in line).split()))
    r.append(l)
print(l)
ll=[]
def f(x):
    return x*(x+1)//2
for a in range(max(l)):
    ll.append(0)
    ll[-1]+=(sum(f(abs(a-b)) for b in (l)))
print(min(ll))
