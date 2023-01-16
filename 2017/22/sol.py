import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"
f=[line.strip() for line in open(fname)]

from collections import defaultdict

d=defaultdict(lambda : ".")
xs=[0]


dy=-1

for y,line in enumerate(f):
    for x,c in enumerate(line):
        d[y,x]=c

y = len(f)//2
x = len(f[0])//2

dy=-1
dx=0

inf=0

for i in range(10000):
    if d[y,x]=="#":
        d[y,x]="."
        x,y=-y,x
    else:
        d[y,x]="#"
        x,y=y,-x
        inf+=1
    x+=dx
    y+=dy

print(sum(1 for k in d if d[k]=="#"))
print(inf)
    
#5339 too low
