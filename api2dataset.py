import pandas as pd
from json import loads

with open('api-text.txt') as fl:
  data = loads(fl.read())["value"]

wanted_keys = ['metadata_storage_name', 'keyphrases']

data = [{k: data[i][k] for k in wanted_keys} for i in range(len(data))]

for i in range(len(data)):
  data[i]['keyphrases'] = ' '.join(data[i]['keyphrases'])

dataset = pd.DataFrame.from_dict(data)[wanted_keys]
dataset.columns = ['Nome do Arquivo', 'Palavras Chaves']
dataset.to_csv('api-dataset.csv', sep = ';', index = False)
