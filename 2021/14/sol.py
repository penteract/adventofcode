from collections import defaultdict
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"

f=list(open(fname))

d={} #defaultdict(int)

r=[]
for y,line in enumerate(f):
    if "-" in line:
        a,b=map(lambda x:x.strip("> \n&gt;"), line.split("-"))
        d[a]=b

k = f[0].strip()
dd=defaultdict(int)
for a,b in zip(k,k[1:]):
    s=a+b
    dd[s]+=1
    #if s in d:
    #    o.append(d[s])
    #o.append(b)
#k="".join(o)
#print(k)

mx=0
mn=10**10

def prs(dd):
    d2=defaultdict(int)
    for k in dd:
        c=d[k]
        d2[k[0]+c]+=dd[k]
        d2[c+k[1]]+=dd[k]
    return d2
for i in range(40):
    dd=prs(dd)
    counts=defaultdict(int)
    for cc in dd:
        counts[cc[0]]+=dd[cc]
        counts[cc[1]]+=dd[cc]
    #print(dd)
    #print(counts)
    
    



counts[k[0]]+=1
counts[k[-1]]+=1
print(counts)
print((max(counts.values())-min(counts.values()))//2)
