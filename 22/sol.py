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

def intersect(a,b):
    return a[0]<=b[1] and b[0]<=a[1]
def s1(a,b):
    return (a[1]<=b[1] and b[0]<=a[0])
def s2(a,b):
    """a subsumes b"""
    return (a[0]<=b[0] and b[1]<=a[1])

def s3(a,b):
    return all(s2(*k) for k in zip(a,b))

def i3(a,b):
    return all(intersect(*k) for k in zip(a,b))


regs = []
count=0
i=len(r)
print(i)
"""
while i>0:
    i-=1
    k=i
    while k>0:
        k-=1
        if s3(r[i][1:],r[k][1:]):
            print(r[i][1:], r[k][1:])
            r.pop(k)
            i-=1"""
print(len(r))
def isn(a,b):
    return (max(a[0],b[0]),min(a[1],b[1]))
def isn3(x,y):
    return [isn(a,b) for a,b in zip(x,y)]

for i,ps in enumerate(r):
    s=ps[0]
    t=ps[1:]
    for sr,reg in regs[:len(regs)]:
        if i3(t,reg):
            regs.append((not sr,isn3(t,reg)))
    if s:
        regs.append((s,t))
    
        
#for i,ps in enumerate(r):
#    for ps2 in r[i:]:
#        #print(ps2)
#        count+=i3(ps[1:],ps2[1:])
print(len(regs))

for s,sz in regs:
    k=1
    for a,b in sz:
        k*=(b+1-a)
    count += k*(s*2-1)
print(count)
"""
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
                """
#print(arr.count(True))
#count+=1
#print(count)
