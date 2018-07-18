#%%
import os
os.chdir('./01_source/')

#%%
import pandas as pd
xls2 = pd.read_excel('caixa.xls', sheet_name = 'REL. DOCUMENTOS COPIADOS')
xls3 = pd.read_excel('caixa.xls', sheet_name = 'COLUNAS A APRESENTAR')
xls3.head()

#%%
xls = pd.merge(xls2, xls3)
xls.drop_duplicates(subset = 'Expediente', keep = False, inplace = True)
xls.head()
len(xls)

#%%
xls.to_csv('xls-dataset.csv', sep = ';', index = True)