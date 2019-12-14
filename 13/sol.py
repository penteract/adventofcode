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
                    if res!=1: print(res)
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


def display(d):
    l = list(d.keys())
    m=max(l)
    for y in range(m[1]):
        print("".join(" #=_@"[d[x,y]] for x in range(m[0])))
    if (-1,0) in d: print(d[-1,0])
def getinp():
    while True:
        display(d)
        x = input()
        print(x)
        #for k in x:
        #    yield (int(k)-6)
        #if bp[0]>pp[0]:
            #yield 1
        #elif bp[0]<pp[0]:
            #yield -1
        #else: yield 0

ll=[x for x in lll] + [0]*10000
#ll=defaultdict(int) # this doesn't seem to affect speed
for i,x in enumerate(lll):
    ll[i]=x
i=0
inp=[]
rel=0
ll[0]=2
mach = ll,i,getinp(),rel

def gen(mach):
    while True:
        out,mach = run(mach)
        if out is None:
            break
        else:
            #print("out:",out)
            yield out

print(len(l))
d= defaultdict(int)
g = gen(mach)
bp = (0,0)
pp = (0,0)
try:
    while True:
        x=next(g)
        y=next(g)
        d[x,y] = next(g)
        if d[x,y]==4:
            bp = (x,y)
        if d[x,y]==3:
            pp = (x,y)
except StopIteration:
    print("over")


#for x,y,t in zip(l[::3],l[1::3],l[2::3]):
#    d[x,y]=t
#print(sum(1 for k in d if d[k]==2))
#resu.append(out[0])

print("done")
display(d)

