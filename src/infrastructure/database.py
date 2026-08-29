import psycopg2
import os

CREATE_BRONZE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS wind_data_bronze(
winddirabs varchar(50)
);
"""

CREATE_SILVER_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS wind_data_silver(
winddirabs float
);
"""

CREATE_GOLD_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS wind_data_gold(
avg_winddirabs float,
calculated_at timestamp
);
"""


def get_connection():
    host = os.environ.get("DB_HOST", "localhost")
    port = os.environ.get("DB_PORT", "5433")
    return psycopg2.connect(
        host=host,
        port=port,
        database=os.environ.get("POSTGRES_DB", "wind_db"),
        user=os.environ.get("POSTGRES_USER", "postgres"),
        password=os.environ.get("POSTGRES_PASSWORD", "postgres"),
    )


def init_db():  # Function to set up the database tables
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(CREATE_BRONZE_TABLE_QUERY)
    cur.execute(CREATE_SILVER_TABLE_QUERY)
    cur.execute(CREATE_GOLD_TABLE_QUERY)
    conn.commit()
    cur.close()
    conn.close()
