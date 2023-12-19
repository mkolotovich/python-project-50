from gendiff.src.gendiff import get_fixture_path
from gendiff.src.gendiff import generate_diff
import os
import pathlib


def test_generate_diff():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    file2_path = open(os.path.join(
        pathlib.Path(__file__).parent.parent.absolute(),
        'tests', 'fixtures', 'expected_file.txt'), "r")
    result = file2_path.read()
    assert generate_diff(file1, file2) == result
