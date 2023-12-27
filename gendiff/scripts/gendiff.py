import argparse
from gendiff.src.gendiff import generate_diff

parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.',
    add_help=False)
parser.add_argument('first_file')
parser.add_argument('second_file')
parent_group = parser.add_argument_group(title='optional arguments')
parent_group.add_argument(
    '-h', '--help', action='help', help='show this help message and exit')
parent_group.add_argument('-f', '--format', help='set format of output',
                          choices=['plain', 'stylish', 'json'],
                          default='stylish')
args = parser.parse_args()


def main():
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
