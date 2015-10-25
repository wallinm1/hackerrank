from scipy.stats import mode
import numpy as np
N = int(raw_input())
numbers = map(float, raw_input().split())
mn = np.mean(numbers)
sd = np.std(numbers)
print round(mn, 1)
print round(np.median(numbers), 1)
print int(mode(numbers)[0])
print round(sd, 1)
print round(mn - (1.96)/(np.sqrt(N))*sd, 1), round(mn + (1.96)/(np.sqrt(N))*sd, 1)