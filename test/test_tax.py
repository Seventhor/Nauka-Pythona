from tax import calculate_tax


def test_if_highest_tax_is_20_percent():
    assert calculate_tax(100_000) == 20_000.0

def test_if_lowest_tax_is_5_percent():
    assert calculate_tax(1000) == 50.0
