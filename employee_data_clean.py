import numpy as np
import pandas as pd

df = pd.read_csv(r'C:\Users\asus\OneDrive\Desktop\NUMPY\employee_dataset_300_rows.csv')
print(df.head())
#    Emp_ID        Name   Age  Salary_INR  Experience_Years       City  Department  Performance_Rating
# 0     101  Alok Mehta  43.0    380000.0               4.0  Hyderabad  Management                 3.2
# 1     102  Meera Nair  47.0    980000.0              10.0      Delhi     Finance                 4.7
# 2     103  Meera Nair   NaN         NaN               7.0      Kochi       Sales                 4.8
# 3     104  Alok Mehta  38.0         NaN               NaN    Chennai          IT                 3.8
# 4     105  Meera Nair  48.0   1100000.0              28.0      Delhi  Operations                 4.2


# check mising values
print('missing values in the csv file')
print(df.isnull().sum())
# missing values in the csv file
# Emp_ID                 0
# Name                   0
# Age                    9
# Salary_INR            17
# Experience_Years      20
# City                   0
# Department             0
# Performance_Rating    25