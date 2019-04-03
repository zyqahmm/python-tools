#!/usr/bin/python

import os
import time

pid = os.fork()

if pid:
    time.sleep(60)
else:
    time.sleep(3)
