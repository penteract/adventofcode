from collections import defaultdict
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"

f=list(open(fname))

d=defaultdict(int)
compass={"N" : -1j,
    "E" : 1,
    "S" : 1j,
    "W" : -1
    }
def n4(x):
    return [x+v for v in compass.values()]

r=[]
for y,line in enumerate(f):
    #l=list(map(int,"".join(c if c in "1234567890-" else " " for c in line).split()))
    #r.append(l)
    for x,c in enumerate(line.strip()):
        d[(x+1j*y)]=int(c)

dd={}

xm = int(max(x.real for x in d))
ym = int(max(x.imag for x in d))
for k in d:
    for a in range(5):
        for b in range(5):
            dd[k+a*1*(xm+1)+(ym+1)*1j*b]= (d[k]+(a+b-1))%9+1
d=dd
xm = int(max(x.real for x in d))
ym = int(max(x.imag for x in d))
print(xm,ym)
seen = set()
pq = [[] for x in range(xm*ym*9)]
i=0
pq[d[xm+1j*ym]].append((xm+1j*ym,[]))

for y in range(5):
    print()
    for x in range(45):
        print(d[x+y*1j],end="")

while i<len(pq):
    for k,p in pq[i]:
        if k not in seen:
            #print(k)
            seen.add(k)
            for n in n4(k):
                if n in d:
                    assert d[n]>0
                    pq[i+d[n]].append((n,[k,p]))
            if k==0:
                while p:
                    print(p[0],d[p[0]],end="  ")
                    p=p[1]
                print(i-1)
                exit()
    i+=1
    #print(i)
        


#print(l)
