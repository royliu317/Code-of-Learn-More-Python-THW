import argparse

parser = argparse.ArgumentParser()  # 1.创建一个解析器：使用argparse的第1步是创建一个ArgumentParser对象，它会保存把命令行解析成Python数据类型所需要的所有信息。

parser.add_argument('files', metavar='F', type=str, nargs='+') # 2.添加参数：调用add_argument()方法向ArgumentParser添加程序的参数信息。通常情况下，
parser.add_argument('-n', '--numbers', action='store_true', help='Print line numbers') # 这些信息告诉ArgumentParser如何接收命令行上的字符串并将它们转换成对象。这些信息被保存下来并在调用parse_args()时用到。

args = parser.parse_args()          # 3.解析参数：ArgumentParser通过parse_args()方法解析参数。它将检查命令行，把每个参数转换成恰当的类型并采取恰当的动作。在大部分情况下，这意味着将从命令行中解析出来的属性建立一个简单的Namespace对象。在脚本中，parse_args()调用一般不带参数，ArgumentParser将根据sys.argv自动确定命令行参数。
print(">>> parsed args: ", args)

line_number = 1
for in_file_name in args.files:    
    in_file = open(in_file_name)
    if args.numbers:               
        #print(args.numbers)        
        for line in in_file.readlines():
            print(f"\t{line_number}\t {line}", end='')
            line_number += 1
        print()
    else:
        print(in_file.read())



# parse_args(): ArgumentParser.parse_args(args=None, namespace=None)
# class argparse.Namespace
# enumerate() ：enumerate(sequence, [start=0])
# readlines() ：fileObject.readlines()