import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
print(arr.shape)
print(arr.ndim)
print(arr.size)
print(arr.dtype)
# (2, 3)
# 2
# 6
# int64


arr = np.arange(12)
print(arr)
# [ 0  1  2  3  4  5  6  7  8  9 10 11]

reshapes = arr.reshape((3,4))
print(reshapes)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

transpose = reshapes.T
print(transpose)
# [[ 0  4  8]
#  [ 1  5  9]
#  [ 2  6 10]
#  [ 3  7 11]]



