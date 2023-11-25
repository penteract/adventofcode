# slightly slower than sol.py on the sample input, but morally superior - O(n*log(n)) rather than O(n*n)

import re
from typing import Tuple, Callable, Iterable, Optional
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"
f = open(fname)
ftext=f.read()
f=[line.strip() for line in ftext.split("\n")[:-1]]

from collections import defaultdict

d=defaultdict(int)

#copied from https://github.com/joefarebrother/adventofcode/blob/master/misc_utils.py
def lmap(f: Callable, *xs) -> list:
    """Like map but returns a list"""
    return list(map(f, *xs))

def ints(xs: Iterable) -> list[int]:
    """Casts each element of xs to an int"""
    return lmap(int, xs)

def mint(x, default=None):
    """Maybe int - casts to int and returns default on failure"""
    try:
        return int(x)
    except ValueError:
        return default

def ints_in(x: str) -> list[int]:
    """Finds and parses all integers in the string x"""
    ex = r'(?:(?<!\d)-)?\d+'
    return ints(re.findall(ex, x))


class Skip():
    def __init__(self,v):
        self.v = v
        self.links = []
        self.backlinks = []
    def _init_link(self,ln,target):
        self.links.append((ln,target))
        target.backlinks.append((ln,self))
    def __getitem__(self,i):
        if i==0:
            return self
        elif i>0:
            for (ln,nd) in self.links:
                if ln>i:
                    break
                else:
                    l=(ln,nd)
            return l[1][i-l[0]]
        elif i<0:
            for (ln,nd) in self.backlinks:
                if ln<i:
                    break
                else:
                    l=(ln,nd)
            return l[1][i-l[0]]
        raise Exception("Bad integer")
    def shift(self,n):# move the current node n spaces forward
        if n==0:#remember to make the node with value 0 the front node
            return
        assert self.links[0][0]==1
        nx = self.links[0][1]
        self.remove()
        newsucc = nx[n]
        f,lf=newsucc,0
        for j in range(len(self.links)):
            dlf,f = f.getf(j)
            lf+=dlf
            self.links[j]=(lf+1,f)
            lb,b = f.backlinks[j]
            f.backlinks[j] = (lf+1,self)
            self.backlinks[j]=(lb-lf,b)
            b.links[j] = (lb-lf,self)
        for j in range(len(self.links),maxlinks):
            _,f = f.getf(j)
            k,b = f.backlinks[j]
            f.backlinks[j] = (k+1,b)
            b.links[j] = (k+1,f)
        #insertbefore.insertBefore(self)
        
    def remove(self):
        for (n,((lf,f),(lb,b))) in enumerate(zip(self.links,self.backlinks)):
            f.backlinks[n] = (lf+lb-1,b)
            b.links[n] = (lf+lb-1,f)
        i = len(self.links)
        f=self
        for j in range(i,maxlinks):
            _,f = f.getf(j)
            k,b = f.backlinks[j]
            f.backlinks[j] = (k-1,b)
            b.links[j] = (k-1,f)
            
    def getf(self,j):
        if j<len(self.links):
            return (0,self)
        else:
            ln,f = self.links[-1]
            k,r = f.getf(j)
            return (ln+k,r)
xs = ints(f)
xs = [811589153*k for k in xs]

offset = xs.index(0)

nodes = lmap(Skip,xs)
nds = nodes[offset:]+nodes[:offset]
l = len(nds)

#build skiplist from nds
maxlinks = len(bin(len(nds)))-2

for j in range(maxlinks):
    dst = 1<<j
    for h in range(0,len(nds), dst):
        if dst+h>=len(nds):
            dst=len(nds)-h
        nds[h]._init_link(dst, nds[(h+dst)%len(nds)])




for kk in range(10):
    for k in nodes:
        k.shift(k.v%(l-1))
#print(l)   

s=0
for i in range(1000,4000,1000):
    a = nds[0][i].v
    s+=a

print(s)











