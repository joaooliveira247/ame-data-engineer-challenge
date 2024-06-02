CREATE_TABLE_OS: str = """
CREATE TABLE IF NOT EXISTS operation_system(id SERIAL PRIMARY KEY, name VARCHAR(100));
"""

CREATE_TABLE_COUNTRY: str = """
CREATE TABLE IF NOT EXISTS country(id SERIAL PRIMARY KEY, name VARCHAR(100));
"""


def main() -> None: ...


if __name__ == "__main__":
    main()
