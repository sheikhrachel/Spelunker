import os
import shutil
import time
from fnmatch import fnmatch
import sys

from file_parser import file_reader
from test_maker import destination_matcher, test_generator


root = os.getcwd()
print(root)
pattern = "*.py"

request_files = {}

for path, subdirs, files in os.walk(root):
    for file in files:
        if fnmatch(file, pattern):
            current_file = os.path.join(path, file)
            try:
                k, v = file_reader(current_file)
                request_files[k] = v
            except:
                continue

if len(request_files) is 0:
    sys.exit("No request imports found.")

test_directory = destination_matcher(root)

test_generator(test_directory, request_files)

# python3 ../Spelunker/src/Spelunker.py

# time.sleep(4)
# shutil.rmtree('test')
