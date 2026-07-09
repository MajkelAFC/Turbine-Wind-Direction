import psycopg2

CREATE_BRONZE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS wind_data_bronze( 
winddirabs varchar(50) 
);
"""

def get_connection():
    return psycopg2.connect(host="localhost",
                            database="wind_db",
                            user="postgres",
                            password="postgres")


def init_db():  # Function to set up the database table
    conn = get_connection()  # Step 1: Open the connection
    cur = conn.cursor()  # Step 2: Create a worker (cursor)
    cur.execute(CREATE_BRONZE_TABLE_QUERY)  # Step 3: Execute the creation query
    conn.commit()  # Step 4: Save the changes permanently
    cur.close()  # Step 5: Dismiss the worker
    conn.close()  # Step 6: Close the connection


