class Crawler(object):
  def __init__(self, service, index, version):
    self.service = service
    self.index   = index
    self.version = version
    
    self.url     = 'https://' + service +\
                   '.search.windows.net/indexes/' + index +\
                   '/docs?api-version=' + version
  
  def searchDocuments(self, key, headers = {}, query = {}, file = 'api-response.txt'):
    from requests import get
    from json import dumps
    from time import time

    headers['api-key'] = key
    if not query:
      query['search'] = '*'
    
    t0 = time()
    response = get(self.url, headers = headers, params = query)
    print('Foram retornados', len(response.json()['value']), 'documentos!')
    print('Em', round(time()-t0, 3), 'segundos!')
    
    with open(file, 'w') as fl:
      fl.write(dumps(response.json(), indent = 2))
      print('Arquivo', file, 'criado!')

if __name__ == '__main__':
  chave = open('../../Keys/api-key.txt').read()
  print(chave)

  spider = Crawler('demoowshq', 'teste', '2017-11-11')
  print(spider.url)
  
  spider.searchDocuments(chave)