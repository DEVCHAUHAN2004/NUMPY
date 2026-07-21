import numpy as np

arr = np.array([8,4,9,6,9,2,5,4,7])
print(np.sort(arr))
# [2 4 4 5 6 7 8 9 9]

arr_2d_unsorted = np.array([[5,3],[8,6],[3,4]])
print(np.sort(arr_2d_unsorted,axis = 0))
# [[3 3]
#  [5 4]
#  [8 6]]



arr_2d_unsorted = np.array([[5,3],[8,6],[3,4]])
print(np.sort(arr_2d_unsorted,axis = 1))
# [[3 5]
#  [6 8]
#  [3 4]]

numbers = np.array([1,2,3,4,5,6,7,8,9,10])
even_number = numbers[numbers % 2 == 0]
print(even_number)
# [ 2  4  6  8 10]


result = np.where(numbers > 7)
print(numbers[result])
# [ 8  9 10]



