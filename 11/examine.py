from collections import defaultdict
counts=defaultdict(int)
knownpairs=defaultdict(list)
with open("cycles") as f:
    for line in f:
        p,t=map(int,line.split())
        counts[p,t]+=1
        if t not in knownpairs[p]:
            knownpairs[p].append(t)

l=list(counts)
print(max(l))
