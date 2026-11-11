# Week2 Lecture Activity
import numpy as np

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d)

print(arr2d [:,2:])

print(arr2d[1,1:])

#Tutorial 2.1

a=np.array([2,3,4])
print(a)
print(a.dtype)
b=np.array([1.2,3.5,5.1])
print(b.dtype)

#Numpy needs all numbers to be the same type.This makes it fast.

#Task 2:
c = np.array([[1,2],[3,4]],dtype=complex)
print(c)

# ndarray: NumPy's box of numbers.
# shap: How many rows and columns.
# dtype : what kind of data is inside.

#Task 3:
zeros = np.zeros((3,4))
print(zeros)
ones = np.ones((2,3), dtype = np.int16)
print(ones)
empty = np.empty((2,3))
print(empty)

# empty is dangerous because it gives us random number, and we might
# use them by mistake.

#Task 4:

print(np.arange(10,30,5))
print(np.linspace(0,2,9))

#Floating-point precision:  As computers can not save some decimals perfectly
# so it is going to round them a bit so tiny mistake can happen.

# Linspace is safer because we choose exactly how many number we get.


from numpy import pi
x=np.linspace(0,2 * pi , 100)
y = np.sin(x)
print(y)

a=np.array([20,30,40,50])
print(a)
b=np.arange(4)
print(b)

#Task 5:

print(a-b)
print(b ** 2)
print(10 * np.sin(a))

# In Numpy * multiplies each number by the one in the sane place.
# For matrix multiplication we use @.

#Task 6:
A = np.array([[1,1],[0,1]])
print(A)
B=np.array([[2,0],[3,4]])
print(B)
print(A * B)   #elementwise
print(A @ B) #matrix product

b = np.arange(12).reshape(3, 4)
print(b)

#Task 7:
print(b.sum(axis=0)) # column sums
print(b.min(axis=1) )# row minimums
print(b.cumsum(axis=1))


#Task 8:
a = np.arange(10) ** 3
print(a)
print(a[2])
print(a[2:5])
print(a[:6:2])
print(a[::-1])

print(a[a > 100])
# Masking is better because it uses one line instead
# of many and it is faster.


#Task 9:
def f(x, y):
    return 10 * x + y
b = np.fromfunction(f, (5, 4), dtype=int)
print(b[:, 1])
print(b[1:3, :])

#Task 10:
a = np.floor(10 * np.random.random((3, 4)))
print(a.shape)
print(a.ravel())
print(a.reshape(6, 2))
print(a.T)

# copy is a new array.If I change it, the old one does not change.
# View is the same array.If I change it the old one changes too.

print(a.reshape(6, -1))
# reshape with -1 : python works out that number for me.

# Task 11:
print(np.vstack((a, a)))
print(np.hstack((a, a)))
print(np.hsplit(a, 2))


sensor = np.array([
[21.5, 22.1, 21.9],
[20.9, 21.3, 21.0],
[22.4, 22.8, 23.0]
])
print(sensor.mean(axis=1))
print(sensor.max())
print((sensor-sensor.min())/ (sensor.max()-sensor.min()))
print(sensor > sensor.min())

data = np.random.randint(0, 100, size=(10, 5))
print(data.mean(axis=0))
centred = data - data.mean(axis=0)
print(centred)

print(data[data > data.mean()+data.std()])

#column means: column 5 has the lowest average.

#zero-centre the data: negative numbers are below
# their column's average the positive numbers are above it.

# extract value > 1 standard deviation: There are the very
# high numbers , all close to 99.


#1. Panda is built on top of NumPy. Pandas table use NumPy array inside so
#understanding NumPy makes pandas easier to learn.


#2.Masking and vectorized operations replaced a loop. one line did the work of many lines.

#3.Machine learning uses a lots of numbers. NumPy makes it fast
#to do maths on big grids of numbers, like normalized data.


#Tutorial: 2.2


#Task 1:
scores = np.array([
[55, 62, 71, 68],
[78, 85, 88, 90],
[45, 50, 48, 52],
[90, 92, 94, 96],
[60, 65, 70, 75]
])
print(scores.shape)
# There are 5 Students and 4 assessments.

#Task 2:
print(scores.mean(axis=1))
print(scores.mean(axis=0))

#Task 3:
print(np.sum (np.all (scores>=40 , axis=1)))


#Task 4:

avg = scores.mean(axis=1)
print(avg>=70)
print(avg[avg>=70])

#Task 5:
print((scores-scores.min())/ (scores.max() - scores.min()))

#Task 6:
print(scores[scores>scores.mean()])
print(np.sum(scores > scores.mean()))

#Task 7:
#Because NumPy does maths on the whole grid at once with no loops and it is faster.
#Task 5 ( normalizing) would be the hardest because I would need loops to change every numbers one by one.
