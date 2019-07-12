# Below code accomplishs the replace functionality via call mex09_2_tools. For example:
# python sed.py 's/test/SAMPLE/g' file_name
# python sed.py 'r in_file_name' file_name

import sys
import mex09_2_tools

script = sys.argv[1]    
files = sys.argv[2:]    
                        

mex09_2_tools.sed(script, files)


# sys.argv
# The list of command line arguments passed to a Python script. sys.argv[0] is the script name. If no script name was passed to the Python interpreter, argv[0] is the empty string.
# https://docs.python.org/3/library/sys.html?highlight=sys%20argv#sys.argv