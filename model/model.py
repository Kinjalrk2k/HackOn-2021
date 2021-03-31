import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle


from constants import COLUMNS
from encode import encode
from clean import clean

df = pd.read_csv("data.csv")
df = clean(df)

X = df.drop('work_interfere', axis=1)
y = df['work_interfere']

X = encode(X)

forest = RandomForestClassifier(n_estimators=100, random_state=28, max_depth=5)
forest_model = forest.fit(X, y)

filename = 'model.sav'
pickle.dump(forest_model, open(filename, 'wb'))
