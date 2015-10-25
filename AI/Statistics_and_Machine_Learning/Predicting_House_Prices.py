import numpy as np
from sklearn.linear_model import LinearRegression
F, N = [ int(i) for i in raw_input().strip().split() ]
xtrain = []
for i in range(N):
    xtrain.append(map(float, raw_input().split()))
T = int(raw_input())
xtest = []
for i in range(T):
    xtest.append(map(float, raw_input().split()))
xtrain = np.array(xtrain)
ytrain = xtrain[:, -1]
xtrain = xtrain[:, :-1]
xtest = np.array(xtest)
lr = LinearRegression().fit(xtrain, ytrain)
preds = list(lr.predict(xtest))
for pred in preds:
    print pred