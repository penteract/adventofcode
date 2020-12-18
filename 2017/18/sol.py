from functools import *
from itertools import *
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)

f = open("input")

l=[x.split() for x in f]

trans ={
    "set":"=",
    "mul":"*=",
    "add":"+=",
    "mod":"%="
    }

d0=defaultdict(int)
d1=defaultdict(int)
res=[]
d0["p"]=0
d1["p"]=1
other=(0,d1,0) #pc,vars,numread
myout=[]
otherout=res
numrecving=0
numread=0
d=d0
pc=0
ic=0
while True:
    ins=l[pc]
    if(len(ins)==3):
        i,a,b=ins
        if i=="jgz":
            if eval(a+">0",d):
                pc+=eval(b,d)
            else:
                pc+=1
        else:
            #print(i)
            pc+=1
            exec(a+trans[i]+b,d)
            ic+=1
            #print(d["a"])
    else:
        i,a=ins
        if i=="snd":
            #print("sending",otherout is res)
            pc+=1
            myout.append(eval(a,d))
            if numrecving>0:
                numrecving-=1
        else:
            assert i=="rcv"
            #print("rcv")
            if len(otherout)>numread:
                pc+=1
                d[a.strip()]=otherout[numread]
                numread+=1
            else:
                #print("swapping",ic)
                if numrecving>0:
                    print("here")
                    break
                numrecving+=1
                other,(pc,d,numread)=(pc,d,numread),other
                otherout,myout=myout,otherout

print(len(res))
