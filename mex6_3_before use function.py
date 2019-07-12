from pathlib import Path                         
import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument('start', type=str, nargs=1)  # nargs=1: Get the first parameter passed in. start means the search startpoint
parser.add_argument('--name', type=str)          # search name
parser.add_argument('--type' , type=str)         # search type

args = parser.parse_args()


start_path = Path(args.start[0])                 
print("start_path is: ", start_path)

def name_find(args):
if args.name and not args.type:
    for f in start_path.rglob(args.name):        
        print(f)                                 

elif args.type:
    if args.type not in ['d', 'f']:
        print(f"Unknown type: {args.type}")
        sys.exit(1)
    for f in start_path.rglob(args.name or '*'): 
        if args.type == "d" and f.is_dir():      
            print(f)
        elif args.type == "f" and f.is_file():
            print(f)
        else:
            pass
                
else:
    print("You need either --name or --type")




# Path.glob(pattern):
# Glob the given relative patternin the directory represented by this path, yielding all matching files (of any kind).
# The “**” pattern means “this directory and all subdirectories, recursively”. In other words, it enables recursive globbing.
# https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob

# Path.rglob(pattern): 
# This is like calling Path.glob() with “**/” added in front of the given relative pattern.
#https://docs.python.org/3/library/pathlib.html#pathlib.Path.rglob

# import glob
# glob.glob('*.py')
# --> ['primes.py', 'random.py', 'quote.py']

# Path.is_dir()
# Return True if the path points to a directory (or a symbolic link pointing to a directory), False if it points to another kind of file.
# False is also returned if the path doesn’t exist or is a broken symlink; other errors (such as permission errors) are propagated.
# https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_dir

# Path.is_file()
# Return True if the path points to a regular file (or a symbolic link pointing to a regular file), False if it points to another kind of file.
# False is also returned if the path doesn’t exist or is a broken symlink; other errors (such as permission errors) are propagated.
# https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_file

# pathlib — Object-oriented filesystem paths: https://docs.python.org/3/library/pathlib.html
