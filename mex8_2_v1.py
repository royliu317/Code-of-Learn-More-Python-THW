# 本代码实现的不是读取文件内容然后cut，而是让用户直接手输内容，同时进行cut

import sys

_, delim, fields = sys.argv
split_at = [int(x) for x in fields.split(',')]  # 列表推倒式：通过for循环取出fields.split列表内的每个元素，转换为int类型，并存入新的split_at[]列表内
#print(split_at, type(split_at[0]))

while True:                                     # 无限循环，实现用户可以input无限行的功能（但每行的input会立即根据delim和field被cut，并展示在下一行；而非用户全部输完所有行后，再去cut）
    try:
        line = input()
        cuts = line.split(delim)                
        for i in split_at:
            print(f"{cuts[i]} ", end="")
        print()

    except KeyboardInterrupt:                  # 因为是无限循环，所以会用到ctrl+c退出循环。由于这样退出时系统会报错，所以通过except捕获该错误，并执行退出命令
        sys.exit(0)
    except IndexError:                         # 因为用户输入的fields超出index范围时，系统会报错，所以通过except捕获该错误，并直接pass掉即可
        pass



# 列表推导式：
# https://www.runoob.com/python3/python3-data-structure.html
# 推导式的执行顺序：各语句之间是嵌套关系，左边第二个语句是最外层，依次往右进一层，左边第一条语句是最后一层。