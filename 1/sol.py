from collections import defaultdict
f=open("input")
f=list(f)
t=2021

d=defaultdict(int)
tot=0
xs=[]

p=10**9
for line in f:
    xs.append(int(line))


for a,b,c in zip(xs,xs[1:],xs[2:]):
    v=a+b+c
    if(v>p):
        tot+=1
    p=v
print(tot)
