import os
import main
import time

exec(open('main.py').read())

while True:
    os.system("main.py")
    time.sleep(5)