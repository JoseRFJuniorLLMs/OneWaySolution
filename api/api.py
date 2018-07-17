class Crawler(object):
  def __init__(self, service, index, version):
    self.service = service
    self.index   = index
    self.version = version
    
    self.url     = 'https://' + service +\
                   '.search.windows.net/indexes/' + index +\
                   '/docs?api-version=' + version
    print(self.url)
  
  def searchDocuments(self, key, query={}, headers={}, meta=False, file=False):
    from requests import get
    from json import dumps
    from time import time
    
    headers['api-key'] = key
    if not query:
      query['search'] = '*'
    
    t0 = time()
    response = get(self.url, headers = headers, params = query).json()
    if not meta:
      response = response['value']
    
    print('Foram retornados', len(response), 'documentos!')
    print('Em', round(time()-t0, 3), 'segundos!')
    
    if file:
      with open(file, 'w') as fl:
        fl.write(dumps(response, indent = 2))
        print('Arquivo', file, 'criado!')
    else:
      return response

def concatFields(data, fields):
  for field in fields:
    for i in range(len(data)):
      data[i][field] = ' '.join(data[i][field])
  
    print('Campo', field, 'concatenado!')
  
  return data

def api2dataset(data, file, columns=None):
  import pandas as pd
  dataset = pd.DataFrame.from_dict(data)
  dataset.to_csv(file, sep = ';', columns = columns, index=False)
  print('Arquivos', file, 'criado!')

if __name__ == '__main__':
  from json import loads
  
  filename = 'api-response.txt'
  fields   = ['keyphrases']
  dataset  = 'api-dataset.csv'
  
  chave = open('../../Keys/api-key.txt').read()
  spider = Crawler('demoowshq', 'teste', '2017-11-11')
  
  query = {'$select':'metadata_storage_name,keyphrases'}
  spider.searchDocuments(chave, query = query, file = filename)
  
  data = loads(open(filename).read())
  data = concatFields(data, fields)
  api2dataset(data, dataset)