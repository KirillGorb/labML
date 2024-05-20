from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd

dataset = pd.read_excel("dataset.xlsx")
x1 = np.array(dataset['age'])
x2 = np.array(dataset['education'])
x3 = np.array(dataset['sports'])
y = np.array(dataset['diploma'])

le = LabelEncoder()
y = le.fit_transform(y)

df = np.array([x1, x2, x3]).T

X_train1, X_test1, Y_train1, Y_test1 = train_test_split(df, y, test_size=0.2, random_state=3)
model = LogisticRegression()
model.fit(X_train1, Y_train1)
with open('AI.ist', 'wb') as pkl:
    pickle.dump(model, pkl)