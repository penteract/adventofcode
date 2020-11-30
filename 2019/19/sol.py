from functools import *
from itertools import *
from collections import defaultdict
import sys
sys.setrecursionlimit

print (len(sys.argv))

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


def gen(lll,x,y):
    ll=[x for x in lll] + [0]*10000
    i=0
    inp=[]
    rel=0
    mach = ll,i,getinp(x,y),rel
    while True:
        out,mach = run(mach)
        if out is None:
            break
        else:
            #print("out:",out)
            yield out

    
def getinp(x,y):
    yield x
    yield y
    #while True:
        #prmap()
        #x = input()
        #for k in x.split():
            #yield int(k)
##        if inp is not None:
##            print("input:"+str(inp))
##            yield inp
##        else:
##            break


def tst(x,y):
    return next(gen(lll,x,y))
    #if y==0: return x==0
    #return (x)*9>5*y and x*10<y*7
m={}
for x in range(50):
    for y in range(50):
        m[x,y] = tst(x,y)#next(gen(lll,x,y))

print(sum(m[k] for k in m))

##for y in range(50):
##    for x in range(50):
##        print(int(m[x,y]),end="")
##    print()
print(max(x/y for (x,y) in m if y!=0 and m[x,y]))
print(min(x/y for (x,y) in m if y!=0 and m[x,y]))
print(max(x/y for (x,y) in m if y!=0 and not m[x,y] and (x/y)<0.6))
print(min(x/y for (x,y) in m if y!=0 and not m[x,y] and (x/y)>0.6))
mx = max(x/y for (x,y) in m if y!=0 and m[x,y])
x=0
for y in range(200,100000):
    while not (tst(x,y) and not tst(x+1,y)):
        x+=1
    if x/y>mx:
        print(x/y)
        print((x+1)/y)
        mx=x/y
    if tst(x-99,y+99):
        print(10000*(x-99)+(y))
        break
print(x,y)
##
##g = gen(x for i,x in enumerate(lll))
##
##dx=[0,0,-1,1]
##dy=[1,-1,0,0]
##
##def tol(xs):
##    r = []
##    while xs is not None:
##        xs,k=xs
##        r.append(k)
##    r.reverse()
##    return r
##m={}
##try:
##    while True:
##        print("out:",next(g))
##except StopIteration:
##    print("over")



print("done")
