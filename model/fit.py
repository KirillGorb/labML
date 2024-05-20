
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

data_df = pd.read_excel('dataset.xlsx')
label_encoder = LabelEncoder()
data_df["diploma"]=label_encoder.fit_transform(data_df["diploma"])
X=data_df.drop(["diploma"],axis=1)
Y=data_df["diploma"]
X_train1,X_test1,Y_train1,Y_test1=train_test_split(X,Y,test_size=0.3,random_state=3)
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train1, Y_train1)
y_pred = model.predict(X_test1)

df = pd.DataFrame({'y_pred': y_pred,
                   'Y_test1': Y_test1})
with open('AI.ist', 'wb') as pkl:
    pickle.dump(model, pkl)