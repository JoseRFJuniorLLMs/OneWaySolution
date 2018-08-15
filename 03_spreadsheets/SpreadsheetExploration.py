
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


path = '../01_source/RelaÆo de expedientes para capturar arquivos no GED_resposta.xls'
data = pd.read_excel(path, sheet_name='REL. DOCUMENTOS COPIADOS')
data.head()


# In[3]:


data.shape


# In[4]:


data.info()


# In[5]:


data['iSequencial GED'].nunique() == data.shape[0]


# In[6]:


data['Expediente'].nunique() == data.shape[0]


# In[7]:


data['iCodDocumento'].unique()


# In[8]:


data['Nome do Arquivo'].nunique() == data.shape[0]


# In[9]:


data.groupby('Expediente').iCodDocumento.nunique().sort_values(ascending=False).head()


# In[10]:


data.drop(['iSequencial GED', 'Expediente'], axis=1, inplace=True)
data.set_index(['Nome do Arquivo'], inplace=True)
data.head()


# In[11]:


data.to_csv('xls-dataset.csv', sep = ';')

