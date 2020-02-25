import pytest
from twitter_picker import make_selection


def test_make_selection():
    choices_to_make = 3
    csv_data = ['@tim', '@kelly', '@steve', '@mark', '@john', '@sam']
    random_selection = make_selection(csv_data, choices_to_make)
    assert len(random_selection) == choices_to_make
