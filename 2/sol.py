from utils import *
#print (arrowvec)
f=open("input")

f=[r.strip().split() for r in f] # list(f)

x=0
y=0
aim=0
for r in f:
    #print(r)
    dx,dy=compass[r[0]]
    x+=dx*int(r[1])
    aim+=dy*int(r[1])
    y+=aim*dx*int(r[1])

print(x*y)
    
