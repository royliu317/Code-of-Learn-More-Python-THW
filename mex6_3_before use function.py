# find - 在目录中，搜索指定文件

from pathlib import Path                         # Path模块默认支持使用通配符*
import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument('start', type=str, nargs=1)  # nargs=1: 确保只读取第一个传入的参数（即要搜索的路径）。start means the search startpoint
parser.add_argument('--name', type=str)          # search name
parser.add_argument('--type' , type=str)         # search type

args = parser.parse_args()


start_path = Path(args.start[0])                 # args.start[0]: 从args.start列表中取出第一个传入的参数（即要搜索的路径，作为第1个列表项以str类型保存）
print("start_path is: ", start_path)

def name_find(args):
if args.name and not args.type:
    for f in start_path.rglob(args.name):        # 在start_path路径下（包括子folders），找出所有等于args.name的items，并循环传给f变量
        print(f)                                 # 本代码，使用Path的rglob方法，搜索匹配的文件名，因此args.name(即--name)参数可以使用通配符，例如指定为"*.txt"，而非只能使用特定的文件名

elif args.type:
    if args.type not in ['d', 'f']:
        print(f"Unknown type: {args.type}")
        sys.exit(1)
    for f in start_path.rglob(args.name or '*'): # 在start_path路径下（包括子folders），找出所有等于args.name的items。注意：rglob的start_path必须是一个相对路径，绝不能只是一个文件名
        if args.type == "d" and f.is_dir():      # 如果args.name为空（即未使用--name参数，只使用--type参数），则将该路径下所有内容循环传给f变量（Path默认支持使用通配符*）
            print(f)
        elif args.type == "f" and f.is_file():
            print(f)
        else:
            pass
                
else:
    print("You need either --name or --type")




# Path.glob(pattern):
# Glob the given relative pattern（传入给glob的必须是一个相对路径）in the directory represented by this path, yielding all matching files (of any kind).
# The “**” pattern means “this directory and all subdirectories, recursively”. In other words, it enables recursive globbing.
# https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob

# Path.rglob(pattern): 
# This is like calling Path.glob() with “**/” added in front of the given relative pattern.
#https://docs.python.org/3/library/pathlib.html#pathlib.Path.rglob

# 文件通配符 - glob模块提供了一个函数用于从目录通配符搜索中生成文件列表:
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
# argparse — 命令行选项、参数和子命令的解析器: https://www.cnblogs.com/xiaofeiIDO/p/6154953.html
# Zed's Answer: https://github.com/zedshaw/learn-more-python-the-hard-way-solutions/blob/master/ex06_find/find.py