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
            if name in item:   
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



# find . -name "*.txt" -print
# find . -name "*.rb" -exec rm {} \;

# -print    os.listdir()
# -name	    os.path.isfile()
# -type	    os.path.isdir()
# -exec	    os.system()