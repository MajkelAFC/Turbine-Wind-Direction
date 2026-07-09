import csv
from src.domain.wind_turbine import WindRecord
from src.domain.repository import WindTurbineRepository

def load_csv_to_bronze(file_path: str, repo: WindTurbineRepository) -> None:
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            record = WindRecord(row['WindDirAbs'])
            repo.save(record)
            print(f"Record saved: {record.winddirabs}")