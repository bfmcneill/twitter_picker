import pytest
from twitter_picker import make_selection, load_handles


@pytest.fixture(scope="session")
def csv_file_path(tmpdir_factory):
    import csv
    data = [
        ('handle',),
        ('@test1',),
        ('@test2',),
        ('@test3',),
        ('@test4',),
        ('@test5',),
        ('@test5',),
        ('@test6',),
    ]

    directory = tmpdir_factory.mktemp('data')
    csv_filename = directory.join('output.csv')

    with open(csv_filename, 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for item in data:
            writer.writerow(item)
    return csv_filename


def test_read_csv(csv_file_path):
    data_list = load_handles(csv_file_path)
    assert data_list == ['@test1', '@test2', '@test3',
                         '@test4', '@test5', '@test5', '@test6']


def test_make_selection():
    choices_to_make = 3
    csv_data = ['@tim', '@kelly', '@steve', '@mark', '@john', '@sam']
    random_selection = make_selection(csv_data, choices_to_make)
    assert len(random_selection) == choices_to_make
