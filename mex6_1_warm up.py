from pathlib import Path
from sys import argv

_, start, query = argv

start_path = Path(start)

for f in start_path.rglob(query):  
    print(f)


# PS C:\Users\roy\projects\moreZed> python mex6_1.py . *

# pathlib — Object-oriented filesystem paths: https://docs.python.org/3/library/pathlib.html
# Path.rglob(pattern): https://docs.python.org/3/library/pathlib.html#pathlib.Path.rglob
# argparse — 命令行选项、参数和子命令的解析器: https://www.cnblogs.com/xiaofeiIDO/p/6154953.html
# Zed's Answer: https://github.com/zedshaw/learn-more-python-the-hard-way-solutions/blob/master/ex06_find/find.py