#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[2]:


df  = pd.read_csv("student-mat.csv")
df.head()


# In[3]:


df.shape


# In[8]:


df.isnull().sum()


# In[4]:


df.dtypes


# In[16]:


df.drop_duplicates(inplace = True)


# In[17]:


df.head()


# In[15]:


df.describe()


# # Q1 What is the average score in math (G3)?

# In[18]:


df['G3'].mean()


# # Q2 How many students scored above 15 in their final grade (G3)?

# In[19]:


count = df[df['G3']>15].shape[0]
print(count)


# # Q3 Is there a correlation between study time (study time) and the final grade (G3)?
# 

# In[20]:


corr = df['studytime'].corr(df['G3'])
print(corr)


# # Q4 Which gender has a higher average final grade (G3)?

# In[32]:


gender_avg = df.groupby('sex')['G3'].mean()
print(gender_avg)


# # Q5 Plot a histogram of final grades (G3).

# In[62]:


plt.figure(figsize = (4,5))
plt.hist(df['G3'],bins = 10,color = 'skyblue',edgecolor = 'black')
plt.legend('G3')
plt.title('Histogram chart')
plt.xlabel('x_value')
plt.ylabel('number_of_student')
plt.show()


# # Q6 Create a scatter plot between study time (study time) and final grade (G3).

# In[64]:


plt.figure(figsize = (4,5))
plt.scatter(df['studytime'],df['G3'],alpha = 0.6,color = 'skyblue',edgecolor = 'black')
plt.legend('chart')
plt.title('study and grade chart')
plt.xlabel('studytime hour per week')
plt.ylabel('grade_value')
plt.show()


# # Q7  Create a bar chart comparing the average scores of male and female students.
# 

# In[65]:


gender_avg = df.groupby('sex')['G3'].mean()
print(gender_avg)


# In[73]:


plt.figure(figsize = (4,6))
plt.bar(gender_avg.index,gender_avg.values,color = ['pink','skyblue'],width = 0.6,edgecolor = 'black')
plt.xlabel('Gender')
plt.ylabel('Avg_Score_of_student')
plt.legend('chart')
plt.show()


# In[ ]:




