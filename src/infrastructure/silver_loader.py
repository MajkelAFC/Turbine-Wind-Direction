from src.domain.wind_turbine import WindRecord
from src.domain.repository import WindTurbineRepository

def process_bronze_to_silver(conn, repo:WindTurbineRepository) -> None:
    with conn.cursor() as cursor:
        cursor.execute("SELECT winddirabs FROM wind_data_bronze;")
        rows = cursor.fetchall()
        for row in rows:
            record = WindRecord(winddirabs=row[0])
            clean_val = record.get_clean_data()
            if clean_val is not None:
                repo.save_silver(clean_val)

    conn.commit()
