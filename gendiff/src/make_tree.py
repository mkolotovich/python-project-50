import functools


def isValueObject(node, file1, file2):
    if (type(file1.get(node)) == dict and type(file2.get(node)) == dict):
        return True
    return False


def make_node(key, type, children, **kwargs):
    node = {
        "key": key,
        "type": type,
        "children": children
    }
    node.update(kwargs)
    if (node.get('value') is False):
        node['value'] = 'false'
    if (node.get('value') is True):
        node['value'] = 'true'
    if ('new_value' in node and node.get('new_value') is None):
        node['new_value'] = 'null'
    return node


def build_node(el, parsed_data1, parsed_data2):
    if (isValueObject(el, parsed_data1, parsed_data2)):
        sub_keys1 = parsed_data1.get(el)
        sub_keys2 = parsed_data2.get(el)
        keys1 = list(sub_keys1.keys())
        keys2 = list(sub_keys2.keys())
        keys1.extend(keys2)
        inner_keys = set(keys1)
        sortedKeys = sorted(inner_keys)
        return make_node(el, 'nested', make_tree(sortedKeys,
                                                 sub_keys1, sub_keys2))
    if (parsed_data1.get(el) == parsed_data2.get(el)):
        return make_node(el, 'unchanged', [], value=parsed_data2[el])
    if (el in parsed_data1 and el in parsed_data2):
        if (parsed_data1.get(el) != parsed_data2.get(el)):
            return make_node(el, 'updated', [], value=parsed_data1[el],
                             new_value=parsed_data2[el])
    if (el in parsed_data1):
        return make_node(el, 'removed', [], value=parsed_data1[el])
    return make_node(el, 'added', [], value=parsed_data2[el])


def make_tree(keys, parsed_data1, parsed_data2):
    return list(map(functools.partial(build_node, parsed_data1=parsed_data1,
                                      parsed_data2=parsed_data2), keys))


def build_tree(parsed_data1, parsed_data2):
    keys1 = list(parsed_data1.keys())
    keys2 = list(parsed_data2.keys())
    keys1.extend(keys2)
    keys = set(keys1)
    sortedGroups = sorted(keys)
    res = make_tree(sortedGroups, parsed_data1, parsed_data2)
    tree = make_node('', 'root', res)
    return tree
