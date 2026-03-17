import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib

df = pd.read_csv("train.csv")

# Fill missing values
df['Item_Weight'].fillna(df['Item_Weight'].mean(), inplace=True)
df['Outlet_Size'].fillna(df['Outlet_Size'].mode()[0], inplace=True)

# Convert categorical
df = pd.get_dummies(df)

X = df.drop('Item_Outlet_Sales', axis=1)
y = df['Item_Outlet_Sales']

model = RandomForestRegressor()
model.fit(X, y)

joblib.dump(model, "model.pkl")
joblib.dump(X.columns, "columns.pkl")

print("Model ready!")