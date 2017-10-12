import sys
import traceback
from os import getcwd, listdir
from os.path import join

try:
    listdir(join(getcwd(), "pp"))
except Exception as ex:
    print(ex.args)
    tb = traceback.format_exc()
    print(tb)