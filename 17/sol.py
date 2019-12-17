from functools import *
from itertools import *
from collections import defaultdict
import sys

print (len(sys.argv))

fname = "input"
if len(sys.argv)>1:
    fname=sys.argv[1]
f = open(fname)
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


def gen(lll):
    ll=[x for x in lll] + [0]*10000
    #ll=defaultdict(int) # this doesn't seem to effect speed
    #for i,x in enumerate(lll):
    #    ll[i]=x
    i=0
    inp=[]
    rel=0
    #ll[0]=2
    mach = ll,i,getinp(),rel
    while True:
        out,mach = run(mach)
        if out is None:
            break
        else:
            #print("out:",out)
            yield out

def prmap():
    l = list(mapp.keys())
    m1=max(x for x,y in l)
    m2=min(x for x,y in l)
    m3=max(y for x,y in l)
    m4=min(y for x,y in l)
    for y in range(m4,m3+1):
        print("".join("#.@="[mapp[x,y]] if (x,y) in mapp else " " for x in range(m2,m1+1)))
    print(pos)
    
def getinp():
    while True:
        #prmap()
        x = input()
        for k in x:
            yield ord(k)
        yield 10
        #k = findunk()
##        if inp is not None:
##            print("input:"+str(inp))
##            yield inp
##        else:
##            break



def tol(xs):
    r = []
    while xs is not None:
        xs,k=xs
        r.append(k)
    r.reverse()
    return r
mapp={(0,0):"?"}
g = gen(lll)

m=list(g)
grid = "".join(map(chr,m))
print(grid,end="")
rws = grid.split("\n")
#print(rws[-3:])
m={}
for y,row in enumerate(rws):
    for x,col in enumerate(row):
        m[x,y]=col
#print(m)
#print("".join(m[15,y] for y in range(20)))
t = 0
f = lambda x,y: False if (x,y) not in m else m[x,y]
for x in range(len(rws[0])):
    for y in range(len(rws)):
        #if all(f(x+dx,y+dy)=="#" for dx,dy in [(0,0),(1,0),(0,1),(-1,0),(0,-1)]): t+=x*y
        if f(x,y)=="^": pos=(x,y)

L = lambda x,y:(y,-x)
R = lambda x,y:(-y,x)
add = lambda a,b:(a[0]+b[0],a[1]+b[1])
dr = (0,-1)
instrs = []
while True:
    while f(*add(pos,dr))=="#":
        #instrs[-1]+=1
        instrs.append(1)
        pos=add(pos,dr)
    if f(*add(pos,L(*dr)))=="#":
        instrs.append("L")
        #instrs.append(0)
        dr=L(*dr)
    elif f(*add(pos,R(*dr)))=="#":
        instrs.append("R")
        #instrs.append(0)
        dr=R(*dr)
    else:
        break
print(instrs)
#instrs=instrs[1:-1]
print(len(instrs))

res = []
matches = {}
for i,x in enumerate(instrs):
    res.append((0,-1))
    for j in range(i):
        m=0
        while i+m<len(instrs) and instrs[j+m]==instrs[i+m] and j+m+1<i:
            m+=1
        a,b=res[-1]
        if m>a: res[-1]=m,j
        matches[i,j]=m

def ti(xs):
    k=[0]
    for p in xs:
        if p in ["L","R"]:
            k.append(p)
            k.append(0)
        else: k[-1]+=p
    if k[0]==0:k.pop(0)
    if k[-1]==0:k.pop()
    return k

#print(list((i,b) for i,b in enumerate(res) if b[1]!=-1))
for i,x in enumerate(res):
    #print(x)
    if x[0]>40 and res[i-1][0]<x[0]:
        print(i,x)

for ((i,j),v) in matches.items():
    if v>10 and (j==99 or i==99):
        print(i,j,v)

#print("".join(map(chr,m)))
#print(t)
rs = [x for x in instrs]
al=5

def ss(xs):
    return ",".join(str(x)for x in xs)

while len(ss(ti(rs[0:al])))<21:
    aseg = rs[0:al]
    bl=1
    if rs[al+bl-1]==1:bl+=1
    bseg = rs[al:al+bl]
    while len(ss(ti(bseg)))<21:
        pos=al+bl
        hist="AB"
        while True:
            if rs[pos:pos+al]==aseg:
                hist+="A"
                pos+=al
            elif rs[pos:pos+bl]==bseg:
                hist+="B"
                pos+=bl
            else: break
        cl = 1
        if rs[pos+cl-1]==1:cl+=1
        cseg=rs[pos:pos+cl]
        hist+="C"
        while len(ss(ti(cseg)))<21:
            p=pos+cl
            while True:
                if rs[p:p+al]==aseg:
                    hist+="A"
                    p+=al
                elif rs[p:p+bl]==bseg:
                    hist+="B"
                    p+=bl
                elif rs[p:p+cl]==cseg:
                    hist+="C"
                    p+=cl
                else: break
            if p>300 and len(hist)<20: resu = ",".join(hist),ss(ti(aseg)),ss(ti(bseg)),ss(ti(cseg))
            cl+=1
            if rs[pos+cl-1]==1:cl+=1
            cseg=rs[pos:pos+cl]
        bl+=1
        if rs[al+bl-1]==1:bl+=1
        bseg = rs[al:al+bl]
    al+=1
    if rs[al]==1:al+=1


print(resu)

lll[0]=2
g = gen(lll)
try:
    while True:
        i=next(g)
        if i<128:
            print(chr(i),end="")
        else: print(i)
except StopIteration:
    print("over")
    #prmap()



#print("done")

