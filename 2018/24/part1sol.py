import sys
from collections import defaultdict


fname=sys.argv[1] if len(sys.argv)>1 else "input"
f=list(open(fname))
#print(sys.argv[1])

split = f.index("\n")
a=f[1:split]
b=f[split+2:]

def intq(x):
    try:
        int(x)
    except Exception:
        return False
    return True
    

def parse(line):
    assert line.count("damage")==1
    mods=defaultdict(list)
    #print(line,end="")
    if "(" in line:
        r=line[line.index("(")+1:line.index(")")]
        for part in r.split(";"):
            i = part.index(" to ")
            mods[part[:i].strip()]=list(map(lambda x:x.strip(), part[i+4:].split(",")))
    ps = line.split(" ")
    
    typ = ps[ps.index("damage")-1]
    hn,hp,dam,init = [int(x) for x in ps if intq(x)]
    #print (typ, hn,hp,dam,init, mods)
    return [typ, hn,hp,dam,init, mods]
            
        
        
imm = list(map(parse,a))
inf = list(map(parse,b))

def damcalc(u1,u2):
    typ, hn,_,dam,_, _ = u1
    _, _,_,_,_, mods = u2
    if typ in mods["immune"]: return 0
    d=hn*dam
    
    if typ in mods["weak"]: d=d*2
    #print(u1,u2,d)
    return d

def targets(a,b):
    res = []
    b=list(b)
    a.sort(key=lambda t:(- t[1]*t[3],-t[4]))
    for x in a:
        b.sort(key=lambda y:( damcalc(x,y),y[1]*y[3], y[4]))
        if damcalc(x,b[-1])>0: res.append((x,b.pop()))
        if (not b): break
    return res

while imm and inf:
#for n in range(10):
    print([x[1] for x in imm] , [x[1] for x in inf],sep="\n")
    t1 = targets(imm,inf)
    t2 = targets(inf,imm)
    l = t1+t2
    l.sort(key=lambda x: - x[0][4])
    for at,df in l:
        #print(at[4])
        k = min(df[1], damcalc(at,df)//df[2])
        print(k)
        if at[1]: df[1] -= k
    imm = [x for x in imm if x[1]]
    inf = [x for x in inf if x[1]]
print([x[1] for x in imm] , [x[1] for x in inf],sep="\n")

#print("wrong")
print(sum([x[1] for x in imm + inf]))
