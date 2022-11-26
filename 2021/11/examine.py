from collections import defaultdict
counts=defaultdict(int)
knownpairs=defaultdict(list)
with open("cycles") as f:
    for line in f:
        p,t=map(int,line.split())
        if p!=10 and p%7:
            print(p)
        counts[p,t]+=1
        if t not in knownpairs[p]:
            knownpairs[p].append(t)

kp2 = {k:sum(counts[k,a] for a in v) for k,v in knownpairs.items()}
l=list(counts)
print(max(l))
