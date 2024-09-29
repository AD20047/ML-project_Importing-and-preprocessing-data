import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

dataset = pd.read_csv('iris.csv')

X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values
print("Matrix of features(X)")
print(X)

print("\nDependent Variable vector y")
print(y)