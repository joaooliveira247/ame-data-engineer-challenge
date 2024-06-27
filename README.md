# Ame Data Engineer Challenge

[Descrição do Desafio](./docs/challenge.md)

## Requirements 🧑‍💻:
This project use a packaging and dependency management called [poetry](https://python-poetry.org/).
- Installation:

    `osx / linux / bashonwindows install instructions
    `

    ```bash
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
    ```
    `
    windows powershell install instructions
    `
    ```bash
    (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
    ```
- Running:
    ```bash
    poetry install
    ```
    ```bash
    poetry shell
    ```

## Documentation 📜:

- 🐋 Start docker with database.

    ```bash
    make run-docker
    ```

- 📋 Create all tables in "data warehouse".

    ```bash
    make db-create
    ```

- 📋 Delete all tables in "data warehouse".

    ```bash
    make db-delete
    ```


## This project was based 🤝:

https://github.com/AmeDigital/challenge-data-engineer