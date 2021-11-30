## Writing a parser was a mistake

f = open("input")

class X:
    def __init__(self,v):
        self.v=v
    def __mul__(self,other):
        return X(self.v+other.v)
    def __sub__(self,other):
        return X(self.v*other.v)
    def __add__(self,other):
        return X(self.v+other.v)

def evl(x):
    s=""
    for c in x:
        if c=="*": s+="-"
        elif c=="+": s+="*"
        elif c in "1234567890":
            s+="X("+c+")"
        else:
            s+=c
    return eval(s)
s=0
for line in f:
    s+=evl(line).v

print(s)
