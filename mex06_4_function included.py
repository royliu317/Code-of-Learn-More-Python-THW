from pathlib import Path
import argparse
import sys

# 4. Define the function for --name
def name_parameter(start, args):
    for f in start.rglob(args.name):  
        print(f)

# 5. Define the function for --type
def type_parameter(start, args):
    if args.type not in ['d', 'f']:
        print(f"Unknown type: {args.type}")
        sys.exit(1)
    for f in start.rglob(args.name or '*'):  
        if args.type == "d" and f.is_dir():
            print(f)
        elif args.type == "f" and f.is_file():
            print(f)
        else:
            pass
    
# 3. Define search logic based on the user's input 
def find_files(args):
    start_path = Path(args.start[0])      
    
    if args.name and not args.type:
        name_parameter(start_path, args)
    elif args.type:
        type_parameter(start_path, args)
    else:
        print("You need either --name or --type")
        sys.exit(1)

# 1. Define how argparse receives and parses command line characters, then return the parsed instantiated object
def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('start', type=str, nargs=1)   
    parser.add_argument('--name', type=str)
    parser.add_argument('--type' , type=str)

    return parser.parse_args()

# 2. Define the startpoint of the code
find_files(parse_args())