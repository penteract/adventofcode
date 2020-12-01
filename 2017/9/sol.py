from functools import *
from itertools import *
from collections import defaultdict

f = open("input")
l=[x for x in f]
#l = [int (x) for x in l]
#print(l)

s=l[0]

def parsegarbage(s):
    i=0
    j=0
    while s[i]!=">":
        if s[i]=="!":
            i+=2
        else:
            i+=1
            j+=1
    return j,s[i+1:]
    

def parseitem(s,n=0):
    if s[0]=="{":
        return parsegroup(s[1:],n+1)
    if s[0]=="<":
        return parsegarbage(s[1:])
    else:
        print(s[:20])
def parsegroup(s,n):
    tot=0
    while s[0]!="}":
        m,s=parseitem(s,n)
        tot+=m
        if s[0]==",":
            s=s[1:]
    return tot,s[1:]

k=parseitem(s)
print(k[0])
