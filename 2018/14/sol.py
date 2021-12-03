f=int(next(open("input")))
print(f)
ss=str(f)

rs = [3,7]
e1=0
e2=1
while str(f) not in "".join(map(str,rs)):
    for i in range(f):
        t=str(rs[e1]+rs[e2])
        for k in t:
            rs.append(int(k))
        e1+=1+rs[e1]
        e1%=len(rs)
        e2+=1+rs[e2]
        e2%=len(rs)
print("".join(map(str,rs)).find(str(f)))
