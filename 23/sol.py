from functools import *
from itertools import *
import operator as op
from collections import defaultdict
import re
import sys
sys.setrecursionlimit(1000)
def mint(ns):
    return list(map(int,ns))

ds = [(0,1),(0,-1),(1,0),(-1,0)]

f = open("input")
#f=iter(["389125467 "])

l=[int(x) for x in next(f)[:-1]] +list(range(10,1000001))
##class Tree():
##    def __init__(self,lch,rch=None,parent=None):
##        self.parent=parent
##        self.val=None
##        self.rch=rch
##        if isinstance(lch,list):
##            #print(len(lch))
##            if len(lch)==1:
##                self.val=lch[0]
##                known[self.val]=self
##            else:
##                a = len(lch)//2
##                self.lch = Tree(lch[:a])
##                self.rch = Tree(lch[a:])
##                self.lch.parent=self
##                self.rch.parent=self
##        else:
##            if rch is None:
##                self.val=lch
##                known[self.val]=self
##            else:
##                self.lch=lch
##                self.rch=rch
##                self.lch.parent=self
##                self.rch.parent=self
##    def popNext(self):
##        n=self.getNext()
##        print(n.val)
##        p=n.parent
##        oth = p.rch if p.lch is n else p.lch
##        global root
##        if p is root:
##            root=oth
##        else:
##            oth.parent=p.parent
##            if p.parent.lch is p:
##                p.parent.lch=oth
##            elif p.parent.rch is p:
##                p.parent.rch=oth
##            else:
##                print(n.val)
##                raise Exception("err")
##        return n
##    def getNext(self):
##        while self is self.parent.rch:
##            self=self.parent
##            if self is root:
##                out=self.lch
##                break
##        else:
##            out=self.parent.rch
##        while out.val is None:
##            out=out.lch
##        return out
##    def insertBefore(self,a,b,c):
##        p=self.parent
##        oth=Tree(Tree(a,b),Tree(c,self),parent=self.parent)
##        if p.lch is self:
##            p.lch=oth
##        elif p.rch is self:
##            p.rch=oth
##    def __str__(self):
##        if self.val: return str(self.val)
##        else:
##            return "("+str(self.lch)+str(self.rch)+")"

class LL():
    def __init__(self,val,nx):
        self.val=val
        self.next=nx
        known[self.val]=self
    def popNext(self):
        n=self.next
        self.next=n.next
        return n
    def insertAfter(self,a,c):
        c.next=self.next
        self.next=a
    def __str__(self):
        e=self
        s=str(self.val)
        while e.next is not self:
            e=e.next
            s+=" "+str(e.val)
        return s

MAX=max(l)
known={}
prev=None
rt=LL(l.pop(),None)
root=rt
while l:
    root=LL(l.pop(),root)
rt.next=root
#print(root)

x=known[1]

for aa in range(10000000):
    if aa%100000==0:print(aa)
    #print("".join([str(x) for x in l]))
    #print(x)
    r=[]
    for j in range(3):
        r.append(x.popNext())
    j=x.val-1
    if j==0: j=MAX
    while j in [k.val for k in r]:
        j-=1
        if j==0: j=MAX
    #print(j)
    known[j].insertAfter(r[0],r[2])
    x=x.next

#l=[(x:=x.getNext()).val for i in range(len(l))]

#print("".join([str(x) for x in l]))
#i=l.index(1)
#print(l[i],l[i+1],l[i+2])
