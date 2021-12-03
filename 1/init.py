from collections import defaultdict
f=open("input")
f=list(f)
t=2021

d=defaultdict(int)
tot=0
xs=[]


for line in f:
    l = line.split()
    #v+=int(l[0])
    #tot+=v
    #xs.append(int(l[0]))
    for k in l:
        try:
            x=int(k)
            print(int(k))
            tot+=x
        except e:
            pass

print(tot)
