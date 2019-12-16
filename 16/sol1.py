from functools import *
from itertools import *
from collections import defaultdict
from math import gcd,atan2
from string import *

lcm = lambda x,y: x*y//gcd(x,y)

f = open("input")

x = f.read()
x="0303673257721294406349"*100+" "
l = (list(map(int,x[:-1])))
ll= l*10000

print(len(l))

def k(i):
    return cycle([0]*(i-1)+[1]*i+[0]*i+[-1]*i+[0])

def f(x): return abs(x)%10
for j in range(100):
    #nx=[]
    #for i in range(len(l)):
##        t=0
##        if (650*1000)%((i+1)*4)==0:
##            nx.append(0)
##        else:
##            d = ((i+1)*)4
        #for k in range(len(l)):
        #    (k+1)*4
     #   nx.append(abs(t)%10)

    l = [abs(sum(a*b for a,b in zip(l,k(i+1))))%10 for i in range(len(l)) ]
    print(j)

##for j in range(1):
##    nx=[]
##    for i in range(len(l)*10000):
##        t=0
##        if (650*1000)%((i+1)*4)==0:
##            nx.append(0)
##        else:
##            d = ((i+1)*4)
##            
##        #for k in range(len(l)):
##        #    (k+1)*4
##        nx.append(abs(t)%10)
##    #l = [int(str(sum(a*b for a,b in zip(l,k(i+1))))[-1]) for i in range(len(l)) ]


def justgetints(line):
    line+="\n"
    i=0
    res=[]
    while i<len(line):
        if (line[i]=="-" and line[i+1] in digits) or line[i] in digits:
            j=i+1
            while line[j] in digits: j+=1
            res.append(int(line[i:j]))
            i=j-1
        i+=1
    return res
        
#5979187

#print("".join(map(str,nx[:10000])))
print("".join(map(str,l)))
#59522422
