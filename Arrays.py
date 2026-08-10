import numpy

def arrays(arr):
    return numpy.array(arr, float)[::-1] #.reverse() is not a function for numpy arrays (list), but [::-1] will reverse the array.

arr = input().strip().split(' ')
result = arrays(arr)
print(result)