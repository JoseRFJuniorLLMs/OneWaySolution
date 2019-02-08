Arquitetura Caixa
====

Caixa
---

- Source: Pasta de arquivos enviados pela Caixa que servem de dados teste e insumo de treinamento para o modelo de machine learning.

Azure
---

- Blob Storage: Armazenamento em nuvem para onde os dados de insumo (Source) são enviados, hoje esse processo é feito manualmente.
- Azure Search: Mecanismo de OCR, utilizado para reconhecimento de texto nos arquivos e detecção de palavras-chave.
- API: Canal de comunicação externa do Azure Search, por meio do qual é possível consultar as palavras chaves de cada documento.

WebApp Node, C# e Angular
---

- BackEnd: Servidor em nuvem onde é centralizado todo o processamento da aplicação Curadoria, como consulta das palavras-chave por meio da API, disponibilização de serviços para o FrontEnd e manipulação da base de dados MongoDB.
- Python Services e ML Model: Servidor em nuvem onde são disponibilizados os serviços e manipulação do modelo de ML.
- MongoDB: Paas de MongoDB para armazenamento das informações.
- FrontEnd: aplicação.
