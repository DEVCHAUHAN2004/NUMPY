import numpy as np

v1 = np.array([1,2,3])
v2 = np.array([4,5,6])

print(v1 + v2)

print(v1 * v2)

print(np.dot(v1,v2))
# [5 7 9]
# [ 4 10 18]
# 32

restaurant = np.array(['biryani','burger','pizza'])

upper = np.vectorize(str.upper)
print(upper(restaurant))
# ['BIRYANI' 'BURGER' 'PIZZA']

