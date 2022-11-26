from collections import defaultdict
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"

f=list(open(fname))

d=defaultdict(list)
#d={}

r=[]
for line in (f):
    a,b=line.split("-")
    b=b.strip()
    d[a].append(b)
    d[b].append(a)

l=list(d)

print(l)


s=defaultdict(int)
s["start"]=1
def cp(n,k=True):
    print(n,"(")
    s[n]+=1
    if n=="end":
        #if k:
        #    tot=1
        #    k=False
        #else:
            s[n]-=1
        #    print(")")
            return 1
    else:
        tot=0
    for x in d[n]:
        if (k and s[x.lower()]<=1) or s[x.lower()]<=0 or x=="end":
            tot+=cp(x,k and s[x.lower()]<=0)
    s[n]-=1
    print(")")
    return tot

print(cp("start"))
