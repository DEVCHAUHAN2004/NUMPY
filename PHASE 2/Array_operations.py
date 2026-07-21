import numpy as np

arr = np.arange(10)
print(arr)
# [0 1 2 3 4 5 6 7 8 9]

print(arr[2:8])
# [2 3 4 5 6 7]

print(arr[1:8:2])
# [1 3 5 7]

print(arr[-3])
# 7

arr_2d = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]
                  ])
print(arr_2d[1,2])
print(arr_2d[1])
print(arr_2d[:,1])
# 6
# [4 5 6]
# [2 5 8]

