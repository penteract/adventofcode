from collections import defaultdict
d=defaultdict(int)
f=list(open("input"))

l=list(f)
for a in range(13):
    if(len(l)==1):
        print("0b"+l[0])
        break
    d=defaultdict(int)
    for line in l:
        s = line.strip()
        d[s[a]]+=1
    k=("0" if d["0"]>d["1"] else "1")
    l=[x for  x in l if x[a]==k]
l=list(f)
for a in range(13):
    if(len(l)==1):
        print("0b"+l[0])
        break
    d=defaultdict(int)
    for line in l:
        s = line.strip()
        d[s[a]]+=1
    k=("1" if d["0"]>d["1"] else "0")
    l=[x for  x in l if x[a]==k]
    

print(("0b"+ss))
