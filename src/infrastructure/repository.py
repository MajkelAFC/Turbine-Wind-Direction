from typing import List

from src.domain.repository import WindTurbineRepository
from src.domain.wind_turbine import WindRecord

class PostgresWindTurbineRepository(WindTurbineRepository):
    def __init__(self, conn):
        self.conn = conn

    def truncate(self, table: str) -> None:
        with self.conn.cursor() as cursor:
            cursor.execute(f"TRUNCATE TABLE {table};")
        self.conn.commit()

    def save (self, record: WindRecord) -> None:
        with self.conn.cursor() as cursor:
            cursor.execute("INSERT INTO wind_data_bronze (winddirabs) VALUES (%s);", (record.winddirabs,))
        self.conn.commit()

    def save_silver(self, clean_value: float) -> None:
        with self.conn.cursor() as cursor:
            cursor.execute("INSERT INTO wind_data_silver (winddirabs) VALUES (%s);", (clean_value,))
        self.conn.commit()

    def save_gold(self, avg_value: float) -> None:
        with self.conn.cursor() as cursor:
            cursor.execute("INSERT INTO wind_data_gold (avg_winddirabs, "
                           "calculated_at) VALUES (%s, NOW());", (avg_value,))
        self.conn.commit()

    def get_silver_directions(self) -> List[float]:
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT winddirabs FROM wind_data_silver;")
            rows = cursor.fetchall()
            return [row[0] for row in rows]
