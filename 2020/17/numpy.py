
from time import time
import numpy as np
from itertools import product
from math import log
t=time()
f = open("input")
l = [x[:-1] for x in f]


grid = np.zeros((8,8,1,1))

for y,r in enumerate(l):
    for x,c in enumerate(r):
        if c=="#":
            grid[x,y,0,0]=1

res=[log(sum(sum(sum(sum(grid)))))]
for i in range(30):
    neighbourCount = np.zeros(tuple(x+2 for x in grid.shape))
    for ds in product([-1,0,1],repeat=4):
        neighbourCount[tuple(slice(1+d,1+d+s) for d,s in zip(ds,grid.shape))]+=grid
    survived = np.zeros(neighbourCount.shape)
    survived[tuple(slice(1,k+1) for k in grid.shape)] = grid*(neighbourCount[tuple(slice(1,k+1) for k in grid.shape)]==4)
    grid = 1*(neighbourCount==3)+survived
    print(log(sum(sum(sum(sum(grid))))))
    res.append(log(sum(sum(sum(sum(grid))))))
    

print(sum(sum(sum(sum(grid)))),time()-t)

import matplotlib.pyplot as plt

plt.plot(res)
plt.show()
