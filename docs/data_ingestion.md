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
