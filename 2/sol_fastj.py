#from utils import *
import math

ranges_pre = [[int("3"*11+"2"),int("3"*11+"4")]] #mapl(ints_in, inp_readall().replace("\n", "").split(","))

# split ranges that cross a power of 10, e.g. 77-122 -> 77-99, 100-122
ranges = []
ranges_pre = iter(ranges_pre)

a,b = next(ranges_pre)
while True:
    assert a <=b, (a,b)
    if len(str(a)) == len(str(b)):
        ranges.append((a,b))
        try:
            a,b = next(ranges_pre)
        except StopIteration:
            break 
    else:
        mid = int(10**(len(str(a))))
        ranges.append((a, mid-1))
        a = mid 

def sum_multiples(n, a, b):
    """Sums the multiples of n in the range a-b (inclusive)"""
    base = (b+1-a)//n 
    extra = (b+1-a)%n + (a-1)%n+1 > n 
    
    num_multiples = base + extra 
    first_multiple = math.ceil(a/n)*n 

    # a + (a+n) + (a+2n) + (a+3n) + ... + (a+(k-1)n)
    # = ka + (0+n+2n+...+(k-1)n)
    # = ka + n(1+2+..+k-1)
    # = ka + nk(k-1)//2

    res = num_multiples*first_multiple + n*num_multiples*(num_multiples-1)//2
    #print(n,a,b,base,extra,num_multiples, first_multiple,res)
    return res
    

def reps(k, a, b):
    """
    Sums the ids in the range a-b with reps of groups of size k
    e.g. k=1 = multiples of 1111, k=2 = multiples of 0101
    """ 
    n = len(str(a))
    assert n == len(str(b))
    if k==0 or n%k != 0:
        return 0
    return sum_multiples(int(("0"*(k-1)+"1")*(n//k)), a, b)

def invalid1(a,b):
    return reps(len(str(a))//2, a,b)

def invalid2(a,b):
    """
    Sums the invalid ids in the range a-b
    """
    n = len(str(a))
    assert n == len(str(b))

    excl_counts = {}
    for k in range(n-1,0,-1):
        if n%k != 0:
            continue
        
        count = reps(k,a,b)
        
        # double-counting: 
        # for n=6, we have:
        #  k=3: mults of 001001
        #  k=2: mults of 010101
        #  k=1: mults of 111111, which are counted in both of above. to count these only once, add it to k=1 exc count, and subtract it from k=2 and k=3 exl count 

        # for n=8 we have:
        #   k = 4: mults of 00010001
        #   k = 2: mults of 01010101. already included
        #   k = 1: mults of 11111111. already included in k=2, but those that are in k=4 have already been removed from that group. thus we track removed multiples.

        cf=1
        for j,dat in excl_counts.items():
            #print(k,j,dat)
            if j%k == 0:
                #print("*")
                cf-=dat[1]
        excl_counts[k] = [count*cf,cf]

    #print(excl_counts)
    
    return sum(dat[0] for dat in excl_counts.values())


tot1 = 0 
tot2 = 0 
for a,b in ranges:
    tot1 += invalid1(a,b)
    tot2 += invalid2(a,b)

print("Part 1:", tot1)
print("Part 2:", tot2)  
        
