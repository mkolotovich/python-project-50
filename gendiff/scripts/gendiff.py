import argparse
import json
import os
import pathlib

parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.', add_help = False)
parser.add_argument('first_file')     
parser.add_argument('second_file')    
parent_group = parser.add_argument_group (title='optional arguments')
parent_group.add_argument ( '-h','--help', action='help', help='show this help message and exit')
parent_group.add_argument('-f', '--format', help='set format of output')
args = parser.parse_args()

def main():
    print(generate_diff(args.first_file, args.second_file))
def get_key(item):
    return list(item.keys())[0]
def dict_to_list (dict, list):
    for prop1, value1 in dict.items():
        list.append({prop1: value1})
def compare (a):
    return list(a.keys())[0][2:]
def generate_diff(file_path1, file_path2):
    file1 = json.load(open(os.path.join(pathlib.Path(__file__).parent.absolute(), file_path1)))
    file2 = json.load(open(os.path.join(pathlib.Path(__file__).parent.absolute(), file_path2)))
    result = {}
    data1 = []
    data2 = []
    resultArray = []
    dict_to_list(file1, data1)
    dict_to_list(file2, data2)
    data1.sort(key=get_key)
    data2.sort(key=get_key)
    for prop, in data1:
        for prop1, value1 in file2.items():
            if prop1 in file1 and file1[prop1] == value1:
                result[f'  {prop1}'] = value1
            else:
                if prop1 in file1 and file1[prop1] != value1:
                    result[f'- {prop1}'] = file1[prop1]
                    result[f'+ {prop1}'] = value1
                elif prop not in file2:
                    result[f'- {prop}'] = file1[prop]
                else:
                    result[f'+ {prop1}'] = value1
    dict_to_list(result, resultArray)
    resultArray.sort(key=compare)
    sortedObject = {}
    for prop1 in resultArray:
        sortedObject[list(prop1.keys())[0]] = list(prop1.values())[0]
    resultString = json.dumps(sortedObject, indent=2)
    resultValue = resultString.replace('"','')
    return resultValue

if __name__ == '__main__':
    main()