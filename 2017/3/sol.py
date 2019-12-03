from functools import *
from itertools import *
inp = 12 #265149

g = [[0]*12 for j in range(12)]

g[0][0]=1
r = range(-1,2)
k=0
n=0
def do(i,j):
    print(i,j)
    t=0
    global n
    n+=1
    for dx in r:
        for dy in r:
            t+=g[dx][dy]
    if t>inp:
        print (t,n)
        exit()
    #for l in g: print("".join(map(str,l)))
    g[i][j]=t

while True:
    k+=1
    #n = k*2+1
    for y in range(1-k,k+1):
        do(-k,y)
    for x in range(1-k,k+1):
        do(x,k)
    for y in range(k-1,-k-1,-1):
        do(k,y)
    for x in range(k-1,-k-1,-1):
        do(x,-k)
    


print(tot)
