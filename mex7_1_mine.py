import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('keyword', metavar='K', type=str, nargs=1, help='Input the keyword for the search') 
parser.add_argument('file', metavar='F', type=str, nargs=1, help='Input the (path and) file for the search ') 

args = parser.parse_args()

in_file = open(args.file[0])
keywords = args.keyword[0]

for line in in_file.readlines():
    if re.search(keywords, line):
        print(line, end='')
    else:
        pass



# re — Regular expression operations： https://docs.python.org/3/library/re.html