from src.domain.wind_turbine import WindRecord


def test_valid_reading_is_accepted():
    record = WindRecord(180.5)
    assert record.get_clean_data() == 180.5


def test_negative_reading_is_rejected():
    record = WindRecord(-5)
    assert record.get_clean_data() is None


def test_reading_above_360_is_rejected():
    record = WindRecord(400)
    assert record.get_clean_data() is None
