from collections import defaultdict
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"

f=list(open(fname))

d=defaultdict(int)

r=[]
av = {'^': (-0-1j), '>': 1, 'v': 1j, '<': -1}

avv = {v:k for k,v in av.items()}

for y,line in enumerate(f):
    #=list(map(int,"".join(c if c in "1234567890-" else " " for c in line).split()))

    #r.append(l)
    for x,c in enumerate(line.strip()):
        d[(x+1j*y)]=av[c] if c in av else "."

#print(l)

arrowvec = {'^': (-0-1j), '>': 1, 'v': 1j, '<': -1}

i=0
stop=False

dd=list(d)
mx=max(a.real for a in dd)+1
my=max(a.imag for a in dd)+1
while not stop:
    #print(i)
    i+=1
    move=[]
    for k in dd:
        v=d[k]
        if v==1:
            if d[k+v]==".":
                move.append((k,k+v))
            elif d[k+v]==0 and d[k.imag*1j]==".":
                move.append((k,k.imag*1j))
    stop = not move
    for k,dst in move:
        d[k]="."
        d[dst]=1

        
    move=[]
    for k in dd:
        v=d[k]
        if v==1j:
            if d[k+v]==".":
                move.append((k,k+v))
            elif d[k+v]==0 and d[k.real]==".":
                move.append((k,k.real))
    stop = stop and not move
    for k,dst in move:
        d[k]="."
        d[dst]=1j
    kp=-1j
    """
    for k in dd:
        if k.imag!=kp.imag:
            print()
        kp=k
        print("." if d[k]=="." else avv[d[k]],end="")
    print()"""

print( i)
