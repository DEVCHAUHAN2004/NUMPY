import numpy as np
import matplotlib.pyplot as plt

# Data structure: [restaurant_id, 2021, 2022, 2023, 2024]
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000],  # Paradise Biryani
    [2, 120000, 140000, 160000, 190000],  # Beijing Bites
    [3, 200000, 230000, 260000, 300000],  # Pizza Hub
    [4, 180000, 210000, 240000, 270000],  # Burger Point
    [5, 160000, 185000, 205000, 230000]   # Chai Point
])

print(sales_data.shape)
# (5, 5)

# 1st 3 restaurant sales
print(sales_data[:3])
# [[     1 150000 180000 220000 250000]
#  [     2 120000 140000 160000 190000]
#  [     3 200000 230000 260000 300000]]

# total sales per year
total_sales = np.sum(sales_data,axis=0)
print(total_sales)
# [     15  810000  945000 1085000 1240000]

# yearly total 
total_sales = np.sum(sales_data[:,1:],axis=0)
print(total_sales)
# [ 810000  945000 1085000 1240000]



# min sales per restaurant
min_sales = np.min(sales_data[:,1:],axis=1)
print(min_sales)
# [150000 120000 200000 180000 160000]

# max sales per year
max_sales = np.max(sales_data[:,1:],axis=0)
print(max_sales)
# [200000 230000 260000 300000]

# avearge sales per restaurant
avg_sales = np.mean(sales_data[:,1:],axis = 1)
print(avg_sales)
# [200000. 152500. 247500. 225000. 195000.]

cumulative_sum = np.cumsum(sales_data[:,1:],axis = 1)
print(cumulative_sum)
# [[150000 330000 550000 800000]
#  [120000 260000 420000 610000]
#  [200000 430000 690000 990000]
#  [180000 390000 630000 900000]
#  [160000 345000 550000 780000]]

plt.figure(figsize=(8,6))
plt.plot(np.mean(cumulative_sum,axis = 0))
plt.title("Avg cumulative sales")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.grid(True)

plt.show()
