import math
from typing import List

class WindAnalyticsService:
    @staticmethod
    def calculate_average_direction(directions: List[float]) -> float:
        if not directions:
            return 0.0

        total_sin = 0.0
        total_cos = 0.0

        for angle in directions:
            # 1. Convert degrees to radians
            radians = math.radians(angle)
            # 2. Sum up the coordinates of the vectors
            total_sin += math.sin(radians)
            total_cos += math.cos(radians)

        # 3. Calculate the average coordinates
        avg_sin = total_sin / len(directions)
        avg_cos = total_cos / len(directions)

        # 4. Calculate the resulting angle in radians using atan2
        avg_radians = math.atan2(avg_sin, avg_cos)

        # 5. Convert radians back to degrees
        avg_degrees = math.degrees(avg_radians)

        # 6. Normalize the result to be between 0 and 360 degrees
        return (avg_degrees + 360) % 360