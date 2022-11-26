from collections import defaultdict

# screen coords, north "up" is negative
compass={"up" : (0,-1),
    "forward" : (1,0),
    "down" : (0,1),
    "W" : (-1,0)
    }
invcompass = {v:k for k,v in compass.items()}

#arrowvec = {a:compass[b] for a,b in zip("^>v<","NESW")}

def invd(d):
    return {v:k for k,v in d.items()}

def bfs(neighbs,init):
    try:
        frontier=list(init)
    except e:
        frontier=[]
    seen=set(frontier)
    i=0
    while i<len(frontier):
        x=frontier[i]
        for k in neighbs(x):
            if k not in seen:
                frontier.append(k)
                seen.add(k)
    
