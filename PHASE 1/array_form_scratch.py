import numpy as np

zeroes = np.zeros((3,4))
print(zeroes)
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

ones = np.ones((3,4))
print(ones)
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]]

full = np.full((2,2),4)
print(full)
# [[4 4]
#  [4 4]]

random = np.random.random((2,3))
print(random)
# [[0.08992409 0.68016053 0.93024898]
#  [0.33990816 0.06724547 0.40129221]]

seq = np.arange(0,10,2)
print(seq)
# [0 2 4 6 8]
