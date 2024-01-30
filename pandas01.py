# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:31:38 2024

@author: SteynAS
"""

import pandas

file = pandas.read_csv("insurance_data.csv", skiprows=5)

print(file)

file.info()

