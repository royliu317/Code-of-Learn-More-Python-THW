# grep - 在文件中，搜索指定内容

import re
import sys
import argparse
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('pattern', type=str, nargs=1) # pattern means the search keywords
    parser.add_argument('start', type=str, nargs=1)   # start means the search startpoint
    parser.add_argument('-r', action='store_true')    # -r means enable/disable recursive search. 不开启它时，目的就是查询指定文件中的内容，因此args.start此时需是文件名，不能只是相对路径；
                                                      # 开启它时，目的是查询指定目录内所有文件的内容，因此args.start需是相对路径，不能是文件名
    return parser.parse_args()


def find_in_file(startpoint, keywords):
    try:
        lines = open(startpoint).readlines()          # 本代码，使用file.open()打开文件，该方法不支持使用通配符*，因此startpoint（即args.start）参数不能使用通配符*
    except UnicodeDecodeError:                        # 此处作者有一个假设：如果打开某文件时，系统提示Unicode编码错误，则默认该文件是Binary file（实际上该假设并不正确）
        print(f"Binary file {startpoint} matches.")   # 注意：搜索Binary file中的内容，是没有任何意义的
        return

    expr = re.compile(keywords)                       # 其实也可以不用 expr=re.compile(pattern) 和 expr.search(line)，改为 expr=re.search(pattern, line)，但这样用更高效（详见如下）
    for line in lines:
        if expr.search(line):
            print(line, end="")

args = parse_args()

if args.r:  
    start_path = Path(args.start[0])
    for f in start_path.rglob("*"):                   # 将start_path路径（包括子folders）下的所有内容循环传给f变量（Path默认支持使用通配符*）。注意：rglob的start_path必须是一个相对路径，绝不能只是一个文件名
        if f.is_file():
            find_in_file(f, args.pattern[0])
else:
    find_in_file(args.start[0], args.pattern[0])


# 对于File模块来说，它的很多API，调用后返回的到底是Unicode还是Bytes，是很不明确的。
# 对于readline()来说，它返回的是Unicode，但很多其他API返回的则是Bytes。

# re.compile(pattern, flags=0):
# Compile a regular expression pattern(正则表达式公式) into a regular expression object, which can be used for matching using its match(), search() and other methods, described below.
# The sequence:  prog = re.compile(pattern); result = prog.search(string)
# is equivalent to: result = re.search(pattern, string)
# However, using re.compile() and saving the resulting regular expression object for reuse is more efficient when the expression will be used several times in a single program.
# Note: The compiled versions of the most recent patterns passed to re.compile() and the module-level matching functions are cached, 
# so programs that use only a few regular expressions at a time needn’t worry about compiling regular expressions.
# https://docs.python.org/3/library/re.html#re.compile


# 如果不使用
#  File "mex7.py", line 15, in find_in_file
#    lines = open(startpoint).readlines()
#PermissionError: [Errno 13] Permission denied: '.'