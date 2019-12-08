from functools import *
from itertools import *

f = open("input")
l = list(f)
lll = list(map(int,l[0].split(",")) )#+[0 for i in range(3850694)]


##for k in range(100):
##    for j in range(100):
ll=[x for x in lll]
#ll[1]="n"
#ll[2]="v"
i=0



def add(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a+b
    else:
        return str(a)+"+"+str(b)
def mul(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a*b
    else:
        return "("+str(a)+")*("+str(b)+")"

def run(machine):
    ll,i,inp=machine
    def get(x,mode):
        if mode==0:
            if isinstance(x,int):
                return ll[x]
            else: return "{"+x+"}"
        else: return x
    while True:
            try:
                op=ll[i]
                opc=op%100
                mode=list(map(int,str(op//100).rjust(2,"0")))
                if opc==1:
                    ll[ll[i+3]] = add(get(ll[i+1],mode[-1]),get(ll[i+2],mode[-2]))
                    i+=4
                elif opc==2:
                    ll[ll[i+3]] = mul(get(ll[i+1],mode[-1]),get(ll[i+2],mode[-2]))
                    i+=4
                elif opc==3:
                    assert len(inp)>0
                    x = inp.pop(0)
                    ll[ll[i+1]]=x
                    i+=2
                elif opc==4:
                    #print(mode,get(ll[i+1],mode[-1]))
                    #out.append(get(ll[i+1],mode[-1]))
                    r = get(ll[i+1],mode[-1])
                    i+=2
                    return (r,(ll,i,inp))
                elif opc==5:#jiftr
                    if get(ll[i+1],mode[-1])>0:
                        i=get(ll[i+2],mode[-2])
                    else: i+=3
                elif opc==6:#jnz
                    if get(ll[i+1],mode[-1])==0:
                        i=get(ll[i+2],mode[-2])
                    else: i+=3
                elif opc==7:
                    ll[ll[i+3]] = int(get(ll[i+1],mode[-1])<get(ll[i+2],mode[-2]))
                    i+=4
                elif opc==8:
                    ll[ll[i+3]] = int(get(ll[i+1],mode[-1]) == get(ll[i+2],mode[-2]))
                    i+=4
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
resus=[]
for settings in permutations(range(5,10)):
    out=0
    print(settings)
    machs = [([x for x in lll],0,[sett]) for sett in settings]
    while True:
        for mn,mach in enumerate(machs):
            mach[-1].append(out)
            out,x = run(mach)
            if out is None:
                print(resu)
                resus.append(resu)
                break
            else: resu=out
            machs[mn]=x
        else:
            continue
        break
    #resu.append(out[0])

print(max(resus))

