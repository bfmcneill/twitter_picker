import twitter_picker.utils as utils


def test_project_root_is_path_object():
    import pathlib
    assert isinstance(utils.get_project_root(), pathlib.Path)


def test_project_root_is_valid_path():
    import pathlib
    assert utils.get_project_root().exists()


def test_project_root_is_dir():
    import pathlib
    assert utils.get_project_root().is_dir()
