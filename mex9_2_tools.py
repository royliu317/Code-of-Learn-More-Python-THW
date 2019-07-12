# 本代码要实现的sed的原生参数包括：
# s / regexp / replacement: Attempt to match regexp against the pattern space
# 即支持正则表达式的replace方式。例: python sed.py 's/test/SAMPLE/g' file_name （test是file_name文件中的被替换词，SAMPLE是替换词。
# R filename：Append a line read from filename. Each invocation of the command reads a line from the file. This is a GNU extension. Begin a block of commands (end with a ' '). 
# 即追加信息至filename的每行中。例: python sed.py 'r in_file_name' file_name （in_file_name是要追加到file_name文件中的追加项）。
# 注：如上的 file_name 所表示的应是文件的相对或绝对路径，如'./mex9_related/test.txt', 'mex9_2_tools.py', 'C:\\Users\\roy\\projects\\moreZed\\mex9_related\\test.txt', 'mex9_related\test.txt'
# 注: Zed的code中用的都是小写r，但实际应该是大写R这个参数（对于原生的sed，r、R是两个参数，代表的是不同功能）


import re

def parse_script(script):                          # No.2 - 通过该函数，实现从用户输入的script命令行参数中，取到command（s或r）、args(pattern, replace 或 in_file_name) 变量，即 script --> command, args
    if script[0] == "s":                           # 判断第1个命令行参数(argv[1]) 中的第一个元素(script[0]) 是否为s或r，例如 's/test/SAMPLE/g' file_name 或'r in_file_name' file_name
        return ('s', script.split('/')[1:3])       # 如果是s，则取以 / 分隔的第2，3个元素（script[1], script[2]）作为被替换词、替换词（因为script的第1个元素是命令s，第4个元素是另一命令）
    elif script[0] == "r":                         # 如果是r，则取以空格分隔的第2个及之后的元素作为被替换词、替换词（script的第1个元素是命令s，第4个元素是原生的另一命令仅为一致性而在此保留） 
        return ('r', script.split(' ')[1:])        # 此处不能用[1]，因为[1:]切片返回的是list，可供后面的for循环取用，而这种方式返回的是str
    else:
        print("Error, only s supported")
        sys.exit(1)

def do_s(file_name, pattern, replace):             # file_name = 要进行词替换的文件；pattern = 被替换词，replace = 替换词。do_s函数实现了支持正则表达式的词替换方式
    with open(file_name) as f:                     # with 是个好东西，打开文件的时候多使用它，可以避免很多问题
        for line in f.readlines():                 # FileObject.readlines(), python的file object类型，要使用 open() 函数来创建
            fixed = re.sub(pattern, replace, line) # 本代码使用 re.sub() 实现支持正则表达式功能的替换，而非mex7中所用 re.compile()，这是因为Zed提到“when you compile a pattern (via re.compile), it doesn't have the same APIs as the full re module."
            print(fixed, end="")                   # 虽然Zed也提到，“re.sub is not on the compiled regular expression”，但为节省时间进行45分钟的hack，我们就先用能实现的方法就可以了

def do_r(file_name, in_file_name):                 # file_name = 要被追加内容的文件；in_file_name = 追加项。do_r函数实现了将“追加项”中的全部内容，追加/插入到被追加文件的每一行之中
    contents = open(in_file_name).read()
    #print('\n', contents, repr(contents), '\n')

    with open(file_name) as f:
        for line in f.readlines():
            print(line, contents, end='')

def apply_script(command, file_name, args):        # No.3 - 基于command是s或r，调用相应函数并传入相应变量，以进行处理
    if command == "s":          
        do_s(file_name, *args)                     # 因为 do_s 与 do_r 所需要传入的变量的个数是不同的，所以此处用不定长参数*args，以保证当调用两个函数时都可以work
    elif command == "r":
        do_r(file_name, *args)
    else:
        print("Not supported.")
        sys.exit(1)

def sed(script, files):                            # No.1 - 程序运行起点（被sed.py调用的起点）
    command, args = parse_script(script)           # script是str类型，包含 command 和 args 两个变量
    for file_name in files:                        # files是list类型，用于读取要操作的文件，即从用户输入的files命令行参数中取到file_name。此处用for是为实现一次性操作多个文件的功能即调用一次s、r命令同时操作多个文件）
        apply_script(command, file_name, args)     # 取得所需变量后，运行脚本（即调用相应函数，以实现r或s的功能）


#如下函数是Zed额外加的，与上面的函数无关联性
def print_uniq_lines(file_list):                   # 本函数实现的是将file_list中所有文件的所有行，全部一次性无序且无重复地打印出来
    all_lines = set()                              # 创建空的集合类型，并赋给all_lines（Set Type是一个 无序不重复 的元素序列，Zed通过使用该类型来实现元素unique的要求）
    for f in file_list:
        all_lines |= set(f.readlines())            # 赋值符 |= 类似 +=，表示将每次从file_list中读取的文件设为集合类型，然后与all_lines集合取并集并赋给它，等同于set(a) = set(a) | set(b)
        #print("".join(all_lines))
        #all_lines = set()
        #如果unmark如上两行并mark如下行，则函数实现的是依次打印文件列表中的每一个文件，每一个文件是无序且无重复地打印出来，即不同文件中的重复行不会进行去重
        #用这种方式时，上面的1行 all_lines |= set(f.readlines())  可改为 all_lines = set(f.readlines())
    print("".join(all_lines))
    



# 不定长参数: 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
# https://www.runoob.com/python3/python3-function.html

# 预定义的清理行为(with as):
# 一些对象定义了标准的清理行为，无论系统是否成功的使用了它，一旦不需要它了，那么这个标准的清理行为就会执行
# 比如，执行打开文件如open（）的操作时多使用它。因为当执行完毕后，文件会保持打开状态，并没有被关闭
# 关键词 with as 语句就可以保证诸如文件之类的对象在使用完之后，一定会正确地执行它的清理方法
# https://www.runoob.com/python3/python3-errors-execptions.html

# str.replace(old, new[, count])
# Return a copy of the string with all occurrences of substring old replaced by new. If the optional argument count is given, only the first count occurrences are replaced.

# re.sub(pattern被替换词, repl替换词, string, count=0, flags=0)：
# Return the string obtained by replacing the leftmost non-overlapping occurrences of pattern (最左边不重叠出现的pattern) in string by the replacement repl. 
# If the pattern isn’t found, string is returned unchanged. 
# The "repl" can be a string or a function; if it is a string, any backslash escapes in it are processed. 
# If repl is a function, it is called for every non-overlapping occurrence of pattern. The function takes a single match object argument, and returns the replacement string. 
# The "pattern" may be a string or a pattern object. 
# https://docs.python.org/3/library/re.html#re.sub

# Python的文件对象（file object），要使用 open() 函数来创建
# https://www.runoob.com/python3/python3-file-methods.html

# 集合(set):
# 集合类型（Set Type）是一个 无序不重复 元素序列。可以使用大括号 { } 或者 set() 函数创建集合类型
# 注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
# 类似列表推导式，同样集合支持集合推导式(Set comprehension)
# https://www.runoob.com/python3/python3-set.html
# 集合是一个无序不重复元素的集。基本功能包括 关系测试 和 消除重复元素

# 函数 set():
# 它用于创建一个 无序不重复 元素集合(即调用它创建set类型的数据)，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等
# 语法: set([iterable])
# 参数说明：iterable -- 可迭代对象（与列表等不同，不支持通过一次性指定多个字符串对集合元素进行赋值的方式）
# 返回值: 返回新的集合对象
# https://www.runoob.com/python/python-func-set.html

# 集合类型（Set Type）：
# 其update(*others)函数， 等价于 set |= other | ...
# Update the set, adding elements from all others.

# fileObject.readlines():
# readlines() 方法用于读取所有行(直到结束符EOF)并返回列表list，该列表可以由 for... in ... 结构进行处理。 如果碰到结束符EOF则返回空字符串
# 参数: 无
# 返回值: 返回列表，包含所有的行。每一行是列表的一个元素。
# https://www.runoob.com/python3/python3-file-readlines.html
