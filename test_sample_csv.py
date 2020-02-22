import pytest
from .sample_csv import *

def test_make_selection():
    choices_to_make = 4
    csv_data = ['@tim','@kelly','@steve','@mark','@john','@sam']
    random_selection = make_selection(csv_data, choices_to_make)
    assert len(random_selection) == choices_to_make