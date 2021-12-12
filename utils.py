from collections import defaultdict

# screen coords, north "up" is negative

compass={"N" : -1j,
    "E" : 1,
    "S" : 1j,
    "W" : -1
    }
invcompass = {(-0-1j): 'N', 1: 'E', 1j: 'S', -1: 'W'} #{v:k for k,v in compass.items()}
arrowvec = {'^': (-0-1j), '>': 1, 'v': 1j, '<': -1}#{a:compass[b] for a,b in zip("^>v<","NESW")}


def invd(d):
    return {v:k for k,v in d.items()}

def bfs(neighbs,init):
    try:
        frontier=list(init)
    except e:
        frontier=[init]
    seen=set(frontier)
    i=0
    while i<len(frontier):
        x=frontier[i]
        for k in neighbs(x):
            if k not in seen:
                frontier.append(k)
                seen.add(k)
        i+=1

compass={"N" : -1j,
    "E" : 1,
    "S" : 1j,
    "W" : -1
    }
def n4(x):
    return [x+v for v in compass.values()]

def n8(x):
    return [x+v*k for v in compass.values() for k in [1,1+1j]]


def ufdsget(x,st):
    k = st[x]
    if k==x:
        return x
    else:
        k=ufdsget(k,st)
        st[x]=k
        return k

def ufdsjoin(x,y,st):
    st[ufdsget(x,st)]=ufdsget(y,st)
