def print_value(value):
    if (type(value) is dict):
        return '[complex value]'
    if (type(value) is str):
        if (value == 'false' or value == 'true' or value == 'null'):
            return f"{value}"
        return f"'{value}'"
    return value


def plain(tree):
    def cb(node, result='', path=''):
        key = node.get('key')
        type = node.get('type')
        children = node.get('children')
        if "value" in node:
            value = node.get('value')
            printed_value = print_value(value)
        if "new_value" in node:
            new_value = node.get('new_value')
            printed_new_value = print_value(new_value)
        node_name = f'{path}{key}'[1:]
        match type:
            case 'root':
                child = list(map(lambda item: cb(item, result, f'{path}{key}.'),
                             children))
                return '\n'.join(child)
            case 'nested':
                res = list(map(lambda item: cb(item, result, f'{path}{key}.'),
                               children))
                filtered = filter(lambda item: item != '', res)
                return '\n'.join(filtered)
            case 'added':
                res = f"{result}Property '{node_name}' was added with value: "
                res += f"{printed_value}"
                return res
            case 'removed':
                return f"{result}Property '{node_name}' was removed"
            case 'updated':
                res = f"{result}Property '{node_name}' was updated. From "
                res += f"{printed_value} to {printed_new_value}"
                return res
            case 'unchanged':
                return ''
    return cb(tree)
