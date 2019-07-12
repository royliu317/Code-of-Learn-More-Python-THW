# Below code accomplishs the parameters of sed：
# s / regexp / replacement: Attempt to match regexp against the pattern space
# For example: python sed.py 's/test/SAMPLE/g' file_name （test is the words to be replaced in the file)
# R filename：Append a line read from filename. Each invocation of the command reads a line from the file. This is a GNU extension. Begin a block of commands (end with a ' '). 
# For example: python sed.py 'r in_file_name' file_name （in_file_name will append to file_name）.


import re

def parse_script(script):                        
    if script[0] == "s":                         
        return ('s', script.split('/')[1:3])     
    elif script[0] == "r":                       
        return ('r', script.split(' ')[1:])      
    else:
        print("Error, only s supported")
        sys.exit(1)

def do_s(file_name, pattern, replace):           
    with open(file_name) as f:                   
        for line in f.readlines():               
            fixed = re.sub(pattern, replace, line)
            print(fixed, end="")                   # To save the time, we use re.sub although "re.sub is not on the compiled regular expression"

def do_r(file_name, in_file_name):           
    contents = open(in_file_name).read()
    #print('\n', contents, repr(contents), '\n')

    with open(file_name) as f:
        for line in f.readlines():
            print(line, contents, end='')

def apply_script(command, file_name, args):  
    if command == "s":          
        do_s(file_name, *args)               
    elif command == "r":
        do_r(file_name, *args)
    else:
        print("Not supported.")
        sys.exit(1)

def sed(script, files):                          
    command, args = parse_script(script)        
    for file_name in files:                     
        apply_script(command, file_name, args)  



# str.replace(old, new[, count])
# Return a copy of the string with all occurrences of substring old replaced by new. If the optional argument count is given, only the first count occurrences are replaced.

# re.sub(pattern, repl, string, count=0, flags=0)：
# Return the string obtained by replacing the leftmost non-overlapping occurrences of pattern in string by the replacement repl. 
# If the pattern isn’t found, string is returned unchanged. 
# The "repl" can be a string or a function; if it is a string, any backslash escapes in it are processed. 
# If repl is a function, it is called for every non-overlapping occurrence of pattern. The function takes a single match object argument, and returns the replacement string. 
# The "pattern" may be a string or a pattern object. 
# https://docs.python.org/3/library/re.html#re.sub


# set(): set([iterable])
# Set Type： Its update(*others) function equals to set |= other | ...
# Update the set, adding elements from all others.