import os
import time

from utils import count_down, zone

while True:
    os.system("clear")
    print("{} Days {} Hours {} Minutes and {} Seconds".format(*count_down(zone)))
    time.sleep(1)
    os.system("clear")
