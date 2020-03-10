

# from click.testing import CliRunner
# runner = CliRunner()
# def test_add():
#     response = runner.invoke(add, ['test-user', '-m', '480083220'])
#     assert response.exit_code == 0
#     assert "test-user Added!" in response.output
#     assert "{'mobile': '480083220'}" in response.output

import pytest
from twitter_picker.cli.cli import add, random_choices


@pytest.fixture(scope="session")
def csv_file_path(tmpdir_factory):
    # TODO: need to do something to ensure the data in a single colum
    # TODO: need to do something to ensure that any duplicates are handled with set()
    # TODO: breaks when n > rows of data
    import csv
    data = [
        ('handle',),
        ('@test1',),
        ('@test2',),
        ('@test3',),
        ('@test4',),
        ('@test5',),
        ('@test6',),
        ('@test7',),
    ]

    directory = tmpdir_factory.mktemp('data')
    csv_filename = directory.join('handles.csv')

    with open(csv_filename, 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for item in data:
            writer.writerow(item)
    return csv_filename


@pytest.mark.runner_setup(charset='cp1251', env={'USER': 'Anon'}, echo_stdin=True)
def test_add(cli_runner):
    response = cli_runner.invoke(add, ['test-user', '-m', '480083220'])
    assert response.exit_code == 0
    assert "test-user Added!" in response.output
    assert "{'mobile': '480083220'}" in response.output
    assert "os.getenv('USER')==Anon" in response.output


@pytest.mark.runner_setup(charset='cp1251', echo_stdin=True)
def test_random_choices(csv_file_path, cli_runner):

    response = cli_runner.invoke(
        random_choices, ['--filepath', csv_file_path, '--n-select', '3'])

    assert response.exit_code == 0
    assert 'winner #1' in response.output
    assert 'winner #2' in response.output
    assert 'winner #3' in response.output
    # to see output use the following command
    # pytest tests/test_cli.py::test_random_choices  -v -s
    print('\n\n')
    print('******')
    print(csv_file_path)
    print('\n\n')
    print('\n\n')
    print(response.output)
    print('\n\n')
    print('\n\n')
