import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = [[10], [20], [30], [40], [50]]
y = [100, 200, 300, 400, 500]

model = LinearRegression()
model.fit(X, y)

plt.scatter(X, y, color='b')
plt.plot(X, model.predict(X), color = 'r')
plt.xlabel('input(x)')
plt.ylabel('output(y)')
plt.title('basic regression graph')

plt.show()
