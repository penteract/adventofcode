tot = 0
r = open("input")
l = list (r)
print (l)
from  collections import defaultdict

g = defaultdict(int)
k=0
def ch(x,y):
    global t
    t+=1
    if abs(x)+y!=0:
        if (x,y) in g and g[x,y][0]!=k:
            outs.append((x,y,t+g[x,y][1]))
        if (x,y) not in g:
            g[x,y]=(k,t)

outs = []

for r in l:
    x=0
    t=0
    y=0
    k+=1
    for d in r.split(","):
        dr=d[0]
        dist = int(d[1:])
        if dr=="R":
            while dist>0:
                x+=1
                ch(x,y)
                dist-=1
        if dr=="L":
            while dist>0:
                x-=1
                ch(x,y)
                dist-=1
        if dr=="U":
            while dist>0:
                y+=1
                ch(x,y)
                dist-=1
        if dr=="D":
            while dist>0:
                y-=1
                ch(x,y)
                dist-=1


print(outs)
print (min(z for x,y,z in outs))
print(outs)
print(outs)

