# -*- coding: utf-8 -*-
"""
Created on Mon May 17 11:35:13 2021

@author: harsh
"""

#-------------------------Reading & Writing data in Files----------------------

import pandas

# Reading CSV Files with Pandas:
df = pandas.read_csv('C:/Users/harsh/Desktop/SKILL_Edge/DataFile/User_Data.csv')
print(df)

# Writing CSV Files with Pandas:
df.to_csv('C:/Users/harsh/Desktop/SKILL_Edge/DataFile/User_Data_write.csv')

# Reading Excel Files with Pandas
df1 = pandas.read_excel('C:/Users/harsh/Desktop/SKILL_Edge/DataFile/User_Data.xlsx')
df1.head(2) #It is used to give number of rows from the data 

df1 = pandas.read_excel('User_Data.xlsx')
print(df1)
df1.describe()


# Writing Excel Files with Pandas 
df1.to_excel('User_Data_write.xlsx')
df2 = pandas.DataFrame(df1)
print (df2)

df2.describe()

import numpy as np
df2.describe(include=[np.object])


new_df = pandas.read_excel('C:/Users/harsh/Desktop/DataFiles/Marathalli Branch.xls')
new_df.describe()



store = new_df.to_csv('C:/Users/harsh/Desktop/DataFiles/Marathalli_Branch_comma.csv')

