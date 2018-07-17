# -*- coding: utf-8 -*-
'''
Este módulo contém funções para:
- [x] Transformar planilha em dataset.
- [ ] Adicionar palavras chaves.
'''
#%%
import pandas as pd

#%%
xls2 = pd.read_excel('caixa.xls', sheet_name = 'REL. DOCUMENTOS COPIADOS')
xls3 = pd.read_excel('caixa.xls', sheet_name = 'COLUNAS A APRESENTAR')
xls3.head()

#%%
xls = pd.merge(xls3, xls2)
xls.drop_duplicates(subset = 'Expediente', keep = False, inplace = True)
xls.set_index(['Expediente', 'Nome do Arquivo'], inplace = True)
xls.head()

#%%
xls.to_csv('xls-dataset.csv', sep = ';', index = True)