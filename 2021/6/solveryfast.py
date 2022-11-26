from collections import defaultdict
import sys
d=defaultdict(int)
fname=sys.argv[1] if len(sys.argv)>1 else "input"

f=list(open(fname))

for y,line in enumerate(f):
    s = map(int,line.strip().split(","))
    break

s=list(s)
s=[s.count(i) for i in range(9)]

m = [[0]*9 for i in range(9)]
for i in range(8):
    m[i][i+1]=1
m[6][0]=1
m[8][0]=1

def mmul(a,b):
    m = [[0]*9 for i in range(9)]
    for i in range(9):
        for j in range(9):
            m[i][j] = sum(a[i][k]*b[k][j] for k in range(9))
    return m

def pw(m,n):
    while n%2==0:
        m=mmul(m,m)
        n//=2
    if n==1:
        return m
    return mmul(pw(m,n//2),m)

p=pw(m,256)
print(sum( p[i][j]*s[j] for i in range(9) for j in range(9)))
