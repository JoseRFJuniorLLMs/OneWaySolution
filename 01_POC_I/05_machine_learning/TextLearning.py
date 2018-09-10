
# coding: utf-8

# In[1]:


import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.cluster import KMeans
from sklearn import metrics


# In[2]:


data = pd.read_csv('../04_merged_content/dataset.csv', sep = ';',
                   names=['name','cod','words'], index_col='name', header=0)
data.info()


# In[3]:


na = data[data.words.isnull()].index.values
data[data.words.isnull()]


# In[4]:


data.drop(na, inplace=True)
data.shape


# In[5]:


x_train, x_test, y_train, y_test = train_test_split(data.words, data.cod, test_size = 0.2, random_state=42)
print(len(x_train))
print(len(x_test))


# In[6]:


vec = CountVectorizer()
vec_train = vec.fit_transform(x_train)
vec_train.shape


# In[7]:


clf = MultinomialNB().fit(vec_train, y_train)


# In[8]:


vec_test = vec.transform(x_test)
predictions = clf.predict(vec_test)
clf.score(vec_test, y_test)


# In[9]:


print(metrics.classification_report(y_test, predictions))
print(metrics.confusion_matrix(y_test, predictions))