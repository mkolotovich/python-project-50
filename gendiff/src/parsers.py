import json
import yaml
from yaml.loader import SafeLoader
import os
import pathlib


def get_fixture_path(filename):
    return os.path.join(pathlib.Path(__file__).parent.parent.parent.absolute(),
                        'tests', 'fixtures', filename)


def parser(data, format):
    match format:
        case '.json':
            return json.load(open(get_fixture_path(data)))
        case '.yaml':
            return yaml.load(open(get_fixture_path(data)), Loader=SafeLoader)
        case '.yml':
            return yaml.load(open(get_fixture_path(data)), Loader=SafeLoader)

