# Below code is to read the content in specific file and then display it based on the the setting of delim and field

import re
import argparse

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('start', type=str, nargs=1, help='Input the startpoint/file to cut') 
    parser.add_argument('-d', '--delimiter', help='Indicate the fields delimiter')
    parser.add_argument('-f', '--fields', help='Select only these fields')

    return parser.parse_args()

args = parse_args()

in_file = open(args.start[0])                   # in_file's type is fileObject
if args.delimiter and args.fields:
    for line in in_file.readlines():            # line's type is string
        line_list = line.split(args.delimiter)  # args.delimite's type is string. line_list's type is list
        num_list = args.fields.split(',')       # args.fields's type is string. num_list's type is list 
        for num in num_list:                    # num's type is str
            print(line_list[int(num)-1].strip('\n'), end=" ") 
        print()
else:
    print(in_file.read())



# split(): str.split(str="", num=string.count(str))
# strip()：str.strip([chars])