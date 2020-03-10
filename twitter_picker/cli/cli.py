"""Console script for Twitter Picker."""
import os
import click
from twitter_picker import make_selection, load_handles
from twitter_picker.utils import get_project_root


@click.group()
def main():
    """Main Entrypoint"""


@main.command()
@click.argument('name', default='John')
@click.option('--mobile', '-m', required=True)
def add(name, mobile):
    '''Add Contact
    https://github.com/Stranger6667/pytest-click
    https://dev.to/wangonya/testing-click-applications-with-pytest-2o79
    '''
    click.echo(f'{name} Added!')
    click.echo({'mobile': mobile})
    click.echo("os.getenv('USER')=={}".format(os.environ.get('USER', 'Anon')))


@main.command()
@click.option(
    '-i',
    '--filepath',
    'csv_filepath',
    type=click.Path(exists=True, resolve_path=True),
    default=get_project_root().joinpath('handles.csv').as_posix(),
    show_default=True,
    help="specify csv filepath, default is `handles.csv` in project root"
)
@click.option(
    '-n',
    '--n-select',
    'choice_count',
    type=int,
    required=True,
    default=5,
    show_default=True,
    help="Specify how many selections to make"
)
def random_choices(csv_filepath, choice_count):
    """Make random choices"""
    MESSAGE = ' winner #{} -> {}'
    handles = load_handles(csv_filepath)
    selection = make_selection(handles, choice_count=choice_count)
    [click.echo(MESSAGE.format(idx+1, item))
     for idx, item in enumerate(selection)]
