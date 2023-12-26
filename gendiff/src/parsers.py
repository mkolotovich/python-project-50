import json
import yaml
from yaml.loader import SafeLoader


def parser(data, format):
    match format:
        case '.json':
            return json.load(data)
        case '.yaml':
            return yaml.load(data, Loader=SafeLoader)
        case '.yml':
            return yaml.load(data, Loader=SafeLoader)
