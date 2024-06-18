from sys import argv

from core.config import settings
from psycopg import Connection, connect

CREATE_TABLE_OS: str = """
CREATE TABLE IF NOT EXISTS operation_system(id SERIAL PRIMARY KEY, name VARCHAR(100) UNIQUE);
"""

CREATE_TABLE_COUNTRY: str = """
CREATE TABLE IF NOT EXISTS country(id SERIAL PRIMARY KEY, name VARCHAR(100) UNIQUE);
"""

CREATE_TABLE_COMPANY: str = """
CREATE TABLE IF NOT EXISTS company(id SERIAL PRIMARY KEY, size VARCHAR(100) UNIQUE);
"""

CREATE_TABLE_RESPONDENT: str = """
CREATE TABLE IF NOT EXISTS respondent (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    open_source BOOLEAN,
    hobby BOOLEAN,
    salary DECIMAL,
    operation_system_id INTEGER REFERENCES operation_system(id),
    country_id INTEGER REFERENCES country(id),
    company_id INTEGER REFERENCES company(id)
);
"""

CREATE_TABLE_COMMUNICATIONS_TOOLS: str = """
CREATE TABLE IF NOT EXISTS communications_tools (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE
);
"""

CREATE_TABLE_RESP_TOOLS: str = """
CREATE TABLE IF NOT EXISTS resp_tools (
    communications_tools_id INTEGER REFERENCES communications_tools(id),
    respondent_id INTEGER REFERENCES respondent(id)
);
"""

CREATE_TABLE_PROGRAMMING_LANGUAGE: str = """
CREATE TABLE IF NOT EXISTS programming_language (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE
)
"""

CREATE_TABLE_RESP_PROGRAMMING_LANGUAGE: str = """
CREATE TABLE IF NOT EXISTS resp_programming_language (
    respondent_id INTEGER REFERENCES respondent(id),
    programming_language_id INTEGER REFERENCES programming_language(id)
)
"""


def query_execute(conn: Connection, query: str) -> None:
    with conn.cursor() as cur:
        cur.execute(query)
    conn.commit()


def main() -> None:
    conn: Connection = connect(settings.db_conn_info)

    match argv[1]:
        case "create":
            tables: list[str] = [
                CREATE_TABLE_OS,
                CREATE_TABLE_COUNTRY,
                CREATE_TABLE_COMPANY,
                CREATE_TABLE_RESPONDENT,
                CREATE_TABLE_COMMUNICATIONS_TOOLS,
                CREATE_TABLE_RESP_TOOLS,
                CREATE_TABLE_PROGRAMMING_LANGUAGE,
                CREATE_TABLE_RESP_PROGRAMMING_LANGUAGE,
            ]

            for table in tables:
                query_execute(conn, table)
        case "delete":
            print("delete")
        case _:
            print(f"Option '{argv[1]}' not found")


if __name__ == "__main__":
    main()
