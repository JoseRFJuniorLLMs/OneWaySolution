#%%
import pandas as pd
xls2 = pd.read_excel('../01_source/caixa.xls', sheet_name = 'REL. DOCUMENTOS COPIADOS')
xls3 = pd.read_excel('../01_source/caixa.xls', sheet_name = 'COLUNAS A APRESENTAR')
print(len(xls2), len(xls3))

#%%
xls3.head()

#%%
# xls = pd.merge(xls2, xls3, how='left')
xls = pd.merge(xls2, xls3)
xls.drop_duplicates(subset = 'Expediente', keep = False, inplace = True)
len(xls)

#%%
xls.head(n=30)

#%%
# xls.to_csv('../03_spreadsheets/xls-dataset.csv', sep = ';', index = False)
xls.to_csv('../03_spreadsheets/xls-dataset2.csv', sep = ';', index = False)

# 02.000.00030/2017