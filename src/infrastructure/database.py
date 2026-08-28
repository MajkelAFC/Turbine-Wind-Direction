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
    return psycopg2.connect(host= host,
                            port=port,
                            database="wind_db",
                            user="postgres",
                            password="postgres")


def init_db():  # Function to set up the database table
    conn = get_connection()  # Step 1: Open the connection
    cur = conn.cursor()  # Step 2: Create a worker (cursor)
    cur.execute(CREATE_BRONZE_TABLE_QUERY) # Step 3: Execute the creation query
    cur.execute(CREATE_SILVER_TABLE_QUERY)
    cur.execute(CREATE_GOLD_TABLE_QUERY)
    conn.commit()  # Step 4: Save the changes permanently
    cur.close()  # Step 5: Dismiss the worker
    conn.close()  # Step 6: Close the connection


