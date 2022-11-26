from collections import defaultdict
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"

f=list(open(fname))

d=defaultdict(lambda :".")
f=iter(f)
r=[]
s=""
k=True
while k:
    k=next(f).strip()
    s+=k

for y,line in enumerate(f):
    #l=list(map(int,"".join(c if c in "1234567890-" else " " for c in line).split()))
    #r.append(l)
    for x,c in enumerate(line.strip()):
        d[(x+1j*y)]=c

print(len(s))
l=list(d)
swap=False
if s[0]=="#":
    swap=True

#d2=defaultdict(lambda :"#")

for i in range(50):
    xb  = [int(x.real) for x in d if d[x]=="#."[(swap*i)%2]]
    yb =  [int(x.imag) for x in d if d[x]=="#."[(swap*i)%2]]
    d2=defaultdict(lambda :".#"[(swap*i)%2])
    for y in range(min(yb)-1,max(yb)+2):
        for x in range(min(xb)-1,max(xb)+2):
            c=x+1j*y
            ss = "".join("".join(d[c+x+y] for x in [-1,0,1]) for y in [-1j,0,1j])
            sn = int(ss.replace("#","1").replace(".","0"),2)
            #print(int(sn,2))
            #print(sn)
            d2[c]=s[sn]
            #print(s[sn],end="")
        #print()
    d=d2
    #print()
print(len([int(x.real) for x in d if d[x]=="#"]))
