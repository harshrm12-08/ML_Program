# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 20:21:01 2021

@author: harsh
"""

#Import Libraries----------
import numpy as np 
import pandas as pd 
from mlxtend.frequent_patterns import apriori, association_rules 

#Loading and exploring the data-----------------
#Loading the Data 
data = pd.read_excel('C:/Users/harsh/Desktop/SKILL_Edge/DataFile/Online_Retail_Store.xlsx') 
data.head() 
data.info()
# Exploring the columns of the data 
data.columns 
# Exploring the different regions of transactions 
data.Country.unique() 

#Cleaning the Data-----------------
#Identifying missing values:
'''Is there any missing values across columns'''
data.isnull().any()

'''How many missing values are there across each column'''
data.isnull().sum()

# Dropping the rows without any invoice number 
data.dropna(axis = 0, subset =['InvoiceNo'], inplace = True) 
data.isnull().sum()

# Dropping all transactions which were done on credit ('C')
#  ~ = tilda
data.info() 
data = data[~data['InvoiceNo'].str.contains('C')]
#For the above cmd to work, we need to ensure that we convert Column "Invoinve No." to string form.
data['InvoiceNo'] = data['InvoiceNo'].astype('str') 
  
#Hence, now we have been able to remove the rows with credit (C) type billing.

# Stripping extra spaces in the description 
# Extra spaces create problems when there is one invoice but different products

data['Description'] = data['Description'].str.strip()

#Splitting the data according to the region of transaction-------
# Transactions done in France 
basket_France = (data[data['Country'] =="France"] 
		.groupby(['InvoiceNo', 'Description'])['Quantity'] 
		.sum().unstack().reset_index().fillna(0) 
		.set_index('InvoiceNo')) 

# Transactions done in the United Kingdom 
basket_UK = (data[data['Country'] =="United Kingdom"] 
		.groupby(['InvoiceNo', 'Description'])['Quantity'] 
		.sum().unstack().reset_index().fillna(0) 
		.set_index('InvoiceNo')) 

# Transactions done in Portugal 
basket_Por = (data[data['Country'] =="Portugal"] 
		.groupby(['InvoiceNo', 'Description'])['Quantity'] 
		.sum().unstack().reset_index().fillna(0) 
		.set_index('InvoiceNo')) 

# Transaction done in Sweden
basket_Sweden = (data[data['Country'] =="Sweden"] 
		.groupby(['InvoiceNo', 'Description'])['Quantity'] 
		.sum().unstack().reset_index().fillna(0) 
		.set_index('InvoiceNo')) 

data.Country.unique()

# Transaction done in Germany
basket_Germany = (data[data['Country'] =="Germany"] 
		.groupby(['InvoiceNo', 'Description'])['Quantity'] 
		.sum().unstack().reset_index().fillna(0) 
		.set_index('InvoiceNo')) 

# Transaction done in Japan
basket_Japan = (data[data['Country'] =="Japan"] 
		.groupby(['InvoiceNo', 'Description'])['Quantity'] 
		.sum().unstack().reset_index().fillna(0) 
		.set_index('InvoiceNo'))

# Transaction done in Netherland
basket_netherland = (data[data['Country'] == "Netherlands"]
                      .groupby(['InvoiceNo', 'Description'])['Quantity']
                      .sum().unstack().reset_index().fillna(0)
                      .set_index('InvoiceNo'))



#Hot encoding the Data------------
# Defining the hot encoding function to make the data suitable 
# for the concerned libraries 
def hot_encode(x): 
	if(x<= 0): 
		return 0
	if(x>= 1): 
		return 1

# Encoding the datasets 
basket_encoded = basket_France.applymap(hot_encode) 
basket_France = basket_encoded 

basket_encoded = basket_Germany.applymap(hot_encode) 
basket_Germany = basket_encoded 

basket_encoded = basket_Por.applymap(hot_encode) 
basket_Por = basket_encoded 

basket_encoded = basket_Sweden.applymap(hot_encode) 
basket_Sweden = basket_encoded 

#Building the models and analyzing the results-----------------

#France:
# Building the model 
frq_items = apriori(basket_France, min_support = 0.1, use_colnames = True) 
frq_items

# Collecting the inferred rules in a dataframe 
rules = association_rules(frq_items, metric ="lift", min_threshold = 1) 
print(rules.head()) 
France_rules=pd.DataFrame(rules)

#Portugal
frq_items = apriori(basket_Por, min_support = 0.15, use_colnames = True) 
rules = association_rules(frq_items, metric ="lift", min_threshold = 1) 
print(rules.head()) 
Portugal_rules=pd.DataFrame(rules)

#Sweden
frq_items = apriori(basket_Sweden, min_support = 0.10, use_colnames = True) 
rules = association_rules(frq_items, metric ="lift", min_threshold = 1) 
print(rules.head()) 
Sweden_rules=pd.DataFrame(rules)

#Germany
frq_items = apriori(basket_Germany, min_support = 0.05, use_colnames = True) 
rules = association_rules(frq_items, metric ="lift", min_threshold = 1) 
print(rules.head()) 
Germany_rules=pd.DataFrame(rules)  

#Here Empty DataFrame signifies that none of the Rules in UK satisfy the levels mentioned for 
#Support & Lift in above freq items sets