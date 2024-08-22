from app.main import get_human_age


def test_get_human_age_zeros() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_below_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_get_human_age_below_second_year() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_get_human_age_second_year() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_get_human_age_below_third_year() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_get_human_agew_third_and_second_years() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_get_human_age_large_numbers() -> None:
    assert get_human_age(100, 100) == [21, 17]
