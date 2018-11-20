import pandas as pd
import warnings
from flask import Flask
from pymongo import MongoClient
from time import time, strftime
from sklearn import metrics
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from nltk.corpus import stopwords


def process(x):
    return x.lower().translate(str.maketrans('', '', '0123456789_[]')).encode('ascii', errors='ignore').decode()


warnings.filterwarnings("ignore")
app = Flask(__name__)

# Mongo Connection
mongoUrl = 'mongodb+srv://curadoriauser:WVspSzDzUJ9B3NBR@cluster0-vr2hd.mongodb.net/admin'
database = 'CuradoriaDB'
client = MongoClient(mongoUrl)
db = client[database]
expedientes = db.Expediente
controle = db.ControleReaprendizagem
acoes = db.Acao

# Model Creation
stopw = ['no', 'ser', 'sero', 'nao', 'ser', 'sera', 'serao']
vec = CountVectorizer(preprocessor=process,
                      stop_words=stopwords.words('portuguese')+stopw,
                      max_df=.6,
                      min_df=5,
                      ngram_range=(2, 2))
clf = MultinomialNB()
model = Pipeline([('vec', vec), ('clf', clf)])


@app.route("/")
def hello():
    return "hello world!"


@app.route('/processar/<texto>')
def processar(texto):
	return process(texto)


@app.route("/run")
def run():
  # Start Timer
  print(strftime("%H:%M:%S") +' running...')
  controle.update_one({}, {'$set': {'emProcessamento': True}})
  t0 = time()

  # Query Data
  print(strftime("%H:%M:%S") +' querying...')
  df = pd.DataFrame.from_records(expedientes.find(
      {}, {'codExpediente': 1, 'palavrasChave': 1, 'acaoId': 1}))
  df.set_index('_id', inplace=True)
  
  # Data Wrangling
  print(strftime("%H:%M:%S") +' wrangling...')
  df1 = df.groupby('codExpediente')['palavrasChave'].sum()
  df1 = df1.apply(lambda x: ' '.join(x) if type(x) == list else ' ')

  df = df.loc[:, ('codExpediente', 'acaoId')]
  df.drop_duplicates(inplace=True)
  df.set_index('codExpediente', inplace=True)
  df = df.merge(df1.to_frame(), left_index=True, right_index=True)

  # Model Fit and Accuracy
  print(strftime("%H:%M:%S") +' modeling...')
  model.fit(df.palavrasChave, df.acaoId)
  predictions = model.predict(df.palavrasChave)
  accuracy = metrics.classification_report(
      df.acaoId, predictions, output_dict=True)
  del accuracy['micro avg']
  del accuracy['macro avg']
  del accuracy['weighted avg']

  # Accuracy Update on MongoDB
  print(strftime("%H:%M:%S") +' updating...')
  for acao in accuracy:
      query = {'acaoId': int(acao)}
      update = {'$set': {'acuracia': round(accuracy[acao]['f1-score'], 2)}}
      acoes.update_one(query, update)

  # Stop Timer
  print(strftime("%H:%M:%S") +' done!')
  controle.update_one({}, {'$set': {'emProcessamento': False,
                                    'dataUltimoProcessamento': strftime("%m/%d/%Y %H:%M:%S"),
                                    'tempoUltimoProcessamentoSec': int(time()-t0)}})
  
  return "Script executado"