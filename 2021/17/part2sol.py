from collections import defaultdict
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"

f=list(open(fname))

d=defaultdict(int)

r=[]
for y,line in enumerate(f):
    l=list(map(int,"".join(c if c in "1234567890-" else " " for c in line).split()))
    xa,xb,ya,yb=l
    break
    #r.append(l)
    #for x,c in enumerate(line.strip()):
    #    d[(x+1j*y)]=int(c)+1
print(l)
print(ya*(ya+1)//2)
n=0
print((int(xa**0.5),xb+1),(ya,abs(ya)))
for dx in range(int(xa**0.5),xb+1):
    idx=dx
    for dy in range(ya,abs(ya)):
        dx=idx
        idy=dy
        x=0
        y=0
        while x<=xb and y>=ya:
            x+=dx
            y+=dy
            if idx==6 and idy==-1:
                print(x,y)
            dx=0 if dx==0 else dx-1
            dy-=1
            if xa<=x<=xb and ya<=y<=yb:
                print(idx,idy)
                n+=1
                break

print(n)
            
