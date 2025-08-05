import numpy as np

a = np.array([0, 1, 2, 3, 4, 5, 6])

print('array a: ', a)
print('a + 2: ', a + 2)
print('a * 2: ', a * 2)
print('squares of a:', a ** 2)

b = np.array([[0, 1], [3, 6], [6, 5]])

print(b)   #numpy özelliğinden dolayı matris gibi alt alta yazıldı.
print('2 dimensional b: \n', b)
print('transpoze of b: \n', b.T)


print('array 0: \n', np.zeros([5, 6]))
print('identity matris: \n', np.eye(3))
print('random numbers: \n', np.random.rand(6))

c = np.array([55, 56, 57, 58])
print('mean of c:', np.mean(c))
print('standard deviation:' , np.std(c))
print('total:', np.sum(c))


d = np.array([45, 46 , 47, 48, 49, 50])
print('3 numbers from the beggining:', d[ :3])
print('2 numbers from the end: ', d[-2:])
print('numbers greater than 48: ', d[d>48])


#TASK 1 = create a 3x3 matrix.
e = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(e)

#TASK 2 = print the row and coloumn averages of this matrix.
print('1st row average: ',np.mean(e[0]))
print('2nd row average ',np.mean(e[1]))
print('3rd row average ',np.mean(e[2]))
print('1st coloumn average: ', np.mean(e[0][0]))

#TASK 3 = create an array of random numbers between 0 and 100 and find numbers greater than 50.
f = np.random.randint(0, 100, 10)  #generate array of 10 random numbers between 0 and 100
print(f)
print('average of the array f: ', np.mean(f))
print('numbers greater than 50 in array f: ', f[f>50])

g = np.random.randint(0, 50, (4,3))  #generate array of shape(4, 3) with random numbers between 0 and 50
print(g)


