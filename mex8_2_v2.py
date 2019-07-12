# Below code uses Python's generator

import sys

_, delim, fields = sys.argv                    # fields type: str（eg. 2）
split_at = [int(x) for x in fields.split(',')] # split_at type: list（eg. [2]）

def lines_of_input():
    try:
        while True:
            yield input()                      # generator
    except KeyboardInterrupt:
            return        
            #raise StopIteration


try:                                            # Set try...except to capture IndexError: list index out of range
    split_lines = (line.split(delim) for line in lines_of_input()) 
    print("1. split_lines: ", split_lines)

    cuts = (line[split_at[0]] for line in split_lines)
    print("2. cuts: ", cuts)

    
    for cut in cuts:
        print(cut)

    
except IndexError:  
        pass


# Python join(): str.join(sequence)
