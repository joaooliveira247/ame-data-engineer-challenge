# Ame Data Engineer Challenge

[Descrição do Desafio](./docs/challenge.md)

## Requisitos 🧑‍💻:
Este projeto utiliza um sistema de gerenciamento de pacotes e dependências chamado [poetry](https://python-poetry.org/).

- Instalação:

    `osx / linux / bashonwindows instruções de instalação
    `

    ```bash
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
    ```

    `
    windows powershell instruções de instalação
    `

    ```bash
    (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
    ```

- Executando:

    ```bash
    poetry install
    ```

    ```bash
    poetry shell
    ```

## Documentação CLI 📜:

- 🐋 Inicia o "data warehouse".

    ```bash
    make run-docker
    ```

- 📋 Cria todas as tabelas do "data warehouse".

    ```bash
    make db-create
    ```

- 📋 Deleta todas as tabelas do "data warehouse".

    ```bash
    make db-delete
    ```


## Esse projeto foi baseado 🤝:

https://github.com/AmeDigital/challenge-data-engineer