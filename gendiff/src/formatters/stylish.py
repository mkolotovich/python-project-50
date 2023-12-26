import functools
import os

space = 2
depth_space = 4


def inner(acc, el, replace_inner, cb, depth):
    key, val = el
    if type(val) is not dict:
        newAcc = f'{replace_inner * (depth)}{key}: {val}\n'
    else:
        newAcc = f'{replace_inner * (depth)}{key}: '
        newAcc += f'{cb(val, replace_inner, depth + depth_space)}'
        newAcc += f'{replace_inner * (depth)}' + '}\n'
    return acc + newAcc


def stringify(value, replacer=' ', space_count=1):
    if type(value) is not dict:
        return f'{value}'

    def cb(current_value, replace_inner, depth):
        entries = current_value.items()
        return functools.reduce(functools.partial(inner,
                                                  replace_inner=replace_inner,
                                                  cb=cb,
                                                  depth=depth), entries, '{\n')
    res = f'{cb(value, replacer, space_count)}'
    res += f"{' ' * (space_count - depth_space)}}}"
    return res


def mk_str(item, depth):
    if item["type"] == 'nested':
        result = f"{' ' * (depth_space * (depth - 1) + space)}"
        result += f'  {item["key"]}: {{\n'
        return result
    return ''


def stylish(tree):
    def cb(data, result='', depth=0):
        key = data.get('key')
        type = data.get('type')
        children = data.get('children')
        if "value" in data:
            value = data.get('value')
            print_val = stringify(value, ' ', (depth + 1) * depth_space)
        if "new_value" in data:
            new_value = data.get('new_value')
            print_new_val = stringify(new_value, ' ', (depth + 1) * depth_space)
        match type:
            case 'root':
                child = list(map(lambda item: cb(item,
                                                 mk_str(item, depth + 1),
                                                 depth + 1),
                                 children))
                res = f'{{\n{result}{os.linesep.join(child)}\n'
                res += f"{' ' * (space * depth * space)}}}"
                return res
            case 'nested':
                child = list(map(lambda item: cb(item,
                                                 mk_str(item, depth + 1),
                                                 depth + 1),
                                 children))
                res = f'{result}{os.linesep.join(child)}\n'
                res += f"{' ' * (space * depth * space)}}}"
                return res
            case 'updated':
                res = f'{result}'
                res += f"{' ' * (depth_space * (depth - 1) + space)}- {key}"
                res += f': {print_val}\n'
                res += f"{' ' * (depth_space * (depth - 1) + space)}+ {key}"
                res += f': {print_new_val}'
                return res
            case 'added':
                res = f"{result}{' ' * (depth_space * (depth - 1) + space)}"
                res += f'+ {key}: {print_val}'
                return res
            case 'removed':
                res = f"{result}{' ' * (depth_space * (depth - 1) + space)}"
                res += f'- {key}: {print_val}'
                return res
            case 'unchanged':
                res = f"{result}{' ' * (depth_space * (depth - 1) + space)}"
                res += f'  {key}: {print_val}'
                return res
    return cb(tree)
