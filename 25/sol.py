#! /usr/bin/env python3
from functools import *
from itertools import *
from collections import defaultdict
import sys
sys.setrecursionlimit

print (len(sys.argv))

def neighbs(p):
    """neighbours in a 2D grid"""
    x,y=p
    for dx in [1,-1]: yield (x+dx,y)
    for dy in [1,-1]: yield (x,y+dy)

fname = "input"
if len(sys.argv)>1:
    fname=sys.argv[1]
f = open(fname)
l = list(f)
lll = list(map(int,l[0].split(",")) )
print("instruction count: ",len(lll))
ll=[x for x in lll]

def run(machine):
    ll,i,inp,rel=machine
    def get(x,mode):
        if mode=="0":
            if isinstance(x,int):
                return ll[x]
            else: return "{"+x+"}"
        elif mode=="1": return x
        elif mode=="2": return ll[rel+x]
        else:
            raise Exception("Bad mode "+mode)
    def st(x,mode,v):
        if mode=="0": ll[x]=v
        elif mode=="2": ll[rel+x]=v
        else:
            raise Exception("Bad output mode "+mode)
    while True:
            try:
                #print(ll[i:i+4])
                op=ll[i]
                opc=op%100
                mode=list(str(op//100).rjust(3,"0"))
                if opc==1:
                    st(ll[i+3],mode[-3],
                        get(ll[i+1],mode[-1])+get(ll[i+2],mode[-2])
                        )
                    i+=4
                elif opc==2:
                    st(ll[i+3],mode[-3],
                          get(ll[i+1],mode[-1])*get(ll[i+2],mode[-2])
                        )
                    i+=4
                elif opc==3:
                    x = next(inp)
                    st(ll[i+1],mode[-1],
                        x)
                    i+=2
                elif opc==4:
                    r = get(ll[i+1],mode[-1])
                    i+=2
                    return (r,(ll,i,inp,rel))
                elif opc==5:#jiftr
                    if get(ll[i+1],mode[-1])>0:
                        i=get(ll[i+2],mode[-2])
                    else: i+=3
                elif opc==6:#jnz
                    if get(ll[i+1],mode[-1])==0:
                        i=get(ll[i+2],mode[-2])
                    else: i+=3
                elif opc==7:
                    st(ll[i+3],mode[-3],
                          int(get(ll[i+1],mode[-1])<get(ll[i+2],mode[-2]))
                       )
                    i+=4
                elif opc==8:
                    st(ll[i+3],mode[-3],
                       int(get(ll[i+1],mode[-1]) == get(ll[i+2],mode[-2]))
                       )
                    i+=4
                elif opc==9:
                    rel += get(ll[i+1],mode[-1])
                    i+=2
                elif opc==99:
                    res = (ll[0])
                    #if res!=1: print(res)
                    return (None,None)
                    break
                else:
                    print("bad opcode"+str(op))
                    print(i,ll[i:i+4])
                    break
            except Exception as e:
                print(i,ll[i:i+4])
                #print (e)
                raise e
                break


def gen(lll,inp=None):
    if inp is None: inp = getinp()
    inp=iter(inp)
    ll=[x for x in lll] + [0]*10000
    i=0
    rel=0
    mach = ll,i,inp,rel
    while True:
        out,mach = run(mach)
        if out is None:
            break
        else:
            #print("out:",out)
            yield out

e="east"
w="west"
n="north"
s="south"

def getinp():
##    for c in springcode:
##        yield ord(c)
##
    while True:
        x = input()
        if x=="e": x=e
        elif x=="w": x=w
        elif x=="n": x=n
        elif x=="s": x=s
        for k in x:
            yield ord(k)
        yield(ord("\n"))


g = gen(x for i,x in enumerate(lll))

def tol(xs):
    r = []
    while xs is not None:
        xs,k=xs
        r.append(k)
    r.reverse()
    return r
m={}
l=""
try:
    while True:
        #print("out:",next(g))
        x=next(g)
        if x<128:
            print(chr(x),end="")
        else: print(x)
except StopIteration:
    print("over")


print("done")
