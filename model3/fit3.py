from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import pickle
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd

dataset = pd.read_excel("dinrent.xlsx")
x1 = np.array(dataset['age'])
x2 = np.array(dataset['education'])
x3 = np.array(dataset['sports'])
y = np.array(dataset['rez'])

le = LabelEncoder()
y = le.fit_transform(y)

x1 = preprocessing.normalize(x1.reshape(-1, 1))
x2 = preprocessing.normalize(x2.reshape(-1, 1))
x3 = preprocessing.normalize(x3.reshape(-1, 1))

df = np.hstack((x1, x2, x3))

X_train1, X_test1, Y_train1, Y_test1 = train_test_split(df, y, test_size=0.2, random_state=3)
model = DecisionTreeClassifier(criterion="entropy")
model.fit(X_train1, Y_train1)
tree.plot_tree(model, class_names=True)
class_names = dataset['rez']
tree.plot_tree(model, class_names=class_names)
with open('AI.ist', 'wb') as pkl:
    pickle.dump(model, pkl)
