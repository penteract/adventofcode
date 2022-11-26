from collections import defaultdict
from itertools import *
d=defaultdict(int)
f=list(open("input"))

def r(x1,x2):
    """iterator of integers from x1 to x2 """
    if x1==x2:
        return [x1]
    d = int((x2-x1)/abs(x1-x2))
    return range(x1,x2+d,d)

for y,line in enumerate(f):
    s = line.strip()
    a,b = line.split("->")
    x1,y1 = map(int,a.split(","))
    x2,y2 = map(int,b.split(","))
    xs = r(x1,x2)
    ys = r(y1,y2)
    if abs(x1-x2)>abs(y1-y2):
        ys=cycle(ys)
    else:
        xs=cycle(xs)
    for a,b in zip(xs,ys):
        d[a,b]+=1

print (len([k for k in d if d[k]>1]))
