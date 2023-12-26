from gendiff.src.read_file import get_fixture_path
from gendiff.src.gendiff import generate_diff


def test_generate_diff_json():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    file_out_path = open(get_fixture_path('expected_file.txt'), "r")
    result = file_out_path.read()
    assert generate_diff(file1, file2) == result


def test_generate_diff_yml():
    file1 = get_fixture_path('file1.yml')
    file2 = get_fixture_path('file2.yml')
    file_out_path = open(get_fixture_path('expected_file.txt'), "r")
    result = file_out_path.read()
    assert generate_diff(file1, file2) == result


def test_generate_diff_yaml():
    file1 = get_fixture_path('file1.yaml')
    file2 = get_fixture_path('file2.yaml')
    file_out_path = open(get_fixture_path('expected_file.txt'), "r")
    result = file_out_path.read()
    assert generate_diff(file1, file2) == result


def test_generate_diff_nested_json():
    file1 = get_fixture_path('file1_nested.json')
    file2 = get_fixture_path('file2_nested.json')
    file_out_path = open(get_fixture_path('expected_nested_file.txt'), "r")
    result = file_out_path.read()
    assert generate_diff(file1, file2) == result


def test_generate_diff_nested_yaml():
    file1 = get_fixture_path('file1_nested.yaml')
    file2 = get_fixture_path('file2_nested.yaml')
    file_out_path = open(get_fixture_path('expected_nested_file.txt'), "r")
    result = file_out_path.read()
    assert generate_diff(file1, file2) == result
