import Module_1
from imp import reload
import time
print("Going to sleep for 30 sec")
time.sleep(30)
reload(Module_1)
print("I am in test module ..")
