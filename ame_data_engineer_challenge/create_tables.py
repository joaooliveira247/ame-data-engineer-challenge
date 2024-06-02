from psycopg import Connection, connect

CREATE_TABLE_OS: str = """
CREATE TABLE IF NOT EXISTS operation_system(id SERIAL PRIMARY KEY, name VARCHAR(100));
"""

CREATE_TABLE_COUNTRY: str = """
CREATE TABLE IF NOT EXISTS country(id SERIAL PRIMARY KEY, name VARCHAR(100));
"""

CREATE_TABLE_COMPANY: str = """
CREATE TABLE IF NOT EXISTS company(id SERIAL PRIMARY KEY, name VARCHAR(100));
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
    Name VARCHAR(255)
);
"""

CREATE_TABLE_RESP_TOOLS: str = """
CREATE TABLE IF NOT EXISTS resp_tools (
    communications_tools_id INTEGER REFERENCES communications_tools(id),
    respodent_id INTEGER REFERENCES respondent(id)
);
"""

CREATE_TABLE_PROGRAMMING_LANGUAGE: str = """
CREATE TABLE IF NOT EXISTS programming_language (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
)
"""

CREATE_TABLE_RESP_PROGRAMMING_LANGUAGE: str = """
CREATE TABLE IF NOT EXISTS resp_programming_language (
    respondent_id INTEGER REFERENCES respondent(id),
    programming_language_id INTEGER REFERENCES programming_language(id),
    moment BOOLEAN
)
"""


def query_execute(conn: Connection, query: str) -> None:
    with conn.cursor() as cur:
        cur.execute(query)
    conn.commit()


def main() -> None: ...


if __name__ == "__main__":
    main()