import pickle
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd

dataset = pd.read_excel('dataset.xlsx')
x1 = np.array(dataset['age'])
x2 = np.array(dataset['education'])
x3 = np.array(dataset['sports'])
y = np.array(dataset['diploma'])

y = LabelEncoder().fit_transform(y)

x1 = preprocessing.normalize([x1])
x2 = preprocessing.normalize([x2])
x3 = preprocessing.normalize([x3])
y = preprocessing.normalize([y])

df = np.array([x1+x2+x3])
df = df.reshape(-1, 1)
y = y.reshape(-1, 1)
model = LinearRegression()
model.fit(df, y)
with open('AI.ist','wb') as pkl:
    pickle.dump(model, pkl)