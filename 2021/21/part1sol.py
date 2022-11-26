from collections import defaultdict
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"

f=list(open(fname))

d=defaultdict(int)

r=[]
for y,line in enumerate(f):
    l=list(map(int,"".join(c if c in "1234567890-" else " " for c in line).split()))
    r.append(l)
    #for x,c in enumerate(line.strip()):
    #    d[(x+1j*y)]=int(c)+1

print(l)
            
a=r[0][1]
b=r[1][1]
r=[a,b]
print(a,b)

def d():
    while True:
        for i in range(1,101):
            yield i
ss=[0,0]
i=1
y=d()
rn=0
while max(ss)<1000:
    i=(i+1)%2
    v = sum(next(y) for j in range(3))
    #print(v)
    rn+=3
    #print(r)
    r[i]=(r[i]+v-1)%10 + 1
    #print(r)
    ss[i]+=r[i]
    #print(r,ss)
print(r,ss,rn,i)
print(ss[1-i]*rn)
