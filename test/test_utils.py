"""
The purpose of this file is to make sure that all tests pass.
"""

import pytest
from utils.utils import days_to_timestamp

@pytest.mark.parametrize("a, b, resultat", [
    ('2025-01-01', 10, 1734822000),
])
def test_days_to_timestamp(a, b, resultat):
    """ Teste un cas normal. """
    assert days_to_timestamp(a, b) == resultat

def test_days_to_timestamp_negative():
    """ Vérifie que la fonction lève une exception quand nb_jours est négatif. """
    with pytest.raises(ValueError, match="nb_days must be greater than or equal to zero."):
        days_to_timestamp("2025-01-01", -5)

def test_days_to_timestamp_wrong_pattern():
    """ Vérifie que la fonction lève une exception quand la format de la date est incorrect. """
    with pytest.raises(ValueError, match="The date provided doesn't match the expected pattern \(YYYY-MM-DD\)\."):
        days_to_timestamp("20250101", 5)

if __name__ == "__main__":
    pytest.main()