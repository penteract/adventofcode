from collections import defaultdict
d=defaultdict(int)
f=list(open("input"))

for y,line in enumerate(f):
    s = line.strip()
    a,b=line.split("->")
    x,y=map(int,a.split(","))
    x2,y2=map(int,b.split(","))
    #print(x,y,x2,y2)
    if x==x2:
        for a in range(min(y,y2),max(y,y2)+1):
            d[x,a]+=1
    elif y==y2:
        for a in range(min(x,x2),max(x,x2)+1):
            d[a,y]+=1
    elif abs(x-x2)==abs(y-y2):
        for a,b in zip(range(x,x2+int((x2-x)/abs(x-x2)),int((x2-x)/abs(x-x2))),range(y,y2+int((y2-y)/abs(y-y2)),int((y2-y)/abs(y-y2)))):
            d[a,b]+=1

print (len([k for k in d if d[k]>1]))
