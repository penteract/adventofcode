#! /usr/bin/env python3
import json
dat = open("419070.json").read()
j = json.loads(dat)
byname = {j["members"][i]["name"]:j["members"][i] for i in j["members"]}
bypuzz = {}
G="get_star_ts"
HOUR=60*60
DAY = HOUR*24

for n in byname:
  for l in byname[n]["completion_day_level"]:
    if l not in bypuzz: bypuzz[l]={}
    k = byname[n]["completion_day_level"][l]
    if all(c in k for c in "12"): bypuzz[l][n] = [int(k["1"][G]),int(k["2"][G])]
    elif all(c in k for c in "1"): bypuzz[l][n] = [int(k["1"][G]),int(k["1"][G])+1000000]

LEN = len("joefarebrother") + len(str(DAY)) + 1

print(" ".join((b+"").rjust(LEN) for b in ["part1","part2","delta"]))

for day,dat in sorted(bypuzz.items(),key=lambda x:int(x[0])):
  l1=[]
  l2=[]
  ld=[]
  for name,(t1,t2) in dat.items():
    l1.append(((t1-5*HOUR)%DAY,name))
    l2.append(((t2-5*HOUR)%DAY,name))
    ld.append((t2-t1,name))
  l1.sort()
  l2.sort()
  ld.sort()
  print(day)
  for tri in zip(l1,l2,ld):
      print(" ".join((str(b)+":"+str(a)).rjust(LEN) for a,b in tri))
  print()
