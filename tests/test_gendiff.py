from gendiff.src.gendiff import get_fixture_path
from gendiff.src.parsers import parse_files


def test_generate_diff_json():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    file_out_path = open(get_fixture_path('expected_file.txt'), "r")
    result = file_out_path.read()
    assert parse_files(file1, file2) == result


def test_generate_diff_yml():
    file1 = get_fixture_path('file1.yml')
    file2 = get_fixture_path('file2.yml')
    file_out_path = open(get_fixture_path('expected_file.txt'), "r")
    result = file_out_path.read()
    assert parse_files(file1, file2) == result


def test_generate_diff_yaml():
    file1 = get_fixture_path('file1.yaml')
    file2 = get_fixture_path('file2.yaml')
    file_out_path = open(get_fixture_path('expected_file.txt'), "r")
    result = file_out_path.read()
    assert parse_files(file1, file2) == result
