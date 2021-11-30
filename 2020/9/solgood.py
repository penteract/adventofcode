#An O(n) solution to part 2

f = open("input")
l = [int(x[:-1]) for x in f]

for i in range(25,len(l)):
    for x in range(i-25,i):
        for y in range(x,i):
            if x>=0 and y>=0 and l[x]+l[y]==l[i]:
                break
        else:
            continue
        break
    else:
        print(i,l[i])
        c=l[i]
        break

s=0
j=0
k=0
while k<len(l):
    if s<c:
        s+=l[k]
        k+=1
    elif s==c:
        print(j,k,max(l[j:k])+min(l[j:k]))
        s+=l[k]
        k+=1
    else:
        s-=l[j]
        j+=1
        
