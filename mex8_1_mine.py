# 本代码实现的是先读取指定文件的内容，然后根据delim和field去cut并显示出来

import re
import argparse

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('start', type=str, nargs=1, help='Input the startpoint/file to cut') 
    parser.add_argument('-d', '--delimiter', help='Indicate the fields delimiter')
    parser.add_argument('-f', '--fields', help='Select only these fields')

    return parser.parse_args()

args = parse_args()

in_file = open(args.start[0])                   # in_file的type是fileObject
if args.delimiter and args.fields:
    for line in in_file.readlines():            # line的type是str
        line_list = line.split(args.delimiter)  # args.delimite的type是str；line_list的type是list
        num_list = args.fields.split(',')       # args.fields的type是str；num_list的type是list 
        for num in num_list:                    # num的type是str
            print(line_list[int(num)-1].strip('\n'), end=" ") # 命令行参数在传入时，都会自动转换为str类型。所以此处的加法，需先转化为int。因为readline()函数读取的一行内容中含有换行符\n，因此用strip('\n')去掉每行末的换行符
        print()
else:
    print(in_file.read())



# split()方法 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则仅分隔 num 个子字符串
# str.split(str="", num=string.count(str))
# 参数str：分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。num：分割次数
# 返回值：返回分割后的 字符串列表List 
# http://www.runoob.com/python3/python3-string-split.html

# strip()方法语法：str.strip([chars])
# 参数chars: 移除字符串头尾指定的字符序列
# 返回值: 返回移除字符串头尾指定的字符序列生成的新字符串
# strip()如果不带参数，默认是清除两边的空白符，例如：/n, /r, /t, ' '等
# http://www.runoob.com/python3/python3-string-strip.html