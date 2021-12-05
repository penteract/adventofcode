from collections import defaultdict
d=defaultdict(int)
ff=list(open("input"))

f=iter(ff)

inp=[int(k) for k in (next(f).split(","))]

bs=[]
for a,line in enumerate(f):
    if len(line)<4:
        bs.append([])
    else:
        bs[-1].append(list(map(int,line.split())))

def f():
    s=set()
    for a in inp:
        for i in range(len(bs)):
            if i not in s:
                for x in range(5):
                      for y in range(5):
                          if bs[i][x][y]==a:
                              bs[i][x][y]=-a-1
        for i in range(len(bs)):
            if i not in s:
                for x in range(5):
                    if all(bs[i][x][y]<0 for y in range(5)):
                           l= (a,i)
                           s.add(i)
                           
                for y in range(5):
                    if all(bs[i][x][y]<0 for x in range(5)):
                           l= (a,i)
                           s.add(i)
                if all(bs[i][k][k]<0 for k in range(5)):
                    l= (a,i)
                    s.add(i)
                if all(bs[i][k][4-k]<0 for k in range(5)):
                    l= (a,i)
                    s.add(i)
    return l

a,i=f()
print(a*sum([k for k in sum(bs[i],[]) if k>0]))
