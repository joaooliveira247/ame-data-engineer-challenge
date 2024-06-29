# Ingestão de dados

<div style="width:60%; margin: auto;">
    <img src="./images/data_ingestion_diagram.png">
</div>

### Banco de dados usado: [Postgresql](https://www.postgresql.org/)

### Arquitetura usada: [Medallion Architecture](https://www.databricks.com/glossary/medallion-architecture)

### Número de clusters: 1

## Executando a Ingestão de dados:

1º - Inicie o container com postgresql

`Make run-docker`

2º - Crie as tabelas

`Make db-create`

3º - Execute todo [notebook](../ame_data_engineer_challenge/data_ingestion.ipynb)

## Processo de ETL

### 🥉 Bronze Layer

1º - Extração dos dados fornecidos em [Kaggle dataset](https://www.kaggle.com/datasets/stackoverflow/stack-overflow-2018-developer-survey?select=survey_results_public.csv), optei por usar os dados provenientes do kaggle ao invés do disponibilizado no desafio.

2º - Tomei a liberdade de selecionar só as colunas usadas para evitar problemas de performance.  
