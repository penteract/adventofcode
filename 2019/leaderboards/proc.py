#! /usr/bin/env python3
#curl https://adventofcode.com/2019/leaderboard/day/[1-15] -O

import string
from collections import defaultdict

DAYS=25

def process(html):
    with open(html) as f:
        raw = f.read()
    rows = raw.split('<span class="leaderboard-position">')
    al = rows[1:101],rows[101:201]
    for k in al:
        for i,row in enumerate(k):
            a = row.split("</span>")
            pos,time,name = a[0],a[1],a[3]
            assert i+1 == int(pos[:3])
            time = time.split('<span class="leaderboard-time">')[-1]
            if '<span class="leaderboard-anon">' in name:
                name = name.split('>')[1]
            name = name.split('<')[0].strip()
            k[i] = (time,name)
    return al

users = defaultdict(list)



for day in range(1,DAYS+1):
    bth,fst = process(str(day))
    for i,(t,name) in enumerate(fst):
        users[name].append((i,day,"fst",t))
    for i,(t,name) in enumerate(bth):
        users[name].append((i,day,"snd",t))

def score(tup): return 100-tup[0]
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
        self.byday = [[0,0] for i in range(DAYS)]
        for i,day,part,t in self.fsts:
            self.byday[day-1][0]=100-i
        for i,day,part,t in self.snds:
            self.byday[day-1][1]=100-i
        self.bestday = max(sum(sd) for sd in self.byday)
        self.nointcode = sum(sum(x) for i,x in enumerate(self.byday) if not isintcode(i+1))
    def __str__(self):
        return f"{self.name:26}: {self.score:4}={self.score1:4}+{self.score2:4} over {self.num} NotIC:{self.nointcode}"
    def __eq__(self,other):
        if isinstance(other,str):
            return self.name==other
        elif isinstance(other,User):
            return self.name==other.name
        else:
            return False

isintcode = lambda x:bool((x<4)^(x%2))        
muchdata = {u:User(u,v)  for u,v in users.items()}


ll = [u for u in muchdata.values()]

##with open("asdict",mode="w") as f:
##    print(users,file=f)

def rank(key,user="penteract"):
    ss = sorted(ll,key=key,reverse=True)
    return ss.index(user)

def printby(key,n=200):
    for i,x in enumerate(sorted(ll,key=key,reverse=True)):
        if i>n: break
        print(i,x)

print("My rank:",rank(lambda x: x.score))
print("Joe's rank:",rank((lambda x: x.score),"joefarebrother"))
#printby(lambda x:sum(score(p) for p in x.snds if not (isintcode(p[1])) ),n=100)
#print("Not intcode")
#printby(lambda u:sum(sum(x) for i,x in enumerate(u.byday) if not isintcode(i+1)),n=100)
print("Non intcode",rank(lambda u:sum(sum(x) for i,x in enumerate(u.byday) if not isintcode(i+1))))
print("Non intcode part 2:",rank(lambda x:sum(score(p) for p in x.snds if not (isintcode(p[1])) )))
print("part 2 - part 1:",rank(lambda x:x.score2-x.score1))
print("Non intcode part 2 - part 1:",rank(lambda x:
  sum(score(p) for p in x.snds if not (isintcode(p[1]))) -
  sum(score(p) for p in x.fsts if not (isintcode(p[1])))
                                          - (x.score-x.nointcode)
  ))


#part 2 of non intcode days, subtract everything else
##printby((lambda x:
##  sum(score(p) for p in x.snds if not (isintcode(p[1]))) -
##  sum(score(p) for p in x.fsts if not (isintcode(p[1])))
##	 -(x.score-x.nointcode)
##  ),n=50)

printby((lambda x:
  (sum(score(p) for p in x.snds if not (isintcode(p[1])))*2 - x.score)*x.num
  ), n=50)
