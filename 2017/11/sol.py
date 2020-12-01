from functools import *
from itertools import *
from collections import defaultdict

f = open("input")
l=[x for x in f]
d=defaultdict(int)
#l = [int (x) for x in l]
#print(l)
x,y=0,0
#l=["ne,ne,sw,sw "]
m=0
def d(x,y):
    if x>y: return x
    else:
        #I meant to write (y-x)//2+x, but both are equal to (x+y)//2, so it doesn't matter
        return (x-y)//2+y

for r in l[0][:-1].split(","):
    if r=="n":
        y+=2
    elif r=="s":
        y-=2
    else:
        if r[0]=="n":
            y+=1
        elif r[0]=="s":
            y-=1
        else:
            raise Exception
        if r[1]=="e":
            x+=1
        elif r[1]=="w":
            x-=1
        else:
            raise Exception
    m=max(m,d(abs(x),abs(y)))

print(x,y)
