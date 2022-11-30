import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"
f=list(open(fname))

sf = list(open("input1"))
sof = list(open("output1-1"))
sampleout = int(sof[0])
print("hi")
import sympy
import operator as op
from itertools import *
vrs = list(map(sympy.var, (chr(n) for n in range(65,65+26))))
def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    # Recipe credited to George Sakkis
    num_active = len(iterables)
    nexts = cycle(iter(it).__next__ for it in iterables)
    while num_active:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            # Remove the iterator we just exhausted from the cycle.
            num_active -= 1
            nexts = cycle(islice(nexts, num_active))
def merge(gen):
    """generate all elements from an iterator of iterators
    results from later iterables are exponentially rarer"""
    try:
        first = iter(next(iter(gen)))
    except StopIteration:
        pass
    else:
        try:
            yield next(first)
        except StopIteration:
            for a in merge(gen):
                yield a
        else:
            for x in roundrobin(merge(gen),first):
                yield x

ops = [op.add,op.mul,op.floordiv]

def mktrees(n):
    if n==0:
        yield None
    else:
        for i in range(n):
            for l in mktrees(i):
                for r in mktrees(n-i-1):
                    for op in ops:
                        yield (op,i,l,r)

def evalTree(t,vrs):
    if t is None:
        return vrs[0]
    else:
        (op,i,l,r)=t
        return op(evalTree(l,vrs[:i+1]),evalTree(r,vrs[i+1:]))

def treeToExprs(t,n,seenbefore=set()):
    vs = vrs[:n+1]
    for k in permutations(vs):
        e = evalTree(t,k)
        s = str(e)
        if s not in seenbefore:
            seenbefore.add(s)
            yield (t,k,e)

def mkList(start):
    l=len(start)
    def inner(n):
        if n<l:
            return start[n]
        else:
            k = (n-l)*2+4
            if(k%3)==0:
                return (k//-6)
            else:
                return k//3
    return inner



def generateSubs(n,j,fn,offset=0,prefix=()):
    #print("gs",n,j,offset)
    if n==0: yield prefix
    elif n==1:#this would be covered by the other case, but could involve too much recursion
        if j==1:
            yield prefix+(fn(offset),)
        else:
            for i in count(offset):
                #print("aa",i)
                yield prefix+(fn(i),)
    else:
        assert n>=j
        for s in merge(
            generateSubs(ii,j-1,fn,offset+1,prefix+(fn(offset),)*(n-ii)) # important to capture prefix
                for ii in range(max(0,j-1),(n if j>0 else n+1))
            ):
            #print("bb",n,j,offset,s)
            yield s
        """print("h1",i)
            for s in generateSubs(i,j-1,fn,offset+1):
                print("h2",s)
                yield (fn(offset),)*(n-i) + s"""

def genExprs(i,caches={},sb=set()):
    if i not in caches:
        caches[i]=[]
    cache=caches[i]
    for x in cache:
        yield x
    for t in mktrees(i-1):
        for x in treeToExprs(t,i-1,sb):
            cache.append(x)
            yield x
    

def genExprSubs1():
    def cross(i):
        fn = mkList([X])
        sb=set()
        for s in generateSubs(i,1,fn):
            #print("ge",s,i)
            for x in genExprs(i):
                #print(x[2],s)
                yield x[2].subs(zip(vrs,s))
    return merge(cross(i) for i in count(1))

def genExprSubs2():
    def cross(i):
        fn = mkList([X,Y])
        sb=set()
        for s in generateSubs(i,2,fn):
            #print("ge",s,i)
            for x in genExprs(i):
                #print(x[2],s)
                yield x[2].subs(zip(vrs,s))
    return merge(cross(i) for i in count(2))
#import timeit
#print(timeit.timeit("l = genExprSubs1();[next(l) for i in range(10)]",number=10,globals=globals()))

allowable_fractions = {1.0,2.0,3.0,4.0,0.5,-1.0,-2.0,-3.0,-0.5}
print("hello")

try:
    l = list(map(int,sf))
except ValueError:
    pass
else:
    e1 = genExprSubs1()
    e2 = genExprSubs2()
    l2 = zip(l,l[1:])
    i=0
    while True:
        print(i)
        i+=1
        e = next(e1)
        print(e)
        try:
            s = sum(int(e.subs(X,x)) for x in l)
            r = sampleout/(s if s!=0 else 1)
            if r in allowable_fractions:
                l = list(map(int,f))
                s = sum(int(e.subs(X,x)) for x in l)
                print(s*r)
                break
        except Exception:
            pass
        e=next(e2)
        print(e)
        try:
            s = sum(int(e.subs(zip([X,Y],p))) for p in l2)
            r = sampleout/(s if s!=0 else 1)
            if r in allowable_fractions:
                l = list(map(int,f))
                s = sum(int(e.subs(zip([X,Y],p))) for p in l2)
                print(s*r)
                break
        except Exception:
            pass

