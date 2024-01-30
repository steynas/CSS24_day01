# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:41:48 2024

@author: SteynAS
"""

"""
Storing data in Python:
    1. Lists
    2. Dictionaries
    3. Data frames
"""

import pandas

file = pandas.read_csv("country_data.csv")

print(file)

# Storing Data
B1 = 30
B2 = 40
B3 = 30
B4 = 49

print(B1)
print(B2)

age = [20,25,30,35,40,45,50]

print(age)

print(age[0])
print(age[1])
print(max(age))
print(len(age))
ave=sum(age)/len(age)
print(ave)
print(age[0:2])

age.append(100)
print(age)

# Data Storage With Lists
my_list = [42, -2021, 6.283,"tau", "node"]
print(my_list)

d = {'key1': 'value1', 'key2': 'value2'}

person = {'name': 'John Doe', 'age': 30, 'address': '123 Main St.'}
print(person['name']) # 'John Doe'
print(person.get('age')) # 30
person['phone'] = '555-555-5555'

import pandas as pd

# Creating a DataFrame
data = {
    'age': [30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39],
    'gender': ["M", "M", "F", "M", "F", "F", "F", "M", "M", "F", "M"],
    'country': ["South Africa", "Botswana", "South Africa", "South Africa", "Kenya", "Mozambique", "Lesotho", "Kenya", "Kenya", "Egypt", "Sudan"]
}

#df = data frame
df = pd.DataFrame(data)

# Displaying the DataFrame
print(df)
print(df.describe())

# Adding a new column
df['infected']= [1,0,1,1,1,0,0,0,1,1,0]
print(df)

# Removing a column
df.drop(columns=['gender'], inplace=True)
print(df)