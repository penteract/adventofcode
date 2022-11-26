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
            
