import psycopg2
from tabulate import tabulate

# Database configuration
DB_HOST = "darcydb.crgk48smefvn.ap-southeast-2.rds.amazonaws.com"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = r"7crQ9MrrBC216QmgSB^S"
DB_PORT = 5432

# Helper function to execute a SQL file
def run_sql_file(filename: str):
    with open(filename, 'r') as file:
        sql = file.read()

    with psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            conn.commit()

# Create michelle table
def run_ddl():
    run_sql_file("brain/postgres/michelle/DDL/create_michelle_table.sql")

# Insert practice data
def run_dml():
    run_sql_file("brain/postgres/michelle/DML/insert_michelle_table.sql")

# Create summary table
def run_summary_table():
    run_sql_file("brain/postgres/michelle/DDL/create_practice_summary_table.sql")

# View any table and print it as a formatted table
def view_table(query: str, title: str):
    with psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            rows = cur.fetchall()
            colnames = [desc[0] for desc in cur.description]
            print(f"\n📄 {title}")
            print(tabulate(rows, headers=colnames, tablefmt="fancy_grid"))

# View michelle table
def view_michelle_table():
    view_table("SELECT * FROM project_two.michelle;", "Table: michelle")

# View practice_summary table
def view_summary_table():
    view_table("SELECT * FROM project_two.practice_summary;", "Table: practice_summary")

# Main execution
if __name__ == "__main__":
    run_ddl()
    run_dml()
    view_michelle_table()
    run_summary_table()
    view_summary_table()
