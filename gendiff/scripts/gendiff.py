import argparse

parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.', add_help = False)
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
parser.add_argument('first_file')     
parser.add_argument('second_file')    
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')
parent_group = parser.add_argument_group (title='optional arguments')
 
parent_group.add_argument ( '-h','--help', action='help', help='show this help message and exit')

args = parser.parse_args()


def main():
    print(args.accumulate(args.integers))

if __name__ == '__main__':
    main()