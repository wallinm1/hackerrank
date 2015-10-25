import pandas as pd
import sys
import numpy as np
df = pd.DataFrame(columns = ('yyyy', 'month', 'tmax', 'tmin'))
df_idx = 0
n = int(raw_input())
for line in sys.stdin:
    if line.startswith('yyyy'):continue
    df.loc[df_idx] = line.split()
    df_idx += 1
df.replace(r'Missing_', np.nan, regex = True, inplace = True)
df.tmax = df.tmax.astype(float)
df.tmin = df.tmin.astype(float)
df['diff'] = df.tmax - df.tmin
#dict with monthly mean differences in temperature
diffs_by_month = df.groupby(['month'])['diff'].mean().to_dict()
for row in df.values:
    year, month, tmax, tmin, diff = row
    if np.isnan(tmax):
        print tmin + diffs_by_month[month]
    elif np.isnan(tmin):
        print tmax - diffs_by_month[month]