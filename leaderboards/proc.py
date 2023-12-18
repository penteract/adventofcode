#! /usr/bin/env python3
#curl -A "<email> via curl" https://adventofcode.com/2023/leaderboard/day/[1-15] -O

import string
from collections import defaultdict
import time

POINTLESS=[]


import sys,os
print(sys.argv)
path = sys.argv[1] if len(sys.argv)>1 else "../2021"
if os.path.isdir(path+"/leaderboards/"):
    path=path+"/leaderboards/"
print(path)
DAYS=[i for i in list(range(1,25+1)) if os.path.isfile(os.path.join(path,str(i)))]  
print(DAYS)
def process(html):
    with open(os.path.join(path,html)) as f:
        raw = f.read()
    rows = raw.split('<span class="leaderboard-position">')
    al = rows[1:101],rows[101:201]
    for k in al:
        for i,row in enumerate(k):
            a = row.split("</span>")
            pos,t,name = a[0],a[1],a[3]
            assert i+1 == int(pos[:3])
            t = t.split('<span class="leaderboard-time">')[-1]
            t=time.strptime(t,"%b %d  %H:%M:%S")
            if '<span class="leaderboard-anon">' in name:
                name = name.split('>')[1]
            name = name.split('<')[0].strip()
            k[i] = (t,name)
    return al

users = defaultdict(list)



for day in DAYS:
    bth,fst = process(str(day))
    for i,(t,name) in enumerate(fst):
        users[name].append((i,day,"fst",t))
    for i,(t,name) in enumerate(bth):
        users[name].append((i,day,"snd",t))

def score(tup):
    if tup[1] in POINTLESS:
        return 0
    return 100-tup[0]
class User():
    def __init__(self,name,ranks):
        self.name=name
        self.fsts = [r for r in ranks if r[2]=="fst"]
        self.snds = [r for r in ranks if r[2]=="snd"]
        self.ranks = ranks
        self.num = len(ranks)
        self.scores = [score(r) for r in ranks]
        self.score = sum(self.scores)
        self.score1 = sum(score (r) for r in self.fsts)
        self.score2 = sum(score (r) for r in self.snds)
        self.byday = [[0,0] for i in range(max(DAYS)+1)]
        for i,day,part,t in self.fsts:
            self.byday[day-1][0]=100-i
        for i,day,part,t in self.snds:
            self.byday[day-1][1]=100-i
        self.bestday = max(sum(sd) for sd in self.byday)
    def __str__(self):
        return f"{self.name:26}: {self.score:4}={self.score1:4}+{self.score2:4} over {self.num}"
        #k=";".join(",".join(str(x) for x in y) for y in self.byday)
        #return f"{self.name:26}: {self.score:4} {self.score2-self.score1:4} {k}"
        
        #ss = sorted([(a+b,d) for d,(a,b) in enumerate(self.byday)])
        #return "Y" if 19 in [x[1] for x in ss[5:15]] else "N" # ".join(("" if d!=19 else "##")+str(d)+","+str(n) for n,d in ss)
        
        #for n in ss:
        #    print(n,end="")
        #";".join(",".join(str(x) for x in y) for y in self.byday)
    def __eq__(self,other):
        if isinstance(other,str):
            return self.name==other
        elif isinstance(other,User):
            return self.name==other.name
        else:
            return False

muchdata = {u:User(u,v)  for u,v in users.items()}


ll = [u for u in muchdata.values()]

##with open("asdict",mode="w") as f:
##    print(users,file=f)

def rank(key,user="penteract"):
    ss = sorted(ll,key=key,reverse=True)
    return ss.index(user)

def printby(key,n=200):
    count=0
    for i,x in enumerate(sorted(ll,key=key,reverse=True)):
        if i>n: break
        if x.score1<x.score2:count+=1
        
        print(i,key(x),x)
    print("number with greater p2 than p1:",count)

#print("My rank:",rank(lambda x: x.score))
#print("Joe's rank:",rank((lambda x: x.score),"joefarebrother"))
#printby(lambda x:sum(score(p) for p in x.snds if not (isintcode(p[1])) ),n=100)
#print("Not intcode")
#printby(lambda u:sum(sum(x) for i,x in enumerate(u.byday) if not isintcode(i+1)),n=100)
#print("ranked by p2 scores - i*p1/10:")
#for i in range(13,18):
#    print(i)
#    printby((lambda x: x.score2-x.score1*i/10), n=6)
    #print(i,"part 2 - part 1:",rank(lambda x:x.score2-x.score1*i/100))


#part 2 of non intcode days, subtract everything else
##printby((lambda x:
##  sum(score(p) for p in x.snds if not (isintcode(p[1]))) -
##  sum(score(p) for p in x.fsts if not (isintcode(p[1])))
##	 -(x.score-x.nointcode)
##  ),n=50)

#printby((lambda x: x.score), n=150)
#me = muchdata["penteract"]

##for a in range(10):
##  for b in range(2):
##    if me.byday[a][b]==0:
##        #print(a+1,b+1,rank((lambda x: x.score-x.byday[a][b])))
##        pass

#print(me.score2-me.score1)
#print(me.score)
#printby((lambda x: x.score2-x.score1), n=20)


#[x for x in muchdata.values() if x.score>me.score and (x.score - x.byday[2-1][1]) < me.score and x.byday[2-1][1]< ]

top100 = sorted(ll,key=lambda x:x.score,reverse=True)[:100]

for day in DAYS:
    bd = sorted(ll,key=lambda x:sum(sum(z) for z in x.byday[:day]),reverse=True)
    print(day, sum(sum(z) for z in bd[99].byday[:day]))

#print("number of top 100 who scored for a part:")
#for day in DAYS:
#    for part in [0,1]:
#        print(len([x for x in top100 if x.byday[day-1][part]>0 ]),end=" ")
#    print()

