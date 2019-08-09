#!/usr/bin/env python
# coding: utf-8

# # CS7641 A4 Spring 2019 
# ## Peter Chen (cchen376)
# ## Easy Grid World Analysis

# In[54]:


import pandas as pd
import matplotlib.pyplot as plt
import os


# In[60]:


easy_dir='./easyGW_output/'
fileList = os.listdir(easy_dir)


# In[94]:


plt.figure()
comparison_list = ['Easy Policy.csv','Easy Value.csv','Easy Q-Learning L0.1 q-100.0 E0.7.csv']
legend_list=[]
for file in comparison_list:
    legend_list.append(file.split('.csv')[0])
    df=pd.read_csv(easy_dir+file)
    plt.plot(df['reward'])
plt.legend(legend_list)
plt.ylim((-200,100))
plt.xlim((0,100))
plt.title('Comparison of reward')
plt.xlabel('iterations')
plt.ylabel('reward')


# In[93]:


df=pd.read_csv(easy_dir+comparison_list[0])

df['reward'].tail()


# In[83]:


legend_list=[]
plt.figure()
for file in comparison_list:
    legend_list.append(file)
    df=pd.read_csv(easy_dir +file)
    plt.plot(df['convergence'])
    plt.title('Comparison of Convergence')
    plt.xlim((0,100))
plt.xlabel('iterations')
plt.ylabel('convergence')
plt.legend(legend_list)


# In[86]:


legend_list=[]
plt.figure()
for file in comparison_list:
    legend_list.append(file)
    df=pd.read_csv(easy_dir +file)
    plt.plot(df['time'])
    plt.title('Comparison of time')
    plt.xlim((0,100))
plt.xlabel('iterations')
plt.ylabel('time (milliseconds)')
plt.legend(legend_list)


# In[72]:


legend_list=[]
plt.figure()
for file in comparison_list:
    legend_list.append(file)
    df=pd.read_csv(easy_dir +file)
    plt.plot(df['time'])
    plt.title(file)
plt.legend(legend_list)


# In[88]:


legend_list=[]
plt.figure()
for idx, file in enumerate(fileList):
    if ('Q' in file) and file.endswith('csv') and idx < 10:
        #plt.figure()
        legend_list.append(file.split('.csv')[0])
        df=pd.read_csv(easy_dir+file)
        plt.plot(df['reward'])
        plt.title(file)
        plt.ylim((-400,100))
        plt.xlim((0,500))
        plt.xlabel('iterations')
        plt.ylabel('reward')
plt.legend(legend_list)


# In[74]:


legend_list=[]
for file in fileList:
    if ('Q' in file) and file.endswith('csv'):
        plt.figure()
        legend_list.append(file)
        df=pd.read_csv(easy_dir +file)
        plt.xlim((0,500))
        plt.plot(df['convergence'])
        plt.title(file)
        plt.xlabel('iterations')
        plt.ylabel('convergence')


# In[67]:


legend_list=[]
for file in fileList:
    if ('Q' in file) and file.endswith('csv'):
        plt.figure()
        legend_list.append(file)
        df=pd.read_csv(easy_dir +file)
        plt.plot(df['time'])
        plt.title(file)


# In[ ]:





# In[ ]:




