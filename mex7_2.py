import re
import sys
import argparse
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('pattern', type=str, nargs=1) # pattern means the search keywords
    parser.add_argument('start', type=str, nargs=1)   # start means the search startpoint
    parser.add_argument('-r', action='store_true')    # -r means enable/disable recursive search
                                                    
    return parser.parse_args()


def find_in_file(startpoint, keywords):
    try:
        lines = open(startpoint).readlines()        
    except UnicodeDecodeError:                        
        print(f"Binary file {startpoint} matches.")   
        return

    expr = re.compile(keywords)                       # We can replace expr=re.compile(pattern) and expr.search(line) with expr=re.search(pattern, line)
    for line in lines:
        if expr.search(line):
            print(line, end="")

args = parse_args()

if args.r:  
    start_path = Path(args.start[0])
    for f in start_path.rglob("*"):                
        if f.is_file():
            find_in_file(f, args.pattern[0])
else:
    find_in_file(args.start[0], args.pattern[0])


# re.compile(pattern, flags=0):
# Compile a regular expression pattern into a regular expression object, which can be used for matching using its match(), search() and other methods, described below.
# The sequence:  prog = re.compile(pattern); result = prog.search(string)
# is equivalent to: result = re.search(pattern, string)
# However, using re.compile() and saving the resulting regular expression object for reuse is more efficient when the expression will be used several times in a single program.
# Note: The compiled versions of the most recent patterns passed to re.compile() and the module-level matching functions are cached, 
# so programs that use only a few regular expressions at a time needn’t worry about compiling regular expressions.
# https://docs.python.org/3/library/re.html#re.compile
