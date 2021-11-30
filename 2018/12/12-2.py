from collections import defaultdict
import operator as op
d=defaultdict(int)

f=open("input")
init = next(f)[len("initial state:"):].strip()+"."*28
#print(init)
for l in f:
    if l.strip():
        k,v = map(lambda x:x.strip(), l.split("=>"))
        d[k]=v
s=init
start=0
K=20
i=0
print(f"{i:3}"+"."*(3+start)+s)
for n in range(K):
    i+=1
    s = "..."+s+"..."
    res=""
    for l in zip(*(s[i:] for i in range(5))):
        res+=d["".join(l)]
    s=res
    while s.startswith("."):
        start+=1
        s=s[1:]
    start-=1
    print(f"{i:3} "+"."*(3+start)+s)
tot=0
for (i,x) in enumerate(s):
    if x=="#":
        tot+=i+start
print(tot)

sgmts = {}
class Segment:
    def __new__(cls,left,right):
        if isinstance(left,str):
            assert len(left)==4
            assert len(right)==4
            key=left+right
        else:
            assert left.len==right.len
            key=(left.id,right.id)
            
        if key in sgmts:
            return sgmts[key]
        self=object.__new__(cls)
        self.id=len(sgmts)
        sgmts[key]=self
        self.left=left
        self.right=right
        if isinstance(left,str):
            self.mid=key[2:6]
            self.len=8
            self.body=key
            ss = [(c=="#") for c in key]
            self.count=sum(ss)
            self.score=sum(i for i,c in enumerate(ss) if c)
        else:
            self.mid = Segment(left.right,right.left)
            self.len=2*left.len
            self.count=left.count+right.count
            self.score=left.sc(0)+right.sc(left.len)
        self.nexts={}
        return self
    def sc(self,offset):
        return self.score+self.count*offset
    def expsteps(self,n):
        if n not in self.nexts:
            self.nexts[n]=self.es(n)
        return self.nexts[n]
    def es(self,n):
        """returns the segment corresponding to the central self.len/2 cells after 2**n steps"""
        #print(self.len,n)
        if 1<<(n+3)>self.len:
            raise Exception("Trying to run for too long")
        if self.len==8:
            assert n==0
            res=""
            for l in zip(*(self.body[i:] for i in range(5))):
                res+=d["".join(l)]
            return res
        else:
            l,m,r = [k.expsteps(max(0,n-1)) for k in [self.left,self.mid,self.right]]
            
            if n==0:
                if isinstance(l,str):
                    return S(l[2:]+m[:2],m[2:]+r[:2])
                return S(S(l.right,m.left),S(m.right,r.left))
            return S(*(k.expsteps(n-1) for k in (S(l,m),S(m,r))) )
    def __str__(self):
        if self.len==8:
            return self.body
        else:
            return str(self.left)+str(self.right)

S=Segment
print(len(init))
def empty(n):
    assert n>=4
    assert n<(1<<100)
    if n==4:
        return "...."
    else:
        e=empty(n//2)
        return S(e,e)
def toSeg(s): # assumes len(s) is a power of 2
    if len(s)<=8:
        s+="........"
        return S(s[:4],s[4:8])
    else:
        l=len(s)//2
        return S(toSeg(s[:l]),toSeg(s[l:]))
def sg(s):
    l=len(s)
    e=1
    while l>e:
        e*=2
    return toSeg(s+ "."*(e-l))

s=sg(init)
print(s.expsteps(0))
N = 50000000000
m=0
border = 0
left=0
while N!=0:
    while s.len < (1<< (m+2)):
        s=S(s,empty(s.len))
    if N & (1<<m):
        N-=(1<<m)
        assert s.len==(1<< (m+2))
        l = S(empty(s.len),s)
        e=empty(s.len)
        r = S(s,e)
        left -= 1<<(m+1)
        s = S(l.expsteps(m),r.expsteps(m))
    m+=1
print(s.sc(left))

