from collections import defaultdict
from itertools import *
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"

f=list(open(fname))

d=defaultdict(int)

r=[]
for y,line in enumerate(f):
    
    if "scanner" in line:
        r.append([])
    else:
        l=list(map(int,"".join(c if c in "1234567890-" else " " for c in line).split()))
        if len(l)==3:
            r[-1].append(tuple(l))
    #r.append(l)
    #for x,c in enumerate(line.strip()):
    #    d[(x+1j*y)]=int(c)+1

print([len(l) for l in r])
            
def rots(pts):
    res=[]
    for p in permutations([0,1,2]):
        ii = [i for i in p if i!=p[i]]
        ks = [[],[0,1],[0,2],[1,2]] if len(ii)!=2 else [[0],[1],[2],[0,1,2]]
        #ks = [[],[0,1],[0,2],[1,2]]
        for k in ks:
            l=[]
            for pt in pts:
                l.append(tuple(pt[p[i]]*(-1 if i in k else 1) for i in range(3)))
            res.append(l)
    return res

#for a in rots(r[0]):
#    print( a)

s0=r[0]

def diff(a,b):
    return tuple(a[i]-b[i] for i in range(3))
def addd(a,b):
    return tuple(a[i]+b[i] for i in range(3))


found=[(0,(0,0,0),s0)]
for i,dell,sn in found:
    for ax,l in enumerate(r):
        if ax not in [f[0] for f in found]:
            for a in rots(l):
                d=defaultdict(list)
                for i,x in enumerate(sn):
                    for j,y in enumerate(a):
                        d[diff(x,y)].append((i,j))
                for k in d:
                    if len(d[k])>=12:
                        print(d[k])
                        found.append((ax,k,[addd(y,k) for y in a]))
                        break
                else: continue
                break
s=set()
mx=0
def m(tri):
    return sum(abs(x) for x in tri)
for a,b,k in found:
    s=s.union(set(k))
    for aa,bb,kk in found:
        mx=max([mx,m(diff(b,bb))])
print(len(s))
print(mx)
#print(found[1])
