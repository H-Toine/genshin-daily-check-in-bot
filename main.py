#!/usr/bin/env python

import random
import time
import os

cwd = os.getcwd()

randomSleep = random.randint(2,10)

print("Sleeping for: %ds" % randomSleep)

# time.sleep(randomSleep)
print(f"python {cwd}/genshin-os.py")
# os.system(f"python {cwd}/genshin-os.py")
