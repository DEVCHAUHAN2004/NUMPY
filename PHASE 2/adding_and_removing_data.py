import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

concatenate = np.concatenate((arr1,arr2))
print(concatenate)
# [1 2 3 4 5 6]

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr3 = np.array([7,8,9])
print(arr1.shape == arr2.shape)
# True


orignal = np.array([[1,2],[3,4]])
new_row = np.array([7,8])

with_new_row = np.vstack((orignal,new_row))
print(orignal)
# [[1 2]
#  [3 4]]
print(with_new_row)
# [[1 2]
#  [3 4]
#  [7 8]]

arr = np.array([1,2,3,4,5,6])
deleted = np.delete(arr,3)
print(deleted)
# [1 2 3 5 6]



