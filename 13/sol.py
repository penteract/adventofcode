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
    return -abs(z.real)+1j*z.imag

for c,a in r:
    if c=="x":
        k=1
    else:
        k=1j
    d={k*(f(x/k-a)+a) for x in d}

print(d)
print(len(d))

#My solution at the time of submission was worse than this - it used hardcoded constansts that were far too big (based on a previous incorrect output, and I widened my terminal until it worked)
for y in range(int(min(x.imag for x in d)),  int(max(x.imag for x in d ))+1):
	print()
	for x in range(int(min(x.real for x in d)),int(max(x.real for x in d )+1)):
		print("#" if y*1j+x in d else " ",end="")
