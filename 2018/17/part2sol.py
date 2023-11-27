import re
from typing import Tuple, Callable, Iterable, Optional
import sys
from collections import defaultdict

fname=sys.argv[1] if len(sys.argv)>1 else "input"
f = open(fname)
ftext=f.read()
flns=[line.strip() for line in ftext.split("\n")[:-1]]
f=flns
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


board=defaultdict(lambda :".")

f = [(x[0],ints_in(x)) for x in f ]
for dr,(cdr,c1,c2) in f:
    for i in range(c1,c2+1):
        board[(cdr,i) if dr == "x" else (i,cdr)]="#"
(x1,x2),(y1,y2) = [[f(x[i] for x in board.keys()) for f in [min,max]] for i in [0,1]]
def prPart(grid):
    (x1,x2),(y1,y2) = [[f(x[i] for x in grid.keys()) for f in [min,max]] for i in [0,1]]
    for y in range(y1,y2+1):
        for x in range(x1,x2+1):
            print(grid[x,y],end="")
        print()
import automaton
rls = automaton.load("2018-17.rules")
board[500,0]="+"
#automaton.run(board,rls,steps=110)
changed = [(500,0)]
while True:
    changes = [(pos,c) for (pos,c) in automaton.step(board,rls,changed) if pos[1]<=y2]
    #print(changes)
    for k,new in changes:
        board[k]=new
    changed = [change[0] for change in changes]
    if not changed:
        break
res=0
for pos in board:
    if y1<=pos[1]<=y2 and board[pos] in "~":
        res+=1
#print(f,board)
prPart(board)
print(res)
