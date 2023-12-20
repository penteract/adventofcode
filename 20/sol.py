import re
from typing import Tuple, Callable, Iterable, Optional
import sys

fname=sys.argv[1] if len(sys.argv)>1 else "input"
f = open(fname)
ftext=f.read()

from collections import defaultdict

#copied from https://github.com/joefarebrother/adventofcode/blob/master/misc_utils.py
def lmap(f: Callable, *xs) -> list:
    return list(map(f, *xs))
def mint(x, default=None):
    try: return int(x)
    except ValueError: return default
def ints(x: str) -> list[int]:
    ex = r'(?:(?<!\d)-)?\d+'
    return lmap(int,re.findall(ex, x))

def ints_locs(x: str) -> list[tuple[int,tuple[int,int]]]:
    ex = r'(?:(?<!\d)-)?\d+'
    return [(int(x.group()),x.span()) for x in re.finditer(ex, x)]

class Pt(tuple):
    def __add__(self,other):
        return Pt([x+y for x,y in zip(self,other,strict=True)])
    def __sub__(self,other):
        return Pt([x-y for x,y in zip(self,other,strict=True)])
    def __rsub__(self,other):
        return Pt([y-x for x,y in zip(self,other,strict=True)])
    def __radd__(self,other):
        return Pt([y+x for x,y in zip(self,other,strict=True)])
    def __rmul__(self,other):
        return Pt([other*x for x in self])
    def left(self):
        x,y=self
        return Pt((y,-x))
    def right(self):
        x,y=self
        return Pt((-y,x))
def pt(*args):
    if len(args)==1: return Pt(args[0])
    else: return Pt(args)
dirs = {
    "R":Pt((1,0)),
    "U":Pt((0,-1)),
    "L":Pt((-1,0)),
    "D":Pt((0,1))
    }
ods = list(dirs.values())

#odirs = [(0,1),(1,0),(0,-1),(-1,0)]
ddirs = lmap(Pt,[(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)])

##Input handling
flns=[line.strip() for line in ftext.split("\n")[:-1]]
f=flns

fgroups = ftext.split("\n\n")
if len(fgroups)>1:
    fgs = [g.split("\n") for g in fgroups]
    fgns = [lmap(ints,g) for g in fgs]

try: xs = lmap(int,f)
except Exception: pass
try: xss = lmap(ints,f)
except Exception: pass


d=defaultdict(list)
inps = defaultdict(list)
state = {}
for line in f:
    src,dsts = line.split("->")
    dsts=[x.strip() for x in dsts.split(",")]
    src=src.strip()
    op=None
    if src!="broadcaster":
        op=src[0]
        src=src[1:]
    d[src]=(op,dsts)
    for k in dsts:
        inps[k].append(src)
    if op=="%":
        state[src]=False

for k in d:
    if d[k][0]=="&":
        state[k]={x:False for x in inps[k]}

for k in inps:
    if k not in d:
        print(inps[k])
        state[k]=False
        d[k]=("*",[])

from collections import deque
def push():
    #lo=False
    pulses = deque([(False,"broadcaster","button")])
    rr=[]
    while pulses:
        hi,dst,prev = pulses.popleft()
        if prev in ["kv","jg","rz","mr"] and hi:
            rr.append(prev)
        #print(dst,d[dst])
        op,dsts = d[dst]
        if op is None:
            for x in dsts:
                pulses.append((hi,x,dst))
        elif op == "%":
            if (not hi):
                state[dst] = not state[dst]
                for x in dsts:
                    pulses.append((state[dst],x,dst))
        elif op=="*":
            if (not hi):
                return True
        else:
            assert op == "&"
            state[dst][prev]=hi
            r = not all(k for k in state[dst].values())
            for x in dsts:
                pulses.append((r,x,dst))
    return rr

lo=0
hi=0
x=0
while True:
    x+=1
    r=push()
    if r:
        print(x,r)
    
    
#tot=0

#print(lmap(ints_locs,f))

#print(lo*hi)

