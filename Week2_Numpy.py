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

# empty is dangerous because it gives us random number, and we might use them by mistake.

#Task 4:

print(np.arange(10,30,5))
print(np.linspace(0,2,9))

#Floating-point precision:  As computers can not save some decimals perfectly so it is going to round them a bit so tiny mistake can happen
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

# In Numpy * multiplies each number by the one in the sane place. For matrix multiplication we use @.

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
# Masking is better because it uses one line instead of many and it is faster.


#Task 9:
def f(x, y):
    return 10 * x + y
b = np.fromfunction(f, (5, 4), dtype=int)
print(b[:, 1])
print(b[1:3, :])

