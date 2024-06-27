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

CREATE_TABLE_COMMUNICATION_TOOLS: str = """
CREATE TABLE IF NOT EXISTS communication_tools (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE
);
"""

CREATE_TABLE_RESP_TOOLS: str = """
CREATE TABLE IF NOT EXISTS resp_tools (
    communication_tools_id INTEGER REFERENCES communication_tools(id),
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

DELETE_ALL_TABLES: str = """
do $$ declare
    r record;
begin
    for r in (select tablename from pg_tables where schemaname = 'public') loop
        execute 'drop table if exists ' || quote_ident(r.tablename) || ' cascade';
    end loop;
end $$;

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
                CREATE_TABLE_COMMUNICATION_TOOLS,
                CREATE_TABLE_RESP_TOOLS,
                CREATE_TABLE_PROGRAMMING_LANGUAGE,
                CREATE_TABLE_RESP_PROGRAMMING_LANGUAGE,
            ]

            for table in tables:
                query_execute(conn, table)
            print("Create all tables.")
            return
        case "delete":
            query_execute(conn, DELETE_ALL_TABLES)
            print("Delete all tables.")
            return
        case _:
            print(f"Option '{argv[1]}' not found")
            return


if __name__ == "__main__":
    main()
