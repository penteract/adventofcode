from functools import *
from itertools import *


bounds = (165432,707912)

def fac(n):
    if n<=1: return 1
    return n*fac(n-1)

def ncr(n,r):
    return fac(n)//fac(r)//fac(n-r)

@lru_cache(None)
def countinc(sz, n):
    """count the number of length n nondecreasing sequences over the values 1..sz"""
    #how many ways can sz slots be filled so that there are n total items?
    if sz==1 or n==0:
        return 1
    return (countinc(sz-1,n) + # either there is no item in the first slot (no occurences of the lowest digit available)
              countinc(sz,n-1)) # or there is at least 1

#After writing that out, it's obviously Pascal's triangle
#This is actually probably slower due to not caching :)
def ci(sz,n):
    return ncr(sz+n-1,n)

for i in range(1,10):
    for j in range(1,10):
        assert ci(i,j)==countinc(i,j)



def withinit(init,n,sz=9):
    """How many length `n` sequences are there beginning with `init` (part 1 conditions)"""
    if init=="":
        return sum(withinit(str(dig),n,sz) for dig in range(1,1+sz))
    matched = any([a==b for a,b in zip(init,init[1:])])
    l = init[-1]
    available = sz+1-int(l)
    lenleft = n-len(init)
    if matched:
        return ci(available,lenleft)
    else:
        return (ci(available,lenleft - 1)+ #next digit is l
                 ci(available -1,lenleft - 1)*(lenleft-1) -  # nextdigit
