##Create a simple model that estimates how much fuel a car consumes per 100 km based on its engine displacement (engine size, in liters).

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error  #for calculate the margin of error

df = pd.read_csv('PROJECT3.csv')

X = df[['EngineSize']]
y = df['FuelConsumption']

X_train , X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state=42)

modal = LinearRegression()
modal.fit(X_train, y_train)

plt.scatter(X, y, color ='b')
plt.plot(X, modal.predict(X), color = 'r' )
plt.grid()
plt.show()

#Extra: Calculate and print the estimated fuel consumption of the 1.8 litre engine.
print('suggest from 1.8 litre: ', modal.predict([[1.8]])[0])

#Extra: Calculate the model's prediction performance with Mean Absolute Error (MAE).
y_pred = modal.predict(X_train)
print('mae =', mean_absolute_error(y_train, y_pred))
