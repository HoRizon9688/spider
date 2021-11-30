import time
import random

print("Start : %s" % time.ctime())
time.sleep(random.randint(1, 10))
print("End : %s" % time.ctime())