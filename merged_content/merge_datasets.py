import pandas as pd
api = pd.read_csv('api-dataset.csv', sep = ';', encoding='utf-8')
xls = pd.read_csv('xls-dataset.csv', sep = ';', encoding='utf-8')
xls['Nome do Arquivo'] = xls['Nome do Arquivo'].str.strip()

dataset = pd.merge(api, xls, how = 'left', on='Nome do Arquivo')
print(dataset.head())
dataset.to_csv('dataset.csv', sep = ';', index = False)