from collections import defaultdict
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"

f=list(open(fname))

#d=defaultdict(int)

d={k:set() for k in range(10)}

l = list(open("inp"))
for r in l[:8]:
    i=0
    while i*8<len(r):
        for c in r[i*8:(i+1)*8]:
            if c in "abcdefg":
                d[i+0].add(c)
        i+=1

for r in l[8:]:
    i=0
    while i*8<len(r):
        for c in r[i*8:(i+1)*8]:
            if c in "abcdefg":
                d[i+5].add(c)
        i+=1
print(d)

r=[]
for y,line in enumerate(f):
    #print(line)
    #l=list(map(int,("".join(c if c in "1234567890-" else " " for c in line).split())))
    #print(l)
    r.append(list(map((lambda x:"".join(sorted(x))
                             ),line.split())))

#print(sum(len(l) for l in r))

all="qwrtyuio"

ss={k:set() for k in range(10)}

for k,v in d.items():
    ss[len(v)].add(k)

tot=0

ns=[]

def matches(x,s,d):
    print(x,s,d)
    if len(x)!=len(s):
        print("bad len")
        return False
    for k in x:
        if len(d[k].intersection(set(s)))==0:
            return False
    for c in s:
        if not any([c in d[k] for k in x]):
            return False
    return True

for row in r:
    poss={k:v for k,v in d.items()}
    pp={k:set("abcdefg") for k in "abcdefg"} # pp[a] = correct translation of a
    al = row[:10]
    sz={k:set() for k in range(10)}
    for x in al:
        sz[len(x)].add(x)
        if len(ss[len(x)])==1:
            #print(x)
            #tot+=row[11:].count(x)
            for c in "abcdefg":
                a = d[next(iter(ss[len(x)]))]
                if c in x:
                    #print(x,c,d[ss[len(x)]],pp[c])
                    pp[c] = pp[c].intersection(a)
                    #print(x,c,d[len(x)],pp[c])
                else:
                    #print("---",x,c,d[ss[len(x)]],pp[c])
                    pp[c]-=a
                    #print(x,c,d[ss[len(x)]],pp[c])
    print(pp)
    qq = {k :  {x for x in "abcdefg" if k in pp[x]} for k in "abcdefg"}
    for k in qq["b"]:
        print([k in w for w in al])
        if sum(k in w for w in al)>6:
            pp[k].remove("b")
        else:
            assert k in qq["d"]
            pp[k].remove("d")
    print(pp)
    s=""
    for n in [1,4,7,8,0,5,2,3,9,6]:#3,
        print(n)
        for x in al:
            if matches(x,d[n],pp):
                print("--->  ",x,n)
                if n==6:
                    continue
                for c in "abcdefg":
                    if c in x:
                        pp[c] = pp[c].intersection(d[n])
                    else:
                        pp[c]-=d[n]
    for x in row[11:]:
        for n in [1,4,7,8,3,2,5,6,9,0]:
            print(n)
            if matches(x,d[n],pp):
                s+=str(n)
                break
        else:
            print("err")
    ns.append(int(s))
    #sizes = [len(x),x for x in al]
    
    print(row[:10])
print(tot)
print(sum(ns))
