#Create a simple Linear Regression model that predicts the price of a house based on its size (in square meters).

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('project2.csv')

X = df[['Size']]
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X_test)

print('\n real and esimated piceses')
for real, esimate in zip(y_train, y_pred ):
    print(f"REAL:  {real} -->  ESİMATE: {esimate}")
    
plt.scatter(X, y,  color = 'k')
plt.plot(X, model.predict(X), color = 'b')
plt.grid(True)
plt.show()


