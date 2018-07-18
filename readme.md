# Inteligência Cognitiva Caixa

## Azure e Python

---

**Autor:** Matheus Willian Machado e Luan Moreno  
**Data:** Jul 15, 2018  

---

## Visão Geral do Projeto

> Classificação de Projetos Jurídicos quanto a ACAO, GRUPO DE ASSUNTO e ASSUNTO.

---

## Introdução

> Segue todas as informações da Microsoft sobre o projeto com o [Link para download dos arquivos][Link para download dos arquivos]. Irei indexar os documentos no Microsoft Azure para que possamos ter as Key Phrases assim ficará fácil indexar o documento.
> 1. Conforme conversado segue, para iniciarmos a POC com a Microsoft gostaríamos de confirmar o objetivo do trabalho.
>    1. Tratar arquivos em formato WORD, PDF TEXTO ou PDF IMAGEM.
>    1. Classificar os processos judiciais conforme as tipologias da Caixa.
>    1. Capacidade de apreender com as classificações já realizadas pela Caixa.
> 1. Neste trabalho avaliaremos a POC:
>    1. Quanto a velocidade de treinamento.
>    1. Assertividade nas classificações.
>    1. Facilidade nas correções de classificação.
> 1. No [LINK][Link para download dos arquivos], tem uma planilha com a classificação de mais de 2.000 processos para ajudar na construção do modelo.
> 1. A Planilha em anexo contém os campos para classificação: ACAO, GRUPO DE ASSUNTO, ASSUNTO
>
> [(Luan Moreno)](# 'MVP Microsoft')

---

### Insumos

**InteligenciaCognitiva_CAIXA.zip:**

+ Conteúdo:
  + Pasta: Arquivo
  + Planinlha: Relação de expedientes para capturar arquivos no GED_resposta.xls
+ Tamanho: 3,2 GB

**Pasta Arquivo:**

+ Conteúdo: 2127 itens, PDFs e ZIPs
+ Tamanho: 3,5 GB

[Planilha](./01_source/caixa.xls)

1. REL. EXPEDIENTES ELENCADOS (1238 linhas)
   <ol type = 'A'>
     <li>No header</li>
   </ol>
1. REL. DOCUMENTOS COPIADOS (2127 linhas)
   <ol type = 'A'>
     <li>iSequencial GED</li>
     <li>Expediente</li>
     <li>iCodDocumento</li>
     <li>Nome do Arquivo</li>
   </ol>
1. COLUNAS A APRESENTAR (1019 linhas)
   <ol type = 'A'>
     <li>Cod. Expediente</li>
     <li>Nome da Parte</li>
     <li>Situacao da Parte</li>
     <li>CPF/CNPJ/CEI da Parte</li>
     <li>Contratos da Parte</li>
     <li>Matricula</li>
     <li>Processo</li>
     <li>Dt. Entrada</li>
     <li>Vara</li>
     <li>Acao</li>
     <li>Foro</li>
     <li>Area Judicial</li>
     <li>Comarca</li>
     <li>Situacao Caixa</li>
     <li>Advogado</li>
     <li>Centro de Custo</li>
     <li>Unidade Subsidio</li>
     <li>Exito(%)</li>
     <li>Dt. Causa</li>
     <li>Vr. Causa</li>
     <li>Vr. Causa Atual</li>
     <li>Dt. do VPC</li>
     <li>Vr. Prov. Condenacao</li>
     <li>Vr. Prov. Cond. Atual</li>
     <li>Dt. do VRE</li>
     <li>Vr. Reperc. Econ.</li>
     <li>Vr. Reperc. Econ. Atual</li>
     <li>Grupo Provisão</li>
     <li>% Provisão</li>
     <li>Dt. Provisão</li>
     <li>Vr. Provisão</li>
     <li>Grupo de Assunto</li>
     <li>Assunto</li>
     <li>Operação</li>
   </ol>
1. Correlação GRUPO_ASSUNTOxASSUNT (359 linhas)
   <ol type = 'A'>
     <li>NU_GRUPO_ASSUNTO</li>
     <li>NU_ASSUNTO</li>
   </ol>


Tendo isto em vista, foram elencados os seguintes objetivos:

- [ ] Criar algoritmo de classificação supervisionado, para projetos jurídicos, quanto a: ACAO, GRUPO DE ASSUNTO e ASSUNTO.

---

## Tarefas Sugeridas

+ [ ] Definir dicionário de dados, para melhor entendimento das informações.
+ [ ] Definir domínios para os campos ACAO, GRUPO DE ASSUNTO e ASSUNTO, para suportar o algoritmo de classificação.
+ [ ] Definir De-Para dos códigos para seus valores, nos campos a serem classificados.
+ [ ] Verificar existência de alguma regra de negócio.
+ [ ] Verificar existência de alguma premissa de negócio.
+ [ ] Avaliar quais variáveis da planilha podem ser utilizadas para classificar as informações.
+ [ ] Expandir arquivos zip.
+ [ ] Minerar informações dos arquivos.
+ [ ] Indexar os arquivos pdf.
+ [ ] Obter palavras-chave.
+ [ ] Transformar planilha em dataset.
+ [ ] Adicionar palavras-chave.
+ [ ] Estudar Dataset.
+ [ ] Analisar variáveis.
+ [ ] Analisar relações.
+ [ ] Escolher algoritmo.
+ [ ] Definir algoritmo para classificar ACAO.
+ [ ] Definir algoritmo para classificar GRUPO DE ASSUNTO.
+ [ ] Definir algoritmo para classificar ASSUNTO.
+ [ ] Treinar algoritmos.
+ [ ] Aplicar algoritmos em dados novos.
+ [ ] Avaliar resultados.
+ [ ] Iterar.

---

## MVP

+ [x] Minerar informações dos arquivos.
  + [x] Indexar os arquivos pdf.
  + [x] Obter palavras-chave.
+ [ ] Criar dataset.
  + [x] Transformar planilha em dataset.
  + [x] Transformar palavras-chave em dataset.
  + [ ] Unir os datasets em apenas um.
+ [ ] Algoritmo de classificação.
  + [ ] Escolher entre Acao ou Grupo de Assunto.
  + [ ] Treinar o algoritmo com os pdf.
  + [ ] Utilizar os arquivos zip como dados de teste.

---

## Mineração

### Indexação

+ [x] Indexar os arquivos pdf.

Primeiramente, uma amostra de 800 documentos foram disponibilizados na nuvem utilizando a plataforma Microsoft Azure. Devido a natureza dos arquivos pdf, escolheu-se por armazená-los em um _blob storage_. Realizado o _upload_ dos arquivos, foi possível utilizar o módulo do Azure Seach para a indexação dos documento e mineração das palavras-chave (_Key Phrases_).

Todo processo foi executado utilizando a plataforma, desde o armazenamento dos dados, criação do índice e seus campos, extração da base, pesquisas cognitivas (OCR e detecção automática das palavras chaves), criação do indexador e indexação dos documentos.

### Palavras-chave

+ [x] Obter palavras-chave.

O ambiente de nuvem também possui um módulo de pesquisa, este permite realizar consultas à base dos dados indexados. O módulo disponibiliza uma _API_, permitindo acessar o serviço de fora da plataforma, para isto basta realizar uma requisição _REST_ à _API_ e obter o resultado da consulta.

Para este trabalho considerou-se necessário apenas o **nome dos arquivos**, para será utilizado como chave para incrementar a planilha disponibilizada como insumo; e as **palavras-chave**, para auxiliar na classificação dos documentos.

Optou-se por utilizar python para a criação de um agente capaz de montar a requisição, enviá-la à API, receber o resultado da consulta e gravá-lo em um arquivo, para que este pudesse ser utilizados por outros programas.

Segue abaixo o código python utilizado:

[api.py](./02_azure_search/api.py)

Devido a algumas limitações apenas 50 documentos puderam ser indexados, consequentemente o arquivo [api-response.txt](./02_azure_search/api-response.txt) resultante do código acima possui um lista com essa quantidade de objetos _jsons_.

Cada objeto contêm: **metadata_storage_name** (nome do arquivo) e **keyphrases** (palavras-chave), além do campo **@search.score**, que vêm por padrão.

Por fim, a fim de transformar a lista de objetos _jsons_ em um _dataset_ estruturado, optou-se por alterar o formato original do resultado da consulta à _API_, foi gerado o arquivo [api-dataset.csv](./02_azure_search/api-dataset.csv), contendo o nome dos arquivos e as palavras-chave unidas em uma única cadeia de caracteres (_string_).

---

## Datasets

### Planilha Insumo

+ [x] Transformar planilha em dataset.

Da forma como foi disponibilizada, a planilha não possui formato de conjunto de dados comum de ser utilizado em algoritmos de aprendizado de máquina.

Tendo isto em vista, foi desenvolvido código, também em python, capaz de manipular um arquivo xls e transformá-lo em formato csv, agregando as informações consideradas necessárias de cada aba da planilha insumo. Vide abaixo:

[xls2dataset.py](./03_spreadsheets/xls.py)

```python
import pandas as pd
xls2 = pd.read_excel('../01_source/caixa.xls', sheet_name = 'REL. DOCUMENTOS COPIADOS')
xls3 = pd.read_excel('../01_source/caixa.xls', sheet_name = 'COLUNAS A APRESENTAR')

xls = pd.merge(xls2, xls3)
xls.drop_duplicates(subset = 'Expediente', keep = False, inplace = True)

xls.to_csv('xls-dataset.csv', sep = ';', index = True)
```

O arquivo [xls-dataset.csv](./03_spreadsheets/xls-dataset.csv) contêm as seguintes colunas: Expediente, Nome do Arquivo, Vara, Foro, Comarca, Advogado, Centro de Custo, Unidade Subsidio, Vr. Causa, Vr. Causa Atual, Grupo de Assunto, Acao, iCodDocumento. Provenientes das abas: **REL. DOCUMENTOS COPIADOS** e **COLUNAS A APRESENTAR**.

### União

+ [ ] Unir os datasets em apenas um.

Abaixo está disponibilizado o python utilizado para realizar a união dos arquivos. Houve o cuidado de remover os espaços em brancos desnecessários no nome dos mesmos, que num primeiro momento estavam impedindo a união das chaves.

[merge_datasets.py](./merge_datasets.py)

```python
import pandas as pd
api = pd.read_csv('api-dataset.csv', sep = ';', encoding='utf-8')
xls = pd.read_csv('xls-dataset.csv', sep = ';', encoding='utf-8')
xls['Nome do Arquivo'] = xls['Nome do Arquivo'].str.strip()

dataset = pd.merge(api, xls, how = 'left', on='Nome do Arquivo')
dataset.to_csv('dataset.csv', sep = ';', index = False)
```

Mesmo com esse esforço, apenas uma chave obteve sucesso na união das informaçoes, o resultado do processo pode ser conferido no arquivo [dataset.csv](./dataset.csv).

---

## Impedimentos

+ [ ] Buscar _bugs_ nos códigos python.
+ [ ] Indexar todos os arquivos na Azure.
+ [ ] Melhorar a qualidade da planilha insumo.

Ao tentar unir os datasets surgiram alguns problemas. Nota-se que apenas um arquivo do total (1/50) obteve sucesso na união dos 2 _datasets_, os demais 49 arquivos não estavam presentes na aba **COLUNAS A APRESENTAR** da planilha insumo. Sugere-se avaliar a qualidade da planilha disponibilizada.

Há também a possibilidade de erros nos códigos python, onde alguma função aparente estar funcionando corretamente, mas que não esteja trazendo o resultado desejado. Sugere-se a revisão dos códigos python.

Vale ressaltar a limitação na hora de indexar os arquivos no Azure Search, e que nem todos os documentos disponibilizados foram indexados. Sugere-se a indexação de todos os arquivos na Azure.

---

## Referências

1. <https://portal.azure.com/>
1. <https://docs.microsoft.com/pt-br/azure/search/>
1. <https://docs.microsoft.com/en-us/rest/api/searchservice/>
1. <https://pandas.pydata.org/>

---

[Link para download dos arquivos]: <https://na01.safelinks.protection.outlook.com/?url=https://drive.google.com/open?id%3D1XbVSevaSnjHOqZwpAytRnmPxlj0v45yF&data=04%7c01%7ckleumers%40microsoft.com%7ca3ca81e67ad84cb61da408d543c695d2%7c72f988bf86f141af91ab2d7cd011db47%7c1%7c0%7c636489442562324252%7cUnknown%7cTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwifQ%3D%3D%7c-1&sdata=Kb7fqCF3V0x1UAEmBbRap3NtrqYrIjV9k/Z2cGuPuZc%3D&reserved=0>
