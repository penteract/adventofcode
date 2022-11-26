from collections import defaultdict
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"

f=list(open(fname))
def n4(x):
    return [x+v for v in compass.values()]
compass={"N" : -1j,
    "E" : 1,
    "S" : 1j,
    "W" : -1
    }



d=defaultdict(int)
for y,line in enumerate(f):
    #l=list(map(int,"".join(c if c in "1234567890-" else " " for c in line).split()))
    #r.append(l)
    for x,c in enumerate(line.strip()):
        d[(x+1j*y)]=int(c)+1

tot=0
ba={}
dd=list(d)
for k in list(d):
    ba[k]=k
##for k in list(d):
##    a=d[k]
##    print(k,a)
##    if a>0:
##        for b in n4(k):
##            print(b)
##            if d[b]!=0 and d[b]<=a:
##                break
##        else:
##            ba[k]=k


def get(x,st=ba):
    k = st[x]
    if k==x:
        return x
    else:
        k=get(k)
        st[x]=k
        return k

def ufdsjoin(x,y,st=ba):
    st[get(x)]=get(y)

for k in dd:
    a=d[k]
    if a>0 and a<10:
        for b in n4(k):
            #print(b)
            if d[b]!=0 and d[b]<=a:
                #print(b,k)
                ufdsjoin(b,k)

mxs=[]
for k in dd:
    if ba[k]==k:
        mxs.append(len([x for x in dd if get(x)==k]))
    #print(get(k))
mxs.sort()
print(mxs[-1]*mxs[-2]*mxs[-3])

