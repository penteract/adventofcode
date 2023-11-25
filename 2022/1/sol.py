import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"
f=list(open(fname))

from collections import defaultdict

d=defaultdict(int)
xs=[0]

for line in f:
    if line.strip():
        xs[-1]+=(int(line))
    else:
        xs.append(0)

ys=sorted(xs)
print(sum(ys[3:]))
res = max(x for x in xs)

print(res)

try:
    xss = [list(map(int(xs.split(",")))) for xs in f]
except Exception:
    pass

ys=[[]]
for line in f:
    if line.strip():
        ys[-1].append(int(line))
    else:
        ys.append([])

open(sys.argv[2],mode="w").write("\n".join(",".join(map(str,xs)) for xs in ys))
