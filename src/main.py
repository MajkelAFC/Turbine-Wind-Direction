import psycopg2
from src.infrastructure.database import get_connection
from src.infrastructure.repository import PostgresWindTurbineRepository
from src.infrastructure.csv_loader import load_csv_to_bronze
from src.infrastructure.silver_loader import process_bronze_to_silver
from src.infrastructure.gold_loader import GoldWindAnalyticsLoader  # Added Gold loader import

if __name__ == "__main__":
    # 1. Establish database connection
    conn = get_connection()

    # 2. Initialize the repository with the connection
    repo = PostgresWindTurbineRepository(conn)

    print("Starting ETL Pipeline...")

    # 3. Step 1: Bronze Layer (Load raw CSV data into DB)
    print("Processing Bronze layer...")
    load_csv_to_bronze("wind_data.csv", repo)

    # 4. Step 2: Silver Layer (Clean and filter data)
    print("Processing Silver layer...")
    process_bronze_to_silver(conn, repo)

    # 5. Step 3: Gold Layer (Calculate business metrics & aggregates)
    print("Processing Gold layer...")
    gold_loader = GoldWindAnalyticsLoader(repo)
    calculated_avg = gold_loader.load_gold_data()
    print(f"Success! Calculated average wind direction: {calculated_avg:.2f}°")

    # 6. Clean up resources
    conn.close()
    print("Pipeline finished successfully! All layers (Bronze, Silver, Gold) processed.")
