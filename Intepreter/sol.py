from functools import *
from itertools import *

f = open("input")
l = list(f)
lll = list(map(int,l[0].split(",")) )#+[0 for i in range(3850694)]


##for k in range(100):
##    for j in range(100):
ll=[x for x in lll]
ll[1]="n"
ll[2]="v"
i=0

def get(x):
    if isinstance(x,int):
        return ll[x]
    else: return "{"+x+"}"

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

while True:
    print(ll)
    try:
        if ll[i]==1:
            ll[ll[i+3]] = add(get(ll[i+1]),get(ll[i+2]))
        elif ll[i]==2:
            ll[ll[i+3]] = mul(get(ll[i+1]),get(ll[i+2]))
        elif ll[i]==99:
            res = (ll[0])
            if res!=1: print(res)
            break
        else:
            print("bad opcode")
            break
        i+=4
    except Exception as e:
        print (e)
        break
#print(i,j,k,ll[k:k+4])
#print(ll[0])


print(i,ll)


##7+2*1+2*3+5*2*2+
##5*3*4*n+
##4*5
##+5
##+5*5
##+2*2*2
##+v
##+1
##k=0
##while k<len(l):
##    if l[k]==l[k-(len(l)//2) ]:
##        tot+=int(l[k])
##    k+=

print(tot)
