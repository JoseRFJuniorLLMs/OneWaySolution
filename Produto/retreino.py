#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import pickle

from pymongo import MongoClient
from time import time, strftime


# In[2]:


mongoUrl = 'mongodb+srv://curadoriauser:WVspSzDzUJ9B3NBR@cluster0-vr2hd.mongodb.net/admin'
database = 'CuradoriaDB'
client   = MongoClient(mongoUrl)
db       = client[database]
db.list_collection_names()


# In[3]:


expedientes = client[database].Expediente
controle    = client[database].ControleReaprendizagem
acoes       = client[database].Acao
print(expedientes.count_documents({}), controle.count_documents({}), acoes.count_documents({}))


# In[4]:


controle.update_one({}, {'$set': {'emProcessamento': True}})
t0 = time()


# In[5]:


df = pd.DataFrame.from_records(expedientes.find({ },{'codExpediente': 1, 'palavrasChave': 1, 'acaoId': 1 }))
df.set_index('_id', inplace=True)
print(df.shape)
df.head()


# In[6]:


df1 = df.groupby('codExpediente')['palavrasChave'].sum()
df1 = df1.apply(lambda x: ' '.join(x) if type(x) == list else ' ')
df1.head()


# In[7]:


df = df.loc[:,('codExpediente', 'acaoId')]
df.drop_duplicates(inplace=True)
df.set_index('codExpediente', inplace=True)
df = df.merge(df1.to_frame(), left_index=True, right_index=True)
df.head()


# In[8]:


with open('dataset.pkl', "wb") as f:
    clf = pickle.dump(df, f)


# In[9]:


def process(x):
    return x.lower().translate(str.maketrans('', '', '0123456789_[]')).encode('ascii',errors='ignore').decode()


# In[10]:


with open('model.pkl', "rb") as f:
    clf = pickle.load(f)


# In[11]:


clf.fit(df.palavrasChave, df.acaoId)


# In[12]:


from sklearn import metrics
predictions = clf.predict(df.palavrasChave)
print(metrics.classification_report(df.acaoId, predictions))
accuracy = metrics.classification_report(df.acaoId, predictions, output_dict=True)


# In[13]:


del accuracy['micro avg']
del accuracy['macro avg']
del accuracy['weighted avg']


# In[14]:


for acao in accuracy:
    query  = {'acaoId': int(acao)}
    update = {'$set': {'acuracia': round(accuracy[acao]['f1-score'],2)}}
    acoes.update_one(query, update)


# In[15]:


controle.update_one({}, {'$set': {'emProcessamento': False,
                                  'dataUltimoProcessamento': strftime("%m/%d/%Y %H:%M:%S"),
                                  'tempoUltimoProcessamentoSec': int(time()-t0)}})

