import logging
from datetime import datetime
from os import getcwd, listdir
from os.path import join


filename = join("example.log")

logging.basicConfig(filename=filename, level=logging.DEBUG)


logging.debug("at p 1")

logging.error("its error")

logging.debug("at p 1")

logging.error("its error")

if "example.log" in listdir(getcwd()):
    print("Yes")


d = datetime.now().isoformat(timespec="seconds")
logging.info(d)