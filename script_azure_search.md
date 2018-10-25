Curadoria Caixa
===

Azure Search e Cognitive Services
---

### Criar Fonte de Dados

```
POST https://<nome servico>.search.windows.net/datasources?api-version=2017-11-11-Preview
Content-Type: application/json  
api-key: <chave servico>
```

```Json
{   
    "name" : "<nome fonte dados>",  
    "description" : "<descricao fonte dados>",  
    "type" : "azureblob",
    "credentials" :
    { "connectionString" :
      "DefaultEndpointsProtocol=https;AccountName=<nome conta storage>;AccountKey=<chave acesso storage>;"
    },  
    "container" : { "name" : "<nome blob storage>" }
}
```

### Criar Skillset

```
PUT https://<nome servico>.search.windows.net/skillsets/<nome skillset>?api-version=2017-11-11-Preview
api-key: <chave servico>
Content-Type: application/json
```

```Json
{
  "description": "<descricao skillset>",
  "skills":
  [
    {
      "@odata.type": "#Microsoft.Skills.Vision.OcrSkill",
      "description": "Extracts text (plain and structured) from image.",
      "context": "/document/normalized_images/*",
      "defaultLanguageCode": "pt",
      "detectOrientation": true,
      "inputs": [
        {
          "name": "image",
          "source": "/document/normalized_images/*"
        }
      ],
      "outputs": [
        {
          "name": "text"
        }
      ]
    },
    {
      "@odata.type": "#Microsoft.Skills.Text.MergeSkill",
      "description": "Create merged_text, which includes all the textual representation of each image inserted at the right location in the content field.",
      "context": "/document",
      "insertPreTag": " ",
      "insertPostTag": " ",
      "inputs": [
        {
          "name":"text", "source": "/document/content"
        },
        {
          "name": "itemsToInsert", "source": "/document/normalized_images/*/text"
        },
        {
          "name":"offsets", "source": "/document/normalized_images/*/contentOffset" 
        }
      ],
      "outputs": [
        {
          "name": "mergedText", "targetName" : "merged_content"
        }
      ]
    },
    {
      "@odata.type": "#Microsoft.Skills.Text.LanguageDetectionSkill",
      "inputs": [
        {
          "name": "text", "source": "/document/merged_content"
        }
      ],
      "outputs": [
        {
          "name": "languageCode",
          "targetName": "languageCode"
        }
      ]
    },
    {
      "@odata.type": "#Microsoft.Skills.Text.SplitSkill",
      "textSplitMode" : "pages", 
      "maximumPageLength": 50000,
      "inputs": [
        {
            "name": "text",
            "source": "/document/merged_content"
        },
        { 
            "name": "languageCode",
            "source": "/document/languageCode"
        }
      ],
      "outputs": [
        {
              "name": "textItems",
              "targetName": "pages"
        }
      ]
    },
    {
      "@odata.type": "#Microsoft.Skills.Text.KeyPhraseExtractionSkill",
      "context": "/document/pages/*",
      "inputs": [
        {
          "name": "text", "source": "/document/pages/*"
        },
        {
          "name":"languageCode", "source": "/document/languageCode"
        }
      ],
      "outputs": [
        {
          "name": "keyPhrases",
          "targetName": "keyPhrases"
        }
      ]
    }
  ]
}
```

### Criar Index

```
PUT https://<nome servico>.search.windows.net/indexes/<nome index>?api-version=2017-11-11-Preview
api-key: <chave servico>
Content-Type: application/json
```

```Json
{
  "fields": [
    {
      "name": "id",
      "type": "Edm.String",
      "key": true,
      "searchable": true,
      "filterable": false,
      "facetable": false,
      "sortable": true
    },
    {
      "name": "name",
      "type": "Edm.String",
      "searchable": true,
      "filterable": false,
      "facetable": false,
      "sortable": true
    },
    {
      "name": "merged_content",
      "type": "Edm.String",
      "sortable": false,
      "searchable": true,
      "filterable": false,
      "facetable": false,
      "retrievable": false
    },
    {
      "name": "keyPhrases",
      "type": "Collection(Edm.String)",
      "searchable": true,
      "filterable": false,
      "facetable": false
    }
  ]
}
```

### Criar Indexer

```
PUT https://<nome servico>.search.windows.net/indexers/<nome indexer>?api-version=2017-11-11-Preview
api-key: <chave servico>
Content-Type: application/json
```

```Json
{
  "name":"<nome indexer>", 
  "dataSourceName" : "<nome fonte dados>",
  "targetIndexName" : "<nome index>",
  "skillsetName" : "<nome skillset>",
  "fieldMappings" : [
        {
          "sourceFieldName" : "metadata_storage_path",
          "targetFieldName" : "id",
          "mappingFunction" : 
            { "name" : "base64Encode" }
        },
        {
          "sourceFieldName" : "metadata_storage_name",
          "targetFieldName" : "name"
        }
   ],
  "outputFieldMappings" : 
  [
        {
          "sourceFieldName" : "/document/merged_content", 
          "targetFieldName" : "merged_content"
        },
        {
          "sourceFieldName" : "/document/pages/*/keyPhrases/*", 
          "targetFieldName" : "keyPhrases"
        } 
  ],
  "parameters":
  {
    "maxFailedItems":-1,
    "maxFailedItemsPerBatch":-1,
    "configuration": 
    {
        "dataToExtract": "contentAndMetadata",
        "imageAction": "generateNormalizedImages"
        }
  }
}
```