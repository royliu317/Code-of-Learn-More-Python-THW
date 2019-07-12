import argparse
import os

parser = argparse.ArgumentParser()  

parser.add_argument('path', metavar='Path', type=str, help="Input search path")    
parser.add_argument('name', metavar='Name', type=str, help="Input search file name")  
parser.add_argument('-d', '--directory', action='store_false', help='Search directory type')
parser.add_argument('-e', '--exec', help='Exectue command')   

args = parser.parse_args()

def search_file(path, name):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            search_file(item_path, name)
        elif os.path.isfile(item_path):
            if name in item:
                print(item_path)
            else:
                pass        
        else:
            pass

def search_folder(path, name):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path): 
            if name in item:    # 此处的 in 与 for...in 中的in是不同的，这个in表示“被包含于”的意思（类似于搜索时的部分匹配，而非完全匹配）
                print(item_path)
            else:
                pass
            search_folder(item_path, name)
        else:
            pass


if args.directory:
    search_file(args.path, args.name)
else:
    search_folder(args.path, args.name)

if args.exec:
        os.system(args.exec)
else:
    pass


# python笔记之按文件名搜索指定路径下的文件: https://www.cnblogs.com/hyacinthwyd/p/8997917.html
# python之OS模块详解: https://www.cnblogs.com/ginvip/p/6439679.html

# python中os.path.isdir()和os.path.isfile()的正确用法: 
# os.path.isdir()和os.path.isfile()需要传入的参数是绝对路径，但是os.listdir()返回的只是一个某个路径下的文件和列表的名称.**
# 常见错误：直接使用os.listdir()的返回值当做os.path.isdir()和os.path.isfile()的入参
# 正确用法：需要先使用python路径拼接os.path.join()函数，将os.listdir()返回的名称拼接成文件或目录的绝对路径再传入os.path.isdir()和os.path.isfile().
# https://www.jianshu.com/p/582910d13501



# find . -name "*.txt" -print
# find . -name "*.rb" -exec rm {} \;

# -print    os.listdir()
# -name	    os.path.isfile()
# -type	    os.path.isdir()
# -exec	    os.system()