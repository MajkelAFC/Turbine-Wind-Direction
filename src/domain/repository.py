from src.domain.wind_turbine import WindRecord
from typing import List

class WindTurbineRepository:
    def save(self, record: WindRecord) -> None:
        pass

    def save_silver(self, clean_value: float) -> None:
        pass

    def save_gold(self, clean_value: float) -> None:
        pass

    def get_silver_directions(self) -> List[float]:
        pass