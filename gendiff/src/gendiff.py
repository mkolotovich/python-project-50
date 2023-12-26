import pathlib
from gendiff.src.read_file import read_file
from gendiff.src.parsers import parser
from gendiff.src.make_tree import build_tree
from gendiff.src.formatters.index import format_data


def get_data(file_path):
    data = read_file(file_path)
    format = pathlib.Path(file_path).suffix
    return parser(data, format)


def generate_diff(file_path1, file_path2, format_name='stylish'):
    parsed_data1 = get_data(file_path1)
    parsed_data2 = get_data(file_path2)
    tree = build_tree(parsed_data1, parsed_data2)
    return format_data(format_name, tree)
