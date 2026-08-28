from src.domain.analytics import WindAnalyticsService


def test_average_of_simple_directions():
    # Zwykła średnia też by tu zadziałała — 90 i 110 dają 100
    result = WindAnalyticsService.calculate_average_direction([90, 110])
    assert round(result, 2) == 100.0


def test_average_across_north():
    # Sedno projektu: 350 i 10 leżą po obu stronach północy.
    # Zwykła średnia dałaby 180 (południe) — czyli dokładnie odwrotnie.
    result = WindAnalyticsService.calculate_average_direction([350, 10])
    assert round(result, 2) == 0.0


def test_empty_list_returns_zero():
    result = WindAnalyticsService.calculate_average_direction([])
    assert result == 0.0
