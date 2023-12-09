def minCRT(a,b,s1,s2):
    """find the minimum n s.t. n%a in s1 and n%b in s2, assuming a and b are coprime"""
    if len(s1)==0 or len(s2)==0: return None
    if (len(s1)>(a-2) or len(s2)>a-2) or len(s1)*len(s2)>(a*b)/2:#just brute force (TODO: prove that the last check is sufficient to make things fast)
        s1=set(s1)
        s2=set(s2)
        for n in range(a*b):
            if n%a in s1 and n%b in s2:
                return n
    #for each k in s2 find x s.t. a*x == k (mod b)
    ainv = pow(a,-1,b)
    col0 = [((ainv*k)%b) for k in s2] # considering an a*b grid with the numbers 0 to a*b, this gives the rows where the first column contains numbers that are in s2 mod b
    for x,k in zip(col0,s2):
        assert (x*a)%b == k
    
    col0.sort()
    binv = pow(b,-1,a)
    mn = a*b#running minimum
    for col in s1:
        # find what offset to add to 0 to move it to column col
           # find m s.t. b*m == col (mod a) )
        m = ((col*binv)%a)
        assert (b*m)%a == col
        rowOffset = m*b // a
        assert (rowOffset*a+col)%b == 0
        # binary search for the decreasing step in the list [(x+rowOffset)%b for x in col0] (consider it to be cyclic)
        if (col0[-1]+rowOffset)%b > (col0[0]+rowOffset)%b:
            mn = min(mn,((col0[0]+rowOffset)%b)*a + col)
            continue
        hi=len(col0)-1
        lo=0
        while hi!=lo+1:
            # invariant: f(hi)<f(lo) where f(x) = (col0[x]+rowOffset) % b
            mid = (hi+lo)//2
            if (col0[mid]+rowOffset)%b < (col0[lo]+rowOffset)%b:
                hi=mid
            else:
                lo=mid
        mn = min(mn,((col0[hi]+rowOffset)%b)*a + col)
    assert mn!=a*b
    return mn
assert minCRT(9,7,[0,4,6],[6,2,5])==6

def naiveMinCRT(a,b,s1,s2):
    """find the minimum n s.t. n%a in s1 and n%b in s2, assuming a and b are coprime"""
    s1=set(s1)
    s2=set(s2)
    for n in range(a*b):
        if n%a in s1 and n%b in s2:
            return n

def test(mx=100000, n=100,seed=100):
    import math
    import random
    import timeit
    random.seed(seed)
    for i in range(n):
        a=10
        b=10
        while math.gcd(a,b)>1:
            a=random.randint(1,mx)#TODO: consider a different distribution. expovariate?
            b=random.randint(1,mx)
        s1,s2 = [random.sample(range(x),random.choice([random.randint(0,x),random.randint(0,x**0.5//1),random.randint(0,x**0.25//1)])) for x in [a,b]]
        scrt=minCRT
        x=None
        try:
            t = timeit.timeit("global z; z=scrt(a,b,s1,s2)",globals=locals(),number=1)
            print(f"time: {t:.6f}, {len(s1):6} of {a:6},{len(s2):6} of {b:6})" )
            x = locals()["z"] # don't do this; z=locals()["z"] doesn't work
            #x = minCRT(a,b,s1,s2)
            y = naiveMinCRT(a,b,s1,s2)
            if x!=y:
                raise Exception("Test failed, naive gave ",y,"; minCRT gave ",x)
        except Exception as e:
            print("s1:",s1)
            print("s2:",s2)
            print("a,b,len(s1),len(s2)",a,b,len(s1),len(s2))
            raise e
    print("All tests passed (probably)")
