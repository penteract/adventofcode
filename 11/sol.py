from functools import *
from itertools import *
from collections import defaultdict

f = open("input")
l = list(f)
lll = list(map(int,l[0].split(",")) )
print("instruction count: ",len(lll))
ll=[x for x in lll]
i=0


def run(machine):
    global X,Y,D
    ll,i,inp,rel=machine
    def get(x,mode):
        if mode=="0":
            if isinstance(x,int):
                return ll[x]
            else: return "{"+x+"}"
        elif mode=="1": return x
        elif mode=="2": return ll[rel+x]
        else:
            raise Exception("Bad mode")
    def st(x,mode,v):
        if mode=="0": ll[x]=v
        elif mode=="2": ll[rel+x]=v
        else:
            raise Exception("Bad output mode"+mode)
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
                    #assert len(inp)>0
                    #x = inp.pop(0)
                    x = D[X,Y]
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
                    if res!=1: print(res)
                    return (None,None)
                    break
                else:
                    print("bad opcode"+str(op))
                    print(i,ll[i:i+4])
                    break
            except Exception as e:
                print(i,ll[i:i+4])
                print (e)
                raise e
                break


#ll=[x for x in lll] + [0]*10000
ll=defaultdict(int) # this doesn't seem to affect speed
for i,x in enumerate(lll):
    ll[i]=x
i=0
inp=[]
rel=0
mach = ll,i,inp,rel

st = "paint"
D = defaultdict(int)
W=set()
dx = 0
dy = -1
X=0
Y=0
D[X,Y]=1
while True:
    out,mach = run(mach)
    if out is None:
        break
    else:
        #print("out:",out)
        assert out in [0,1]
        #print("out:",out)
        if st=="paint":
            D[X,Y]=out
            W.add((X,Y))
            st="turn"
        elif st=="turn":
            st="paint"
            if out==0: dx,dy = -dy,dx
            else: dx,dy = dy,-dx
            X+=dx
            Y+=dy
##            for i in range(-20,20):
##                for j in range(-20,20):
##                    print(D[i,j]+2*((i,j)==(X,Y)),end="")
##                prin(t)
       #     input()
                
#resu.append(out[0])
for i in range(-50,50):
    for j in range(-50,50):
        print("#" if D[i,j]+2*((i,j)==(X,Y)) else ("." if (i,j) in W else " "),end="")
    print()
print("done")
print(st)
print(len(W),len(D),max((abs(k[0]),k) for k in D))
