from functools import *
from itertools import *
import operator as op
from collections import defaultdict
import re
import sys
sys.setrecursionlimit(100000)
def mint(ns):
    return list(map(int,ns))

ds = [(0,1),(0,-1),(1,0),(-1,0)]
lefts = {t:l for t,l in zip("tblr","lrbt")}
rights = {l:t for t,l in zip("tblr","lrbt")}
getright=[rights,lefts]

f = open("input")
l=[x[:-1] for x in f]
##l="""Tile 2311:
##..##.#..#.
####..#.....
###...##..#.
######.#...#
####.##.###.
####...#.###
##.#.#.#..##
##..#....#..
#####...#.#.
##..###..###
##
##Tile 1951:
###.##...##.
###.####...#
##.....#..##
###...######
##.##.#....#
##.###.#####
#####.##.##.
##.###....#.
##..#.#..#.#
###...##.#..
##
##Tile 1171:
######...##.
###..##.#..#
####.#..#.#.
##.###.####.
##..###.####
##.##....##.
##.#...####.
###.##.####.
######..#...
##.....##...
##
##Tile 1427:
#####.##.#..
##.#..#.##..
##.#.##.#..#
###.#.#.##.#
##....#...##
##...##..##.
##...#.#####
##.#.####.#.
##..#..###.#
##..##.#..#.
##
##Tile 1489:
####.#.#....
##..##...#..
##.##..##...
##..#...#...
#######...#.
###..#.#.#.#
##...#.#.#..
####.#...##.
##..##.##.##
#####.##.#..
##
##Tile 2473:
###....####.
###..#.##...
###.##..#...
########.#.#
##.#...#.#.#
##.#########
##.###.#..#.
##########.#
####...##.#.
##..###.#.#.
##
##Tile 2971:
##..#.#....#
###...###...
###.#.###...
####.##..#..
##.#####..##
##.#..####.#
###..#.#..#.
##..####.###
##..#.#.###.
##...#.#.#.#
##
##Tile 2729:
##...#.#.#.#
######.#....
##..#.#.....
##....#..#.#
##.##..##.#.
##.#.####...
######.#.#..
####.####...
####..#.##..
###.##...##.
##
##Tile 3079:
###.#.#####.
##.#..######
##..#.......
########....
######.#..#.
##.#...#.##.
###.#####.##
##..#.###...
##..#.......
##..#.###...
##""".split("\n")


#l=[mint(x.split(",")) for x in f]
borders=defaultdict(list)
neighbs=defaultdict(list)

f=iter(l)
m={}



def mkmap(xss):
    m={}
    for y,row in enumerate(xss):
        for x,c in enumerate(row):
            m[x,y]=c
    return m


for t in f:
    n=int(t[4:-1])
    l=[]
    while(t:=next(f)):
        l.append(t)
    m[n]=[x[1:-1] for x in l[1:-1]]
    top=l[0]
    bot="".join(reversed(l[-1]))
    left = "".join(x[0] for x in reversed(l))
    right = "".join(x[-1] for x in l)
    #print(n,top,bot,left,right
    for d,i in zip("tblr",[top,bot,left,right]):
        borders[i].append((n,d,0))
        s="".join(reversed(i))
        for k,dd,v in borders[s]:
            neighbs[n].append((k,dd,v))
            neighbs[k].append((n,d,v))
        borders[s].append((n,d,1))

corners = [ v  for v,k in neighbs.items() if len(k)==2]

wid=int(len(neighbs)**0.5)
tl = 1699 if wid==12 else 1951
mp={}

opp={"t":"b",
     "b":"t",
     "l":"r",
     "r":"l"
    }

lv=tl
n=neighbs.copy()
nx=neighbs[tl][0]
if wid==12:
    mp[0,0]=(lv,"l",flp:=1)
else:
    mp[0,0]=(lv,"b",flp:=1)

for x in range(wid-2):
    neighbs[lv]=[x for x in neighbs[lv] if x[0]!=nx[0]]
    neighbs[nx[0]]=[x for x in neighbs[nx[0]] if x[0]!=lv]
    flp=flp^nx[2]
    mp[x+1,0] = (nx[0],getright[flp][nx[1]],flp)
    o = opp[nx[1]]
    for k in neighbs[nx[0]]:
        for a in neighbs[k[0]]:
            if a[1]==o and a[0]==nx[0]:
                r=a
                break
        else:
            continue
        break
    lv=nx[0]
    nx=k
neighbs[lv]=[x for x in neighbs[lv] if x[0]!=nx[0]]
neighbs[nx[0]]=[x for x in neighbs[nx[0]] if x[0]!=lv]
flp=flp^nx[2]


mp[wid-1,0] = (nx[0],getright[flp][nx[1]],flp)
for x in range(wid):
    lv,t,flp=mp[x,0]
    #print(lv,neighbs[lv])
    nx=neighbs[lv][0]
    for y in range(wid-2):
        neighbs[lv]=[x for x in neighbs[lv] if x[0]!=nx[0]]
        neighbs[nx[0]]=[x for x in neighbs[nx[0]] if x[0]!=lv]
        flp=flp^nx[2]
        mp[x,y+1] = (nx[0],nx[1],flp)
        #mp[x,y+1]=nx[0]
        o = opp[nx[1]]
        for k in neighbs[nx[0]]:
            for a in neighbs[k[0]]:
                if a[1]==o and a[0]==nx[0]:
                    r=a
                    break
            else:
                continue
            break
        lv=nx[0]
        nx=k
    neighbs[lv]=[x for x in neighbs[lv] if x[0]!=nx[0]]
    neighbs[nx[0]]=[x for x in neighbs[nx[0]] if x[0]!=lv]
    #mp[x,11]=nx[0]
    flp=flp^nx[2]
    mp[x,wid-1] = (nx[0],nx[1],flp)

res=[]
sz=8
for y in range(wid):
    for yy in range(sz):
        row=""
        for x in range(wid):
            n,dtop,f=mp[x,y]
            l=m[n]
            if dtop=="t":
                a=l[yy]
            elif dtop=="b":
                a=reversed(l[sz-yy-1])
            elif dtop=="l":
                a=[l[sz-1-i][yy] for i in range(sz)]
            elif dtop=="r":
                a=[l[i][sz-yy-1] for i in range(sz)]
            if f:
                a=reversed(list(a))
            row+="".join(a)
        res.append(row)


target="""                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.split("\n")
tmap=set()
for y,r in enumerate(target):
    for x,c in enumerate(r):
        if c=="#":
            tmap.add((x,y))

pts=set()
sz=wid*sz
for dx,dy in ds:
    for flp in [-1,1]:
        ex=dy*flp
        ey=-dx*flp
        for i in range(sz):
            for j in range(sz):
                for x,y in tmap:
                    kx=i+x*dx+y*dy
                    ky=j+x*ex+y*ey
                    if 0<=kx<sz and 0<=ky<sz:
                        if res[kx][ky]=="#":
                            continue
                    break
                else:
                    for x,y in tmap:
                        kx=i+x*dx+y*dy
                        ky=j+x*ex+y*ey
                        if (kx,ky) in pts:
                            vv=True
                        pts.add((kx,ky))
                    




