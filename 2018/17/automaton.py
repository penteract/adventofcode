from collections import defaultdict
def load(fname):
    """
    Loads rules from a file
    the format is a list of states, with each state followed by a list of
    circumstances under which it should change, based on the surrounding cells.
    * is awildcard

    for example:
    
    a

    *c*
    *b*
    ***

    means that 'a' should change to 'b' whenever if there is a 'c' above it.
    """
    ftxt = open(fname).read()
    rules = defaultdict(list)
    currentTok = None
    for group in ftxt.split("\n\n"):
        group = group.strip()
        if not group:
            continue
        if len(group)==1:
            currentTok=group
        else:
            assert currentTok is not None
            g = [x.strip() for x in group.split("\n")]
            assert len(g)==3
            assert all(len(x)==3 for x in g)
            tests = []
            new=None
            for y,r in enumerate(g,start=-1):
                for x,c in enumerate(r,start=-1):
                    if (x,y)==(0,0):
                        new = c
                    elif c!="*":
                        tests.append((Pt((x,y)),c))
            rules[currentTok].append((tests,new))
    return rules
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

ddirs = list(map(Pt,[(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]))


def step(board,rules,changed=None):
    if changed is None:
        changed = board.keys()
    ch2 = set()
    for k in changed:
        ch2.add(k)
        for d in ddirs:
            ch2.add(k+d)
    changes = []
    for k in ch2:
        for tests,new in rules[board[k]]:
            if all(board[k+pos]==c for pos,c in tests ):
                changes.append((k,new))
                break;
    return changes

def run(board,rules,steps=1):
    changed = None
    for i in range(steps):
        changes = step(board,rules,changed)
        for k,new in changes:
            board[k]=new
        changed = [change[0] for change in changes]
        if not changed:
            break
