import numpy as np
n = int(raw_input())
xtrain = []
for i in range(n):
    xtrain.append(map(float, raw_input().split()))
xtrain = np.array(xtrain)
math = xtrain[:, 0]
phys = xtrain[:, 1]
chem = xtrain[:, 2]
print round(np.corrcoef(math, phys)[0, 1], 2)
print round(np.corrcoef(phys, chem)[0, 1], 2)
print round(np.corrcoef(chem, math)[0, 1], 2)