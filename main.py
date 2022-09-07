#!/usr/bin/env python

import random
import time
import os



randomSleep = random.randint(2,10)
time.sleep(randomSleep)

directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(directory)
os.system(f"python {directory}/genshin-os.py")
