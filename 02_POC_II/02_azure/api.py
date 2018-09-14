class Config(object):
  def __init__(self, cfile):
    from json import loads
    config = loads(open(cfile).read())
    
    self.service = config['SERVICE']
    self.index   = config['INDEX']
    self.version = config['VERSION']
    self.key     = config['KEY']
    self.query   = config['QUERY']
    self.output  = config['OUTPUT']
    self.fields  = config['FIELDS']
    self.dataset = config['DATASET']
    self.columns = config['COLUMNS']

class Crawler(object):
  def __init__(self, service, index, version):
    self.service = service
    self.index   = index
    self.version = version
    
    self.url     = 'https://' + service +\
                   '.search.windows.net/indexes/' + index +\
                   '/docs/search?api-version=' + version
    print(self.url)
  
  def searchDocuments(self, key, query={}, headers={}, meta=False, file=False):
    from requests import post
    from json import dumps
    from time import time
    
    headers['api-key'] = key
    headers['content-type'] = 'application/json'
    
    if not query:
      query['search'] = '*'
    
    t0 = time()
    response = post(self.url, headers = headers, json = query).json()
    
    while '@search.nextPageParameters' in response:
      query = response['@search.nextPageParameters']
      response2 = post(self.url, headers=headers, json=query).json()
      response2['value'].extend(response['value'])
      response = response2
    
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

def api2dataset(data, file, columns=False):
  import pandas as pd
  dataset = pd.DataFrame.from_dict(data)
  if columns:
    dataset.columns = columns
  
  dataset.to_csv(file, sep = ';', index=False, encoding='utf-8')
  print('Arquivos', file, 'criado!')

if __name__ == '__main__':
  from json import loads
  
  # Carregar configuracoes
  config = Config('config.json')
  
  # Criar raspador
  spider = Crawler(config.service, config.index, config.version)
  
  # Realizar consulta
  spider.searchDocuments(config.key, query = config.query, file = config.output)

  # Transformar consulta em dataset
  data = loads(open(config.output).read())
  data = concatFields(data, config.fields) # Concatenar valores dos campos de lista em string
  api2dataset(data, config.dataset, config.columns)