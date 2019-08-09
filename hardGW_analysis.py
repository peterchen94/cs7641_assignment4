#!/usr/bin/env python
# coding: utf-8

# # CS7641 A4 Spring 2019 
# 
# ## Peter Chen (cchen376)
# 
# ## Hard Grid World Analysis

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import os


# In[2]:


easy_dir='./hardGW_output/'
fileList = os.listdir(easy_dir)


# In[12]:


plt.figure()
comparison_list = ['Hard Policy.csv','Hard Value.csv','Hard Q-Learning L0.1 q-100.0 E0.7.csv']
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


# In[14]:


df=pd.read_csv(easy_dir+comparison_list[0])

df['reward'].max()


# In[5]:


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


# In[13]:


legend_list=[]
#plt.figure()
for idx, file in enumerate(fileList):
    if ('Q' in file) and file.endswith('csv') and 'L0.1' in file:
        plt.figure()
        legend_list.append(file.split('.csv')[0])
        df=pd.read_csv(easy_dir+file)
        plt.plot(df['reward'])
        plt.title(file)
        plt.ylim((-400,100))
        plt.xlabel('iterations')
        plt.ylabel('reward')
plt.legend(legend_list)
#plt.title('Q learning comparison')


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




