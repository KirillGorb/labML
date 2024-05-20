import pandas as pd
import numpy as np

N = 1000
age = np.random.randint(15, 20, size=N)
education = np.random.randint(20, 50, size=N)
sports = np.random.randint(0, 30, size=N)
y = np.random.randint(0, 2, size=N)

X = np.column_stack((age, education, sports))

data = {'age': age, 'education': education, 'sports': sports, 'diploma': y}
df = pd.DataFrame.from_dict(data)

df.to_excel('dataset.xlsx', index=False)