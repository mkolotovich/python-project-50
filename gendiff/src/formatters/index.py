from gendiff.src.formatters.stylish import stylish
from gendiff.src.formatters.plain import plain


def format_data(format_name, structure):
    if format_name == 'plain':
        return plain(structure)
    if format_name == 'json':
        return json(structure)
    if format_name == 'stylish':
        return stylish(structure)
    return Exception(f'incorrect format: ${format_name}!')
