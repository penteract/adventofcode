from collections import defaultdict
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"

f=list(open(fname))

d=defaultdict(int)

r=[]

ps = [c for c in zip(f[2],f[3]) if c[0] in "ABCD"]

homes = tuple(map(tuple,zip(*ps)))
print(homes)

"""for y,line in enumerate(f):
    l=list(map(int,"".join(c if c in "1234567890-" else " " for c in line).split()))
    r.append(l)
    #for x,c in enumerate(line.strip()):
    #    d[(x+1j*y)]=int(c)+1"""

#print(l)

from heapq import *

def dj(start,pths,done):
    """
Djikstra's algorithm. given an initial vertex and a function from nodes to lists of neighbours with distances,
return a dictionary of shortest paths from the initial vertex.
"""
    seen=set()
    pq = [(0,start)]
    results={}
    while pq:
        k,x = heappop(pq)
        if x not in seen:
            seen.add(x)
            #print(k)
            results[x]=k
            if done(x):
                return x,results[x]
            for d,y in pths(x):
                if y not in seen:
                    dd=k+d
                    heappush(pq,((dd),y))
    return results

cor=tuple("." for i in range(7))

def setat(t,i,y):
    return tuple(x if j!=i else y for j,x in enumerate(t))


def setat2(t,i,j,y):
    return setat(t,i,setat(t[i],j,y))

def iterleft(i,cor):
    for j in range(i+1,0,-1):
        if cor[j] != ".":
            return
        yield ((2*i+2)-(2*j-1) ,j)
    if cor[0] != ".":
        return
    yield (2*i+2,0)
def iterright(i,cor):
    for j in range(i+2,6):
        if cor[j] != ".":
            return
        yield (2*j-1-(2*i+2) ,j)
    if cor[6] != ".":
        return
    yield (10-2*i-2,6)


def mkset(a):
    return set(a[0][0]+a[0][1]+a[1])

def iterleft1(i,cor):
    for j in range(i+1,0,-1):
        if cor[j] != ".":
            return ((2*i+2)-(2*j-1) ,j)
    if cor[0] != ".":
        return (2*i+2,0)
def iterright1(i,cor):
    for j in range(i+2,6):
        if cor[j] != ".":
            return (2*j-1-(2*i+2) ,j)
    if cor[6] != ".":
        return (10-2*i-2,6)
def opts(st):
    homes,cor=st
    #leaving rooms
    for i in range(4):
        k=1
        if (l:=homes[0][i]) == ".":
            if thing:=iterleft1(i,cor):
                d,hor = thing
                l=cor[hor]
                if l=="ABCD"[i]==homes[1][i]:
                    mul = 10**(ord(l)-ord("A"))
                    res = (setat2(homes,k-1,i,cor[hor]) , setat(cor,hor,"."))
                    yield ((d+k)*mul, res)
            if thing:=iterright1(i,cor):
                d,hor = thing
                l=cor[hor]
                if l=="ABCD"[i]==homes[1][i]:
                    mul = 10**(ord(l)-ord("A"))
                    res = (setat2(homes,k-1,i,cor[hor]) , setat(cor,hor,"."))
                    yield ((d+k)*mul, res)
            k+=1
            if (l:=homes[1][i])  == ".":
                if thing:=iterleft1(i,cor):
                    d,hor = thing
                    l=cor[hor]
                    if l=="ABCD"[i]:
                        mul = 10**(ord(l)-ord("A"))
                        res = (setat2(homes,k-1,i,cor[hor]) , setat(cor,hor,"."))
                        yield ((d+k)*mul, res)
                if thing:=iterright1(i,cor):
                    d,hor = thing
                    l=cor[hor]
                    if l=="ABCD"[i]:
                        mul = 10**(ord(l)-ord("A"))
                        res = (setat2(homes,k-1,i,cor[hor]) , setat(cor,hor,"."))
                        yield ((d+k)*mul, res)
                continue
        mul = 10**(ord(l)-ord("A"))
        #moving left
        for d,hor in iterleft(i,cor):
            res = (setat2(homes,k-1,i,".") , setat(cor,hor,l))
            yield ((d+k)*mul, res)
        #moving right
        for d,hor in iterright(i,cor):
            res = (setat2(homes,k-1,i,".") , setat(cor,hor,l))
            yield ((d+k)*mul, res)

def h(p):
    homes,cor=p
    for i,c in enumerate(p):
        mul = 10**(ord(c)-ord("A"))
        

t=("A","B","C","D")
r = dj((homes,cor),opts,lambda x: x[0]==(t,t))
print(r)
