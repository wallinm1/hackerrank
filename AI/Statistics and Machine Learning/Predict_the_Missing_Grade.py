import json, sys
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier, ExtraTreesClassifier, RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
with sys.stdin as f:
    next(f)
    df_test = pd.DataFrame(json.loads(line) for line in f)
with open('training.json', 'r') as f:
    next(f)
    df_train = pd.DataFrame(json.loads(line) for line in f)
ytrain = df_train.Mathematics.values
df_train.drop(['Mathematics', 'serial'], axis = 1, inplace = True)
df_train.fillna(df_train.mean(), inplace = True)
df_test.drop(['serial'], axis = 1, inplace = True)
df_test.fillna(df_test.mean(), inplace = True)
xtrain = df_train.values
xtest = df_test.values
scaler = StandardScaler()
xtrain = scaler.fit_transform(xtrain)
xtest = scaler.transform(xtest)
#model = LogisticRegression(random_state = 42)
#model = GradientBoostingClassifier(random_state = 42, n_estimators = 25)
#model = RandomForestClassifier(random_state = 42, n_estimators = 75)
model = RandomForestRegressor(random_state = 42, n_estimators = 50)
#model = ExtraTreesClassifier(random_state = 42, n_estimators = 100)
#model = LinearSVC(random_state = 42)
model.fit(xtrain, ytrain)
predictions = model.predict(xtest)
for pred in predictions:
    print int(round(pred))