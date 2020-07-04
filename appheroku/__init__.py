import os
import sys
import inspect


dir_list = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe()))).split(os.sep, 10)
for level in range(5):
    sys.path.insert(0, os.sep.join(dir_list[:(len(dir_list))-level]))

from app import application as app
