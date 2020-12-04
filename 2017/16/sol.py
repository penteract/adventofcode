from functools import *
from itertools import *
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)

f = open("input")
l=[x for x in f]
d=defaultdict(int)
#r=list(map(int,l[0].split()))
#l=["s1,x3/4,pe/b"]
l = l[0].split(",")

p = [chr(x) for x in range(ord("a"),ord("p")+1)]
#p=list("abcde")
print("".join(p))
d={"".join(p):0}
aa=0
for i in range(2000):
    for ins in l:
        if ins[0]=="s":
            n=int(ins[1:])
            p=p[-n:]+p[:-n]
        elif ins[0]=="x":
            a,b=list(map(int,ins[1:].split("/")))
            x=p[a]
            p[a]=p[b]
            p[b]=x
        elif ins[0]=="p":
            x,y = ins[1:].split("/")
            a=p.index(x)
            b=p.index(y)
            x=p[a]
            p[a]=p[b]
            p[b]=x
        else:
            print(ins)
    k=("".join(p))
    if k in d:
        print(k)
        break
    aa+=1
    d[k]=aa

perm = [ord(x)-ord("a") for x in "dcmlhejnifpokgba"]

def ap(l,p):
    return [l[i] for i in p]

def apply(prm,n):
    if n==1: return prm
    if n%2:
        return ap(apply(prm,n-1),prm)
    else:
        return apply(ap(prm,prm),n//2)

def disp(s):
    return ("".join(chr(n+ord("a")) for n in s))

disp(apply(perm,10**9))

#wrong:
#jlmenhdafcbkgoip doing x wrong (moving from the front)
#pmbdaelhgonkjcif still doing x wrong

#wrong pt2
#dcmljghfinpokeba (permutation nonsense)
#legnajicfkmdobph (adding 1 after break statement)
