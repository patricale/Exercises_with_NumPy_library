import numpy as np

# Exercise 1: Creating and Manipulating Arrays
#   - Create a NumPy array of 10 random numbers between 0 and 100.
#   - Calculate the mean and standard deviation of the array.
#   - Find the maximum and minimum values ​​in the array.
#   - Add 5 to all elements of the array.
#   - Sort the array in ascending and descending order.

def init_array():
    x = np.random.randint(0, 101, size = 10)
    print("My array is: ", x)
    return x

def average(arr):
    return np.average(arr)

def standard_deviation(arr):
    return np.std(arr)

def findMax(arr):
    return np.max(arr)

def findMin(arr):
    return np.min(arr) 

def addFiveElem(arr):
    return arr + 5 

# Sorting in ascending order
def sortAsc(arr):
    return np.sort(arr)

# Sorting in descending order
def sortDes(arr):
    return np.sort(arr)[::-1]

def printArray(arr):
    print("Average is", average(arr))
    print("Dev. std. is %.3f" %standard_deviation(arr))
    print("Max value is", findMax(arr))
    print("Min value is", findMin(arr))
    print("Array + 5 is", addFiveElem(arr))
    print("Sort in ascending order is", sortAsc(arr))
    print("Sort in descending order is", sortDes(arr))

arr = init_array()
printArray(arr)