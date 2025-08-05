from sklearn.linear_model import LinearRegression

X_train = [[10], [20], [30], [40], [50]]
y_train = [100, 200, 300, 400, 500]

model = LinearRegression()
model.fit(X_train, y_train)

print("suggest for 55:", model.predict([[55]])[0])
