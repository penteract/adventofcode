from heapq import *
def ast(start,neighbs,done,h = lambda x:0):
    """Finds the node n such that done(n) with minimal distance from an element of start.
    neighbs(n) = [(nn,edgeweight)]
    assumes h(n)<d(n,end)
    Returns the path as a lisp-style deeply nested tuple"""
    seen=set()
    hq = []
    for x in start:
        heappush(hq,(h(x),(x,None),0))
    while hq:
        c,pth,d = heappop(hq)
        n=pth[0]
        if n not in seen:
            #print(n)
            seen.add(n)
            if done(n):
                return (pth,d)
            for x,dst in neighbs(n):
                if x not in seen:
                    heappush(hq,(d+dst+h(n),(x,pth),d+dst))
def prgrid(d):
    xs = set(k[0] for k in d)
    ys = set(k[1] for k in d)
    for y in range(min(ys),max(s)+1):
        for x in range(min(xs),max(xs)+1):
            k=x,y
            print(d[k] if d[k]!=0 else ".",end="")
        print()

def flatten(tup):
    l=[]
    while tup is not None:
        l.append(tup[0])
        tup=tup[1]
    return l
def collback(n):
    yield (n*2,1)
    k=(n//3)
    if k*3+1 == n: yield (k,1)
import math
print(ast([1],collback,lambda x:x==7,lambda x:abs(math.log2(x))//2))
