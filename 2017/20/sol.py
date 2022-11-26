from collections import defaultdict
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"

f=list(open(fname))

d=defaultdict(int)

r=[]
for y,line in enumerate(f):
    l=list(map(int,"".join(c if c in "1234567890-" else " " for c in line).split()))
    r.append((l[:3],l[3:6],l[6:]))
    #for x,c in enumerate(line.strip()):
    #    d[(x+1j*y)]=int(c)+1

print(r[-1])

def sign(x):
    if x==0:
        return 0
    return x/abs(x)

flag = True
while flag:#loop until signs of each component agree
    flag=False
    for p,v,a in r:
        for i in range(3):
            v[i]+=a[i]
            p[i]+=v[i]
        if not all(sign(p[i])==sign(v[i])==sign(a[i]) for i in range(3)):
            flag=True

l = [(d,c,b,a) for a,(b,c,d) in enumerate(r)]
l.sort()
print (l[0])
    
