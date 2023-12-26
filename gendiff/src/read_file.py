import os
import pathlib


def get_fixture_path(filename):
    return os.path.join(pathlib.Path(__file__).parent.parent.parent.absolute(),
                        'tests', 'fixtures', filename)


def read_file(file_name):
    fullPath = get_fixture_path(file_name)
    data = open(fullPath)
    return data
