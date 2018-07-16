# -*- coding: utf-8 -*-
'''
Este módulo contém funções para:
+ [x] Consultar .
+ [x] Obter palavras-chave.
'''

from requests import get
from json import dumps

#%%
url = 'https://demoowshq.search.windows.net/indexes/teste/docs?api-version=2017-11-11'
headers = {"api-key":'******************************'} 
params = {"$select":'metadata_storage_name,keyphrases'}
response = get(url, headers = headers, params = params) 
print(len(response.url))

results = response.json()

with open('api-text.txt','w') as fl:
  fl.write(dumps(results, indent = 2))