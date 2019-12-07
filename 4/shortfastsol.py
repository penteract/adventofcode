from math import comb

def c(k):
    f = lambda sz,n: comb(sz+n-1,n)-comb(sz,n)
    s = str(k)+"0"
    tot=0
    for i,p,c in zip(range(1,len(s)),s,s[1:]):
        if p>c:
            return tot+f(10-int(p),len(s)-i)
        tot += f(9-int(p),len(s)-i)
        if c==p:
            f = lambda sz,n: comb(sz+n-1,n)

print(c(165432)-c(707912+1))
