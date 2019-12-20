f = open("input")

pts=[]
for line in f:
    pts.append(tuple(map(int,line.split(","))))

print(len(pts))
ufds = {x:x for x in pts}

def mdist(a,b):
    return sum(abs (x-y) for x,y in zip(a,b))

def get(p):
    r = ufds[p]
    if p==r:
        return p
    else:
        k = get(r)
        ufds[p]=k
        return k

def join(p,q):
    ufds[get(q)]=get(p)

for p in pts:
    for q in pts:
        if mdist(p,q)<=3:
            join(p,q)

s = set()
for p in pts:
    s.add(get(p))
print(len(s))
