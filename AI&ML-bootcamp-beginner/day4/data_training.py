from sklearn.model_selection import train_test_split

X = [[10], [20], [30], [40], [50], [60], [70], [80], [90], [100]]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)  
#p1, p2 = x, y    p3= %30 test  

print("X_train:", X_train)
print("X_test:", X_test)
print("y_train:", y_train)
print("y_test:", y_test)
