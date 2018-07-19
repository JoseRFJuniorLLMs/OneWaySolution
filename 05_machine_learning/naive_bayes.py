#%%
import pandas as pd
ds = pd.read_csv('../04_merged_content/dataset.csv', sep = ';', encoding='utf-8')
ds.fillna(0, inplace=True)
ds.head()

#%%
ds.set_index(['Expediente','Nome do Arquivo'], inplace=True)
ds.columns

#%%
del ds['Unnamed: 0']
del ds['Palavras-chave']
ds.head()

#%%
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(ds.iloc[:,:-1],
                                                    ds.iloc[:, -1:],
                                                    test_size    = 0.2,
                                                    random_state = 42)
print(len(x_train), len(x_test))


#%%
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(x_train, y_train)
clf.score(x_test, y_test)

#%%
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, clf.predict(x_test))