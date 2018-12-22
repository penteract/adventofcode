f = open("input")
r = list(f)	  
r = [x[:-1].split(",") for x in r ]	  
r = [{a[0]:(int(a[2:]),int(a[2:])) , b[1]:(tuple(map(int,b[3:].split(".."))))  }  for a,b in r]
def mp(f,t):
    return (f(t[0]),f(t1))
x="x"
y="y"
norm = [{x:mp(ap(op.add,-464),d[x]),y:mp(ap(op.add,-3),d[y])} for d in r]
ground = [["." for x in range(464,638)] for y in range(3,1817)]
for d in norm:
    for i in range(d[x][0],d[x][1]+1):
        for j in range(d[y][0],d[y][1]+1):
            ground[j][i]="#"

sources = [((0,36))]

total = 0

#def dorow(j,i):
    
    

backtrace = []

while sources:
    j,i = sources.pop()
    l=j
    while l<=j:
        while l+1<len(ground) and ground[l+1][i]==".":
            l+=1
            ground
        if l+1==len(ground):
            break
        if ground[l+1][i] != ".":
            if ground[l+1][i] == "|":
                total+=1
                break
            res=[]
            for delta in [-1,1]:
                bor = i+delta
                while ground[l][bor]=="." and ground[l+1][bor]not in[".","|"]:
                    assert ground[l][bor]!="~"
                    bor+=delta
                    total+=1
                    ground[l][bor]="|"
                res.append(bor)
                if ground[l][bor] == 
            lef,rig = res
            if ground[l][lef] == "#" and ground[l][rig]=="#":
                for k in range(lef+1,rig):
                    ground[l][k]="~"
                    #push up
            else:
                ground[l][:
                
            
        dorow(l,i)
        l+=1
    else:
        l
    
