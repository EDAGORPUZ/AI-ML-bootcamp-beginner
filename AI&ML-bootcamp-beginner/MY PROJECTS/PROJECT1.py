### 1. Simple Forecast Model – Salary Prediction
##Purpose: To build a model that predicts a person's salary based on their years of experience.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


df = pd.read_csv('project1.csv')

X = df[['Experience']]
y = df['Salary']

x_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(X_test)

plt.scatter(X, y, color = 'k')
plt.plot(X, model.predict(X), color = 'b')
plt.grid(True)
plt.show()

#extra
print('\n Real and estimated salaries')
for real, esimate in zip(y_test, y_pred):
    print(f"real: {real}  -->  esimate: {esimate}")

print("\nModel formülü: Salary = ", model.coef_[0], "* Experience +", model.intercept_)

