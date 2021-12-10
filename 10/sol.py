from collections import defaultdict
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"

f=list(open(fname))

d=defaultdict(int)

r=[]
s=0
scs={
    ")": 1 ,
"]": 2 ,
"}": 3,
">": 4
    }
ss=[]
for y,line in enumerate(f):
    #l=list(map(int,"".join(c if c in "1234567890-" else " " for c in line).split()))
    #r.append(l)
    #for x,c in enumerate(line.strip()):
    #    d[(x+1j*y)]=int(c)+1
    stack=[]
    #print(line)
    for c in line:
        if c in "([{<":
            stack.append(c)
        elif c in ")]}>":
            if stack.pop()!="([{<"[")]}<".find(c)]:
                break
                #s+=scs[c]
    else:
        print(stack)
        s=0
        for c in reversed(stack):
            s*=5
            s+=scs[")]}>"["([{<".find(c)]]
        ss.append(s)
        print(s)
    r.append(line)
print(ss)
print(sorted(ss)[len(ss)//2])
#print(s)
