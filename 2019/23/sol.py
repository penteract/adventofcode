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
                    return (-13371338,(ll,i,inp,rel))
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

packs = defaultdict(lambda : [0,[]])
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

seen = set()
idle = [0]*50
def getinp(addr):
    yield addr
    p = packs[addr]
    while True:
        if p[0]<len(p[1]):
            idle[addr]=False
            for cor in p[1][p[0]]:
                yield cor
            p[0]+=1
        else:
            idle[addr]=True
            if addr==0 and all(idle):
                for i,x in enumerate(idle):
                    idle[i]=False
                nat = packs[255][1][-1]
                print(nat)
                if nat[1] in seen:
                    print(nat[1])
                    raise Exception()
                seen.add(nat[1]) #y of last of packs of 255
                for cor in nat:
                    yield cor
            else:
                yield -1


machs = [gen(lll,getinp(i)) for i in range(50)]


try:
    while True:
        for i,m in enumerate(machs):
            #print("out:",next(g))
            ad=next(m)
            if ad!=-13371338:
                idle[i]=False
                while (a:=next(m))==-13371338:
                    pass
                while (b:=next(m))==-13371338:
                    pass
                pack=(a,b)
                #print(pack)
                packs[ad][1].append(pack)
                #if ad==255:
                    #print (pack)
                    #break
        else:
            continue
        break
except StopIteration:
    print("over")

print("done")

#15662
