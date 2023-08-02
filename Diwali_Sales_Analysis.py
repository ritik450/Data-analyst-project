#!/usr/bin/env python
# coding: utf-8

# In[42]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[43]:


df= pd.read_csv(r'C:\Users\LENOVO\Downloads\Diwali Sales Data.csv',encoding='unicode_escape')


# In[44]:


df.shape


# In[45]:


df.head()


# In[46]:


df.info()


# In[47]:


#drop null columns

df.drop(['Status','unnamed1'],axis=1,inplace=True)


# In[48]:


df.isnull()


# In[49]:


df.isnull().sum()


# In[50]:


#drop null values

df.dropna(inplace=True)


# In[51]:


#change data type

df['Amount']=df['Amount'].astype('int')


# In[52]:


df['Amount'].dtypes


# In[53]:


df.columns


# In[54]:


df.describe()


# # Gender

# In[99]:


ax=sns.countplot(x='Gender',data=df)
sns.set(rc={'figure.figsize':(2,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[98]:


sales_gen=df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.set(rc={'figure.figsize':(5,5)})
sns.barplot(x='Gender',y='Amount',data=sales_gen)


# # from above graph we can see that most of the buyurs are female and even purchasing power  of females are greater than men
# 

# # Age

# In[60]:


ax=sns.countplot(x='Age Group',data=df,hue='Gender')
for bars in ax.containers:
   ax.bar_label(bars)


# In[61]:


#Total Amount vs Age Group

sales_age= df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x='Age Group',y='Amount',data=sales_age)


# From the above graph we can see that most of buyurs are of age group between 26-35 yrs female

# # State 

# In[67]:


# total no of orders from top 10 states

sales_state=df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
sns.set(rc={'figure.figsize':(25,5)})
sns.barplot(x='State',y='Orders',data=sales_state)


# In[65]:


# Total amount /sales from top 10 states

sales_state=df.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.set(rc={'figure.figsize':(25,5)})
sns.barplot(x='State',y='Amount',data=sales_state)


# # From the above graphs we can see that mostof the orders & sales/amount are from Uttar Pradesh,Maharastra and Karnataka respectively

# # Marital Status

# In[96]:


ax=sns.countplot(x='Marital_Status',data=df)
sns.set(rc={'figure.figsize':(2,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[79]:


sales_state=df.groupby(['Marital_Status','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.set(rc={'figure.figsize':(7,5)})
sns.barplot(x='Marital_Status',y='Amount',data=sales_state ,hue="Gender")


# From the above graphs we can see that most of the buyurs are married Women and they have high purchasing power

# # Occupation

# In[77]:


ax=sns.countplot(x='Occupation',data=df)
sns.set(rc={'figure.figsize':(30,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[83]:


sales_state=df.groupby(['Occupation'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.set(rc={'figure.figsize':(30,5)})
sns.barplot(x='Occupation',y='Amount',data=sales_state)


# From the above Graphs we can see that  most of the buyurs are working in IT,Aviation and Healthcare sector

# # Product category

# In[89]:


ax=sns.countplot(x='Product_Category',data=df)
sns.set(rc={'figure.figsize':(30,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[93]:


sales_state=df.groupby(['Product_Category'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.set(rc={'figure.figsize':(30,5)})
sns.barplot(x='Product_Category',y='Amount',data=sales_state)


# From the bove graphs we can see that most of sold products are from Food, Clothing and electronics category

# # Conclusion:

# 
# 
# Married Women age group 26-35 years from Up,Maharastra and Karnatake working in IT,Healthcare and Aviation are more likely to buy products from Foods ,Clothing and Electronics Category
