#!/usr/bin/env python
# coding: utf-8

# NeenOpal Assessment (Python)

# In[3]:


import pandas as pd


# In[9]:


# Q1) Read the CSV File. 
df = pd.read_csv(r'\\mdibkstorage\DataAnalytics&Infographics\PRojects\Pruthviraj\test assessment\used_bikes.csv')


# In[10]:


# Top 5 rows in the CSV file to check the proper loading of the data 
df.head()


# In[11]:


# As per specified , the data is dumped daily, therefore indexes are reseted using reset index function in pandas
df.reset_index(drop=True, inplace=True)


# In[12]:


# top 5 rows after the reset in index
df.head()


# In[13]:


# List of the column names present in the data 
df.columns


# In[16]:


# Checking the data type of each column
df.info()


# In[17]:


# Statistical description of the data in the csv
df.describe()


# In[18]:


#Q2) Checking the memory usage of the column data types.
print("Memory usage before change:")
print(df.memory_usage(deep=True))


# In[25]:


# selecting the float type columns to convert into the int type.
columns_to_convert = ['price', 'kms_driven', 'age'] 


# In[26]:


# Typecasting the float columns into integer type to reduce the memory usage.
df[columns_to_convert] = df[columns_to_convert].astype(int)


# In[27]:


# checking the data frame information after changing the data types.
df.info()


# In[28]:


# Checking the memory usage of the data columns after the type conversion.
print("Memory usage after change:")
print(df.memory_usage(deep=True))


# In[ ]:


# Conclusion : Int type columns consums less memory rather than float type columns.


# To dump the data in mysql connection 

# In[ ]:


# Importing libraries from pandas to connect with the data base and upload the data in mysql
import mysql.connector
from sqlalchemy import create_engine


# In[ ]:


conn = mysql.connector.connect(
    host='your_host',
    user='your_username',
    password='your_password',
    database='your_database_name'
)


# In[ ]:


table_name = 'Bike Details'

# Engine is created by mysql alchemy 
engine = create_engine('mysql+mysqlconnector://username:your_password@your_host/your_database_name')

# Dump the DataFrame into the MySQL database table
df.to_sql(table_name, con=engine, if_exists='replace', index=False)


# In[ ]:


index_query = "CREATE INDEX index_name ON " + Bike Details + " (bike_name)"


# In[ ]:


cursor = conn.cursor()
cursor.execute(index_query)

# To Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()

