import pathlib
import json
import yaml
from yaml.loader import SafeLoader
from gendiff.src.gendiff import get_fixture_path
from gendiff.src.gendiff import generate_diff


def parser(data, format):
    match format:
        case '.json':
            return json.load(open(get_fixture_path(data)))
        case '.yaml':
            return yaml.load(open(get_fixture_path(data)), Loader=SafeLoader)
        case '.yml':
            return yaml.load(open(get_fixture_path(data)), Loader=SafeLoader)


def parse_files(file1, file2):
    file1_ext = pathlib.Path(file1).suffix
    file2_ext = pathlib.Path(file2).suffix
    return generate_diff(parser(file1, file1_ext), parser(file2, file2_ext))
