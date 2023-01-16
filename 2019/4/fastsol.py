from functools import *
from itertools import *


bounds = (165432,707912)

def fac(n):
    if n<=1: return 1
    return n*fac(n-1)

def ncr(n,r):
    """n Choose r"""
    if r<0 or r>n: return 0
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

@lru_cache(None)
def nodup(sz,n):
    """how many length n strictly increasing sequences are there?"""
    if sz < n: return 0
    if sz==n or n==0: return 1
    return (nodup(sz-1,n) + # lowest digit is not used
            nodup(sz-1,n-1)) # lowest digit is used

def nd(sz,n):
    return ncr(sz,n)

for i in range(1,10):
    for j in range(1,10):
        assert nd(i,j)==nodup(i,j)


def withdup(sz,n):
    """how many length n nondecreasing sequences are there with a repeated value"""
    return ci(sz,n) - nd(sz,n)

def withinit(init,n,sz=9):
    """How many length `n` sequences are there beginning with `init` (part 1 conditions)"""
    if init=="":
        return withdup(sz,n) # sum(withinit(str(dig),n,sz) for dig in range(1,1+sz))
    matched = any([a==b for a,b in zip(init,init[1:])])
    l = init[-1]
    available = sz+1-int(l)
    lenleft = n-len(init)
    if matched:
        return ci(available,lenleft)
    else:
        return (ci(available,lenleft - 1)+ #next digit is l
                 withdup(available - 1,lenleft) )# next digit is not l (double counts some cases)



def countFrom(k):
    """How many numbers greaer than or equal to k with the same number of digits as k are allowed?"""
    # example 133501:
    # withdup(10-2,6) (2xxxxx,3xxxxx..9xxxxx)
    # +withdup(10-4,5) (14xxxx,15xxxx,..,19xxxx)
    # +withdup(10-4,4) (134xxx,135xxx,..139xxx)
    # +ci(10-5,3) (1335xx,1336xx,..1339xx)
    # example 1200:
    # withdup(10-2,4)
    # +withdup(10-2,3)
    
    f = withdup
    s = str(k)
    n = len(s)
    tot=0
    for i in range(1,len(s)):
        if s[i-1]>s[i]:
            tot += f(10-int(s[i-1]),n-(i-1))
            break
        tot += f(9-int(s[i-1]),n-(i-1))
        if s[i]==s[i-1]:
            f = ci
    else: # last digit should be dealt with
        tot+= f((10-int(s[-1])) ,1)
    return tot

assert withdup(9,2) == 9
assert withdup(2,3) == 4
assert withdup(3,3) == 3*2 + 3
print(withdup(3,4))#1123#1223#1233#1112#1122#1222#
assert withdup(3,4) == 3 + 3*3 + 3
print(withdup(2,3))

print (countFrom(90))
assert countFrom(90)==1

print (countFrom(bounds[0]) - countFrom(bounds[1]+1))
