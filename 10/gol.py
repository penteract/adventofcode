from collections import defaultdict
d=defaultdict(int,{0:1})
for x in (l:=sorted([int(x) for x in open("input")])):
    d[x]=d[x-1]+d[x-2]+d[x-3]
print(d[l[-1]])
    
