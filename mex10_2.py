# Below code is to sort all content altogether via the user input file path(s) or input the content directly.


import sys

lines = []

if len(sys.argv) > 1:           
    for file_name in sys.argv[1:]:
        lines += [line for line in open(file_name).readlines() if len(line) > 20] 
        # If we need to sort the content in each file （not sort all files altogether），we can use below 2 lines to replace above, and the 3rd line to replace the print() at the bottom
        #output = "".join(sorted(line for line in open(file_name).readlines())) 
        #print(output)
         
else:       
    while True:                       # Use Ctrl+Z (Windows OS) to break the loop
        try:
            line = input() + '\n'     
            lines.append(line)
        except EOFError:
            break

print("".join(sorted(lines)), end="") 



# += is an assignment
# We can't put an assignment inside a function call. e.g. lines.append(line += '\n')  --> Wrong!

# readlines()：fileObject.readlines( )
# join(): str.join(sequence)
# sorted()：sorted(iterable, key=None, reverse=False)  
# reverse = True means desc ， reverse = False (by default) means asc。
