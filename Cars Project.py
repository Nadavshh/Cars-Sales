#!/usr/bin/env python
# coding: utf-8

# In[101]:


import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()


# # Load The Data

# In[167]:


df = pd.read_csv(r'C:\Users\nadav\OneDrive\שולחן העבודה\Car_sales.csv')
df.head()


# ## Change the date to Correct data

# In[169]:


df['Latest_Launch'] = pd.to_datetime(df['Latest_Launch'])
df.head()


# In[65]:


df.info()


# ## Statistics 

# In[66]:


df.describe().T


# #### The mean price of all cars is 27,390 $
# 
#     

# # Checking The Data For nulls , duplicates And Change Them 

# In[67]:


df.isnull().sum()


# In[68]:


df.fillna(0, inplace=True)


# In[69]:


df.isnull().sum().sum()


# In[70]:


df.duplicated().sum()


# In[128]:


plt.figure(figsize=(16,6))
sns.scatterplot(x="Horsepower",
                y="Sales_in_thousands",
                color='indigo',
                data=df)
plt.title("Correlation between Horse Power and Sales",
          size=18,
          fontweight='bold')
plt.xticks(size = 14)
plt.yticks(size = 14)

plt.show()


# In[143]:


plt.figure(figsize=(16,6))
sns.scatterplot(x="Engine_size",
                y="Sales_in_thousands",
                color='indigo',
                data=df)
plt.title("Correlation between Engine Size and Sales",
          size=18,
          fontweight='bold')
plt.xticks(size = 14)
plt.yticks(size = 14)
plt.show()


# ## Making A groupby For Manufacturer	

# In[73]:


df_grouped_by= df.groupby(['Manufacturer']).sum().sort_values('Sales_in_thousands',ascending=False)
df_grouped_by = df_grouped_by.drop('__year_resale_value', 1)
df_grouped_by.head()


# In[125]:


ax = df_grouped_by['Sales_in_thousands'].plot.bar(color='indigo',figsize=(16,6))
ax= plt.title('Sales Per Manufacturer (2008-2012)',size= 18, fontweight='bold')
ax = plt.xlabel('Manufacturer', size = 13)
ax=plt.ylabel('Sales_in_thousands',size = 13)
ax =sns.despine(left=True)
ax = plt.xticks(rotation=45)


# #### As we can see Ford is The Most seller Company for the years 2008-2012 With sales of 2,022,635 \$
# 
#     
# 

# In[104]:


df1=df[['Manufacturer','Model','Sales_in_thousands']]
df1
df2=df1.loc[df['Manufacturer'].str.contains('Ford')].sort_values('Sales_in_thousands', ascending=False)
df2


# In[126]:


plt.figure(figsize=(16,6))
sns.set_style('white')
plt.bar(x = df2['Model'],
       height = df2['Sales_in_thousands'],
       color = 'indigo')
plt.xticks(fontsize = 11)
plt.yticks(fontsize = 11)
plt.title('Most-Selled Model (Ford)', fontsize= 18 , fontweight='bold')
plt.ylabel('Sales_in_thousands', fontsize= 13)
plt.xlabel('Model',fontsize= 13)
plt.xticks(rotation=45)
sns.despine(left=True)
plt.show()


# #### The Most Selled Model Of Ford is "F-Series" With Total Sales of 540,561 \$
# 
#     

# In[166]:



plt.figure(figsize=(16,6))
sns.histplot(df["Price_in_thousands"], color='indigo')
plt.title("Count of Cars per Price", size=18,fontweight='bold')
plt.xlabel("Price", size=13)
plt.ylabel("Count",size=13)
sns.despine(left=True)
plt.show()


# In[164]:


df3 = pd.DataFrame(df)
plt.figure(figsize=(16,6))
plt.title("Correlation Between All Variables", size=18,fontweight='bold')
corrMatrix = df3.corr()
sns.heatmap(corrMatrix, annot=True)
plt.show()


# In[ ]:




