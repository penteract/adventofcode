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
def prgrid(d):
    for y in range(int(min(x.imag for x in d)),  int(max(x.imag for x in d ))+1):
        print()
        for x in range(int(min(x.real for x in d)),int(max(x.real for x in d )+1)):
            print("#" if y*1j+x in d else " ",end="")

from heapq import *

def dj(start,pths,done=None):
    """
Djikstra's algorithm. given an initial vertex and a function from nodes to lists of neighbours with distances,
return a dictionary of shortest paths from the initial vertex.
"""
    seen=set()
    pq = [(0,start)]
    results={}
    while pq:
        k,x = heappop(pq)
        results[x]=k
        if done and done(x):
            return results
        if x not in seen:
            seen.add(x)
            for d,y in pths(x):
                if y not in seen:
                    heappush(pq,(k+d,y))
    return results
            
    
