from pathlib import Path
from sys import argv

_, start, query = argv

start_path = Path(start)

for f in start_path.rglob(query):  
    print(f)


# pathlib — Object-oriented filesystem paths: https://docs.python.org/3/library/pathlib.html
# Path.rglob(pattern): https://docs.python.org/3/library/pathlib.html#pathlib.Path.rglob
