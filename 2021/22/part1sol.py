from collections import defaultdict
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"

f=list(open(fname))

d=defaultdict(int)

r=[]
for y,line in enumerate(f):
    l=list(map(int,"".join(c if c in "1234567890-" else " " for c in line).split()))
    r.append(("on"in line, l[:2],l[2:4],l[4:]))
    #for x,c in enumerate(line.strip()):
    #    d[(x+1j*y)]=int(c)+1

print(r[-1])

arr=[False]*(2*10**6)

for st,(x1,x2),(y1,y2),(z1,z2) in r:
    x1=max(x1,-50)
    x2=min(x2,50)
    y1=max(y1,-50)
    y2=min(y2,50)
    z1=max(z1,-50)
    z2=min(z2,50)
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            for z in range(z1,z2+1):
                arr[x+50+(y+50)*101+(z+50)*10201]=st
print(arr.count(True))
