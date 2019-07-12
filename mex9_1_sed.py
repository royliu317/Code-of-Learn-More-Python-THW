# 本代码通过调用另一个 mex9_2_tools代码，实现书中所述的sed功能(replace)，例如：
# python sed.py 's/test/SAMPLE/g' file_name
# python sed.py 'r in_file_name' file_name

import sys
import mex9_2_tools

script = sys.argv[1]    # script取第1个命令行参数，如's/test/SAMPLE/g' 或 'r in_file_name'。用[1]的方式，返回的是str类型
files = sys.argv[2:]    # files取第2个及之后的命令行参数，即file_name。用[2:]切片方式，返回的是list类型，以便当需要读取多个文件用以进行s或r操作时使用
                        # argv[0] 是被调用的脚本的文件全名或全路径，从argv[1]开始就是用户传入的数据

mex9_2_tools.sed(script, files)


#如下代码是针对Zed在tools.py中额外加的def print_uniq_line函数，与上面的代码无关联性，测试那个函数时，可以mark如上3行并unmark如下2行，然后直接用python执行mex9_1_sed.py文件，不需再带命令行参数：
#file_list = [open('.\\mex9_related\\test.txt'), open('.\\mex9_related\\test2.txt')]  # 创建由文件类型组成的列表，用于存储每个file object，以便进行后续的file.readlines()操作
#mex9_2_tools.print_uniq_lines(file_list)

# sys.argv
# The list of command line arguments passed to a Python script. sys.argv[0] is the script name. If no script name was passed to the Python interpreter, argv[0] is the empty string.
# https://docs.python.org/3/library/sys.html?highlight=sys%20argv#sys.argv