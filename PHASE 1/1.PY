import numpy as np

arr_1d = np.array([1,2,3,4,5,6])
print(arr_1d)
# [1 2 3 4 5 6]

arr_2d = np.array([[1,2,3],[4,5,6]])
print(arr_2d)
# [[1 2 3]
#  [4 5 6]]


py_list = [7,8,9]
print(py_list * 2)
# [7, 8, 9, 7, 8, 9]

np_array = np.array([1,2,3])
print(np_array * 2)
# [2 4 6]


import time
import numpy as np

start = time.time()

np_array = np.arange(10000) * 2

print(time.time() - start)
# 5.173683166503906e-05

