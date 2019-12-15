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
        #x = input()
        #for k in x.split():
        #    yield int(k)
        #k = findunk()
        if inp is not None:
            print("input:"+str(inp))
            yield inp
        else:
            break




#print(list(gen(lll)))

g = gen(x for i,x in enumerate(lll))

pos=[0,0]
mapp = {(0,0):1}
dirs=[1,2,3,4]
dx=[0,0,-1,1]
dy=[1,-1,0,0]

def findunk():
    """find the nearest unknown point"""
    known=[(tuple(pos),None)]
    checked={tuple(pos)}
    while known:
        r,pth = known.pop(0)
        if r not in mapp:
            return pth
        elif mapp[r] in [1,2]:
            for d in dirs:
                pp=(r[0]+dx[d-1],r[1]+dy[d-1])
                if pp not in checked:
                    known.append((pp,(pth,d)))
                    checked.add(pp)

def tol(xs):
    r = []
    while xs is not None:
        xs,k=xs
        r.append(k)
    r.reverse()
    return r
try:
    while True:
        prmap()
        r = tol(findunk())
        if r==[]:
            raise StopIteration
        for d in r[:-1]:
            pos[0]+=dx[d-1]
            pos[1]+=dy[d-1]
            inp=d
            assert next(g) in [1,2]
        d = r[-1]
        pos[0]+=dx[d-1]
        pos[1]+=dy[d-1]
        inp=d
        mapp[tuple(pos)]=next(g)
        if mapp[tuple(pos)]==0:
            pos[0]-=dx[d-1]
            pos[1]-=dy[d-1]
        
        #print(next(g))
##        x=next(g)
##        y=next(g)
##        d[x,y] = next(g)
##        if d[x,y]==4:
##            bp = (x,y)
##        if d[x,y]==3:
##            pp = (x,y)
except StopIteration:
    print("over")
    prmap()



print("done")
pos=(0,0)
def findpath():
    """find the nearest unknown point"""
    known=[(tuple(pos),None)]
    checked={tuple(pos)}
    while known:
        r,pth = known.pop(0)
        if mapp[r]==2:
            return r
        elif mapp[r] in [1,2]:
            for d in dirs:
                pp=(r[0]+dx[d-1],r[1]+dy[d-1])
                if pp not in checked:
                    known.append((pp,(pth,d)))
                    checked.add(pp)

pos = findpath()
def findpath():
    """find the nearest unknown point"""
    known=[(tuple(pos),None)]
    checked={tuple(pos)}
    while known:
        r,pth = known.pop(0)
        if mapp[r] in [1,2]:
            res=pth
            for d in dirs:
                pp=(r[0]+dx[d-1],r[1]+dy[d-1])
                if pp not in checked:
                    known.append((pp,(pth,d)))
                    checked.add(pp)
    return res
p = findpath()
print(tol(p))
print(len(tol(p)))
 # ####### ##### ####### ### ########### 
#.#.......#.....#.......#...#...........#
#.#.#####.#.###.#.#####.#.###.#####.###.#
#...#.....#...#...#.....#.#...#...#.#...#
 ####.#.#####.#####.#####.#.###.#.#.#.## 
#.....#.#...#.#...#.....#...#...#...#...#
#.#######.#.#.#.#.#####.#####.###### ##.#
#...#.....#.#.#.#.#...#.......#.....#@#.#
 ##.#.#####.#.#.#.###.#########.###.#.#.#
#...#.#.....#...#...#.............#...#.#
#.###.###.#####.###.#.###########.#####.#
#...#...#.#...#...#.#...#...#.#...#...#.#
#.#.###.#.#.#.#####.###.#.#.#.#.###.#.#.#
#.#.#...#...#.......#.....#.#.#.....#.#.#
 ##.#.###.#################.#.#######.#.#
#...#...#.#.............#.#...#.....#.#.#
#.#####.###.###########.#.###.#####.#.#.#
#.....#...#.#.........#.#...#.......#.#.#
 ####.###.#.#.###.#####.###.#######.#.#.#
#...#...#...#.#.#...#...#.........#.#...#
#.#.###.#####.#.###.#####.###.#####.#### 
#.#.....#.........#.......#...#.....#...#
#.#####.#.###########.#######.#.#######.#
#.....#.#...#...#.....#.....#.#.#.......#
#.###.#####.#.#.#.#.###.###.###.###.###.#
#...#.....#.#.#...#.#...#.#.....#...#...#
 ########.#.#.#### ##.###.#######.###.## 
#.......#...#.....#...#.......#...#.....#
#.#####.#####.###.#.###.###.#.#.#######.#
#...#...#...#.#...#.#...#...#.#.#...#...#
 ##.#.###.#.###.#.#.#####.###.#.#.#.###.#
#...#.....#.....#.#.......#...#...#...#.#
#.## ######################.###### ##.#.#
#...#.........#.......#.....#.....#...#.#
#.#.#.#######.#.#####.#.#####.###.#.###.#
#.#...#...#.#...#...#.#.#.....#...#.#...#
#.#####.#.#.#####.#.#.#.#.#####.###.#### 
#...#...#.#...#.#.#...#.#.....#...#.....#
 ##.#.###.#.#.#.#.#####.#####.###.#####.#
#.....#.....#...#.............#.........#
 ##### ##### ### ############# ######### 
