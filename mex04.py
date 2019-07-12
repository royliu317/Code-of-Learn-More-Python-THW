import argparse
parser = argparse.ArgumentParser()
parser.add_argument('integers', metavar='N', type=int, nargs='+') #Positional argument 
parser.add_argument('-f', '--foo', help='foo help')               #Optional arguments that are options, meaning they do take an argument and set a variable in the script to that option. 
parser.add_argument('-b', '--bar', help='bar help')               #Optional arguments that are options, meaning they do take an argument and set a variable in the script to that option. 
parser.add_argument('-z', '--baz', help='baz help')               #Optional arguments that are options, meaning they do take an argument and set a variable in the script to that option. 
parser.add_argument('-t', '--turn-on', action='store_true')       #Optional arguments that are flags, meaning they don't take an extra argument but simply putting them on the command line turns something on.
parser.add_argument('-x', '--exclude', action='store_false')      #Optional arguments that are flags, meaning they don't take an extra argument but simply putting them on the command line turns something on.
parser.add_argument('-s', '--start', action='store_true')         #Optional arguments that are flags, meaning they don't take an extra argument but simply putting them on the command line turns something on.
args = parser.parse_args()
print(args)
print(vars(args))

# Argparse Tutorial: https://docs.python.org/3/howto/argparse.html#id1
# argparse — Parser for command-line options, arguments and sub-commands: https://docs.python.org/3/library/argparse.html