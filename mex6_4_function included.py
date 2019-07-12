from pathlib import Path
import argparse
import sys

# 4. 定义--name所对应的函数
def name_parameter(start, args):
    for f in start.rglob(args.name):  
        print(f)

# 5. 定义--type所对应的函数
def type_parameter(start, args):
    if args.type not in ['d', 'f']:
        print(f"Unknown type: {args.type}")
        sys.exit(1)
    for f in start.rglob(args.name or '*'):  
        if args.type == "d" and f.is_dir():
            print(f)
        elif args.type == "f" and f.is_file():
            print(f)
        else:
            pass
    
# 3. 基于用户的输入（--name及--type参数的使用），定义搜索逻辑
def find_files(args):
    start_path = Path(args.start[0])      
    
    if args.name and not args.type:
        name_parameter(start_path, args)
    elif args.type:
        type_parameter(start_path, args)
    else:
        print("You need either --name or --type")
        sys.exit(1)

# 1. 设置argparse如何接收与解析命令行字符，并返回解析后的实例化对象（即之前常用的args对象）
def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('start', type=str, nargs=1)   
    parser.add_argument('--name', type=str)
    parser.add_argument('--type' , type=str)

    return parser.parse_args()

# 2. 设置本代码的起始运行点
find_files(parse_args())