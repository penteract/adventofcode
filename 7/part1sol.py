import re
from typing import Tuple, Callable, Iterable, Optional
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"
f=[line.strip() for line in open(fname)]

from collections import defaultdict

d=defaultdict(list)

#copied from https://github.com/joefarebrother/adventofcode/blob/master/misc_utils.py
def lmap(f: Callable, *xs) -> list:
    """Like map but returns a list"""
    return list(map(f, *xs))

def ints(xs: Iterable) -> list[int]:
    """Casts each element of xs to an int"""
    return lmap(int, xs)

def mint(x, default=None):
    """Maybe int - casts to int and returns default on failure"""
    try:
        return int(x)
    except ValueError:
        return default

def ints_in(x: str) -> list[int]:
    """Finds and parses all integers in the string x"""
    ex = r'(?:(?<!\d)-)?\d+'
    return ints(re.findall(ex, x))

try:
    xs = ints(f)
except Exception:
    pass
try:
    xss = lmap(ints_in,f)
except Exception:
    pass

i=0
while i<len(f):
    line=f[i]
    if line=="$ cd /":
        cd=[]
        i+=1
    elif line=="$ cd ..":
        cd.pop()
        i+=1
    elif line.startswith("$ cd "):
        cd.append(line[5:])
        i+=1
    elif line.startswith("$ ls"):
        i+=1
        dn = tuple(cd)
        while i<len (f) and not (line:=f[i]).startswith("$"):
            d[dn].append(line)
            i+=1
    else:
        print(i,line)
        break
dns = list(d)
cache={}
def getsz(dn):
    if dn in cache:
        return cache[dn]
    s=0
    for k in d[dn]:
        if k.startswith("dir "):
            s+=getsz(dn+(k[4:],))
        else:
            s+=int(k.split()[0])
    cache[dn]=s
    return s
        
s=0
for dn in d:
    sz=getsz(dn)
    if sz<=100000:
        s+=sz
print(s)
