# Below code is NOT to read the file content, but let the user to input and cut

import sys

_, delim, fields = sys.argv
split_at = [int(x) for x in fields.split(',')]  # List comprehensions
#print(split_at, type(split_at[0]))

while True:                                     # Endless loop
    try:
        line = input()
        cuts = line.split(delim)                
        for i in split_at:
            print(f"{cuts[i]} ", end="")
        print()

    except KeyboardInterrupt:                  
        sys.exit(0)
    except IndexError:                         
        pass
