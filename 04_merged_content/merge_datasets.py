import pandas as pd
api = pd.read_csv('../02_azure_search/api-dataset.csv', sep = ';', encoding='utf-8')
xls = pd.read_csv('../03_spreadsheets/xls-dataset2.csv', sep = ';', encoding='utf-8')

xls['Nome do Arquivo'] = xls['Nome do Arquivo'].str.strip()

dataset = pd.merge(api, xls, how = 'right', on='Nome do Arquivo')
print(len(dataset))
print(dataset.head())
dataset.to_csv('dataset.csv', sep = ';', index = False)