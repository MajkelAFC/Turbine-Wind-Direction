from src.domain.analytics import WindAnalyticsService
from src.domain.repository import WindTurbineRepository


class GoldWindAnalyticsLoader:
    def __init__(self, repo: WindTurbineRepository):
        self.repo = repo

    def load_gold_data(self) -> float:
        # 1. Fetch clean directions from the Silver layer
        directions = self.repo.get_silver_directions()

        # 2. Calculate the average direction using the domain service
        avg_direction = WindAnalyticsService.calculate_average_direction(directions)

        # 3. Save the aggregated result into the Gold layer
        self.repo.save_gold(avg_direction)

        return avg_direction