from collections import defaultdict
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input2"

f=list(open(fname))

d=defaultdict(int)

r=[]
for y,line in enumerate(f):
    #l=list(map(int,"".join(c if c in "1234567890-" else " " for c in line).split()))
    l=[[]]
    for c in line:
        if c=="[":
            l.append([])
        elif c in "1234567890":
            l[-1].append(int(c))
        elif c=="]":
            l[-2].append(l.pop())
    r.append(l[0][0])
    #for x,c in enumerate(line.strip()):
    #    d[(x+1j*y)]=int(c)+1

print(l[0][0])

def addTo(n,v,lr,expand=True):
    """add v to the left or right of n"""
    if isinstance(n[lr],int):
        n[lr]+=v
        if n[lr]>9 and expand:
            v=n[lr]
            n[lr]=[(v)//2, (v+1)//2]
    else:
        addTo(n[lr],v,lr,expand)

def addTo1(n,v,lr,expand=True):
    if v!=0:
        #print(n,v,lr)
        if isinstance(n[1-lr],int):
            n[1-lr]+=v
            if n[1-lr]>9 and expand:
                v = n[1-lr]
                n[1-lr] = [(v)//2, (v+1)//2]
        else:
            addTo(n[1-lr],v,lr,expand)

def explode(n,d=0):
    if isinstance(n,int):
        return (None,n)
    elif d>3 and isinstance(n[0],int) and isinstance(n[1],int) :
        return ((n[0],n[1]),0)
    else:
        b,v=explode(n[0],d+1)
        if b is True:
            return (True,[v,n[1]])
        elif b is not None:
            addTo1(n,b[1],0,False)
            return ((b[0],0),[v,n[1]])
        else:
            v0=v
            b,v=explode(n[1],d+1)
            n=[v0,v]
            if b is True:
                return (True,n)
            elif b is not None:
                addTo1(n,b[0],1,False)
                return ((0,b[1]),n)
            else:
                return (None,n)
def split(n):
    if isinstance(n,int):
        if n>9:
            return (True,[(n)//2, (n+1)//2])
        return (None,n)
    else:
        k,v = split(n[0])
        if k:
            return (k,[v,n[1]])
        else:
            k,v = split(n[1])
            return (k,[n[0],v])

i=0
def add(k,x):
    k=[k,x]
    while True:
        a,k=explode(k)
        #print(k)
        if a is None:
            a,k=split(k)
            if not a:
                return magnitude(k)

def magnitude(n):
    if isinstance(n,int):
        return n
    else:
        return 3*magnitude(n[0])+2*magnitude(n[1])

mx=0
print(len(r))
import copy
d=copy.deepcopy
for a in range(len(r)):
    for b in range(a+1,len(r)):
        mx=max([mx,add(d(r[a]),d(r[b])),add(d(r[b]),d(r[a]))])
print(mx)
