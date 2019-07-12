#!/usr/bin/env python3.6                              # used in Unix/Linux OS

import sys

def print_uniq_lines(file_list):
    print('file_list: ', file_list, type(file_list))
    all_lines = set()
    #print('file_list: ', file_list, type(file_list)) 

    for f in file_list:                               
        all_lines |= set(f.readlines())               
                
    print("".join(all_lines))


if len(sys.argv) > 1:
    print_uniq_lines(open(f) for f in sys.argv[1:]) 
else:
    print_uniq_lines([sys.stdin])                   # stdin, stdout, stderr - These streams are regular text files like those returned by open().
    


# sys.stdin, sys.stdout, sys.stderr：
# https://docs.python.org/3/library/sys.html?highlight=stdin#sys.stdin
