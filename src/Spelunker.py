import os
import shutil
import time
from fnmatch import fnmatch

from mock_generator import file_reader

root = os.getcwd()
pattern = "*.py"

try:
    os.mkdir('test')
except Exception as e:
    pass

for path, subdirs, files in os.walk(root):
    for file in files:
        if fnmatch(file, pattern):
            current_file = os.path.join(path, file)
            print(current_file)
            file_reader(current_file)

# python3 ../Spelunker/src/Spelunker.py 
print("current directory: ", root)

time.sleep(2)
shutil.rmtree('test')