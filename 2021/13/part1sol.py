from collections import defaultdict
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"

f=list(open(fname))

d=defaultdict(int)


r=[]
for y,line in enumerate(f):
    if "," in line:
        x,y=list(map(int,"".join(c if c in "1234567890-" else " " for c in line).split()))
        d[x+1j*y]="#"
    elif "fold" in line:
        dr = line[len("fold along ")]
        c = int(line[len("fold along x="):])
        r.append((dr,c))
    #for x,c in enumerate(line.strip()):
    #    d[(x+1j*y)]=int(c)+1

def f(z):
    return abs(z.real)+1j*z.imag

for c,a in r[:1]:
    if c=="x":
        k=1
    else:
        k=1j
    d={k*(f(x/k-a)+a) for x in d}

print(d)
print(len(d))
