from functools import *
from itertools import *
from collections import defaultdict
from math import gcd,atan2
from string import *
import sys
from heapq import *

lcm = lambda x,y: x*y//gcd(x,y)
DS=10007
f = open("input")
lines = list(f)
print("lines:",len(lines),"firstlinelength:",len(lines[0]))

deck = list(range(DS))
for line in lines:
    #print(*dec)
    if line.startswith("cut"):
        n = int(line[4:])
        deck = deck[n:] + deck[:n]
    elif line.startswith("deal with increment"):
        n = int(line[20:])
        print(n)
        assert gcd(n,DS)==1
        d=[0]*DS
        for i,k in enumerate(deck):
            d[(i*n)%DS]=k
        deck=d
    elif line:
        assert line.startswith("deal into new stack")
        deck.reverse()

#print(deck)
print(deck.index(2019))
for i in range(DS):
    assert i in deck
