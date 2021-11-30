from functools import *
from itertools import *
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)
def mint(ns):
    return list(map(int,ns))

ds = [(0,1),(1,0),(0,-1),(-1,0)]

f = open("input")
l=[x for x in f]
d=defaultdict(int)
#r=list(map(int,l[0].split()))

ps=[]
p={}
n=0
v=0
for x in l:
    if x=="\n":
        ps.append(p)
        p={}
    for f in x.split():
        a,b=f.split(":")
        p[a]=b.strip()

ps.append(p)

s = """byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)"""

#def test(p):

def th(h):
    if h[-2:]=="cm":
        return 150<=int(h[:-2])<=193
    if h[-2:]=="in":
        return 59<=int(h[:-2])<=76
    return False

for p in ps:
    for l in s.split("\n"):
        k=l.split()[0]
        if k not in p:
            #print(k)
            break
    else:
        if (1920<=int(p["byr"])<=2002 and 2010<=int(p["iyr"])<=2020
                and 2020<=int(p["eyr"])<=2030 and th(p["hgt"])):
            
            c=p["hcl"]
            if c[0]=="#" and all([x in "1234567890abcdef" for x in c[1:]]):
                print(p)
                if (len(c)==7 and p["ecl"] in "amb blu brn gry grn hzl oth".split()
                      and all([x in "1234567890" for x in p["pid"]]) and len(p["pid"])==9):
                    v+=1


print(v)
