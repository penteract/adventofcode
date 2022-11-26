
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"
f=list(open(fname))
lns=[]
for line in f:
    lns.append([])
    for a in line.split(","):
        if a.startswith("x"):
            pass
    print(line)
    

print(int(len(f[0])))
