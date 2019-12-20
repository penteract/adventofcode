def mkmap(xss):
    m={}
    for y,row in enumerate(xss):
        for x,c in enumerate(row):
            m[x,y]=c
    return m

def prmap(mapp):
    l = list(mapp.keys())
    m1=max(x for x,y in l)
    m2=min(x for x,y in l)
    m3=max(y for x,y in l)
    m4=min(y for x,y in l)
    for y in range(m4,m3+1):
        print("".join("#.@="[mapp[x,y]] if (x,y) in mapp else " " for x in range(m2,m1+1)))
    print(pos)


def ufdsget(st,x):
    k = st[x]
    if k==x:
        return x
    else:
        k=get(k)
        st[x]=k
        return k

def ufdsjoin(st,x,y):
    st[get(x)]=get(y)

def neighbs(p):
    """neighbours in a 2D grid"""
    x,y=p
    for dx in [1,-1]: yield (x+dx,y)
    for dy in [1,-1]: yield (x,y+dy)


def search(startpos,neighbs,end)
    fr = [(0,startpos)]
    seen = set()

    while fr:
        d,nxp = heappop(fr)
        for k in neighbs(nxp):
            if k not in seen:
                seen.add(k)
                heappush(fr,(d+1,k))
        if nxp==end:
            print("done",d,nxp)
