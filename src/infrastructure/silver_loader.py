import logging

from src.domain.wind_turbine import WindRecord
from src.domain.repository import WindTurbineRepository

logger = logging.getLogger(__name__)


def process_bronze_to_silver(conn, repo: WindTurbineRepository) -> None:
    accepted = 0
    rejected = 0

    with conn.cursor() as cursor:
        cursor.execute("SELECT winddirabs FROM wind_data_bronze;")
        rows = cursor.fetchall()
        for row in rows:
            record = WindRecord(winddirabs=row[0])
            clean_val = record.get_clean_data()
            if clean_val is not None:
                repo.save_silver(clean_val)
                accepted += 1
            else:
                rejected += 1

    conn.commit()

    total = accepted + rejected
    logger.info(
        "Silver layer: %s readings processed, %s accepted, %s rejected",
        total, accepted, rejected,
    )
