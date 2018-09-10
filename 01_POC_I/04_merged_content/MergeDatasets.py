
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


cols = ['Nome do Arquivo', 'iCodDocumento']
xls = pd.read_csv('../03_spreadsheets/xls-dataset.csv', sep = ';', usecols=cols)
xls.head()


# In[3]:


cols=['Nome do Arquivo','Palavras-chave']
api = pd.read_csv('../02_azure_search/api-dataset.csv', sep = ';', usecols=cols)
api.head()


# In[4]:


xls.set_index('Nome do Arquivo', inplace=True)
api.set_index('Nome do Arquivo', inplace=True)


# In[5]:


print(xls.shape)
print(api.shape)


# In[6]:


api.index.difference(xls.index)


# In[7]:


xls.index = xls.index.str.strip()
api.index.difference(xls.index)


# In[8]:


xls.index = xls.index.str.replace(' /V /', '', regex=False)
api.index.difference(xls.index)


# In[9]:


row = [
    '02000000532017_6809593_20170125_-_PROCESSO_INTEGRAL_-_OSVANDO_REIS_QUEIROZ_0002532-03.2016.5.11.0018',
    '02000005802017_7295032_20170316_PETICAO_INICIAL_LEOMAR_SOUZA_DE_LISBOA_-_0000581-86.2016.5.11.0401.p'
]
fix = [
    '02000000532017_6809593_20170125_-_PROCESSO_INTEGRAL_-_OSVANDO_REIS_QUEIROZ_0002532-03.2016.5.11.0018.pdf',
    '02000005802017_7295032_20170316_PETICAO_INICIAL_LEOMAR_SOUZA_DE_LISBOA_-_0000581-86.2016.5.11.0401.pdf'
]
xls.rename(index={row[i]: fix[i] for i in range(len(row))}, inplace=True)
api.index.difference(xls.index)


# In[10]:


data = pd.merge(xls, api, left_index=True, right_index=True)


# In[11]:


data.shape


# In[12]:


data.head()


# In[13]:


data.to_csv('dataset.csv', sep = ';')

