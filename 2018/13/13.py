from collections import defaultdict

f=open("input")
carts=[]
mp=defaultdict(bool)
for x,line in enumerate(f):
    for y,c in enumerate(line):
        if c in "/\\+":
            mp[x,y]=c
        if c==">":
            carts.append((x,y,0,1,0))
        if c=="<":
            carts.append((x,y,0,-1,0))
        if c=="^":
            carts.append((x,y,-1,0,0))
        if c=="v":
            carts.append((x,y,1,0,0))
print(len(carts))
i=0

dirs={
    (0,1):">",
    (0,-1):"<",
    (1,0):"v",
    (-1,0):"^"
    }
def prnt(cs):
    i=0
    mx = max([y for x,y in (mp)])
    my = max([x for x,y in (mp)])
    for y in range(my+1):
        s=""
        for x in range(mx+1):
            if i<len(cs) and cs[i][:2]==(y,x):
                s+=dirs[cs[i][2:4]]
                i+=1
            else:
                if w:=mp[y,x]:
                    s+=w
                else:
                    s+=" "
        print(s)
cartpos=defaultdict(bool)

crashed=set()
while True:
    carts.sort()
    if len(carts)==1:
        print(str(carts[0][1])+","+str(carts[0][0]))
        break
    #print("-----")
    #prnt(carts)
    c2=[]
    i+=1
    for y,x,dy,dx,st in carts:
        if (y,x) in crashed:
            crashed.remove((y,x))
            continue
        if not( abs(x-100)<=200 and abs(y-100)<=200):
            print (x,y,dx,dy,st,i)
            break
        #if (py,px)==(y,x):
            #print(x,y,i)
            #break
        cartpos[y,x]=False
        ny=y+dy
        nx=x+dx
        if cartpos[ny,nx]:
            cartpos[ny,nx]=False
            print(nx,ny,i)
            l=len(c2)
            c2=[p for p in c2 if p[:2]!=(ny,nx)]
            if len(c2)==l:
                crashed.add((ny,nx))
            continue
        else:
            cartpos[ny,nx]=True
        if w:=mp[ny,nx]:
            if w=="\\":
                dx,dy=dy,dx
            elif w=="/":
                dx,dy=-dy,-dx
            elif w=="+":
                st=(st+1)%3
                if st==0:#turn right
                    dx,dy=-dy,dx
                if st==1:#turn left
                    dx,dy=dy,-dx
        c2.append((ny,nx,dy,dx,st))
    else:
        carts=c2
        continue
    break


#print(f)
