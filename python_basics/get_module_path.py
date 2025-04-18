
import inspect
import os
os_path =inspect.getfile(os)
os_dirname= os.path.dirname(os_path)

this_path= inspect.getfile(inspect.currentframe())
this_dirname= os.path.dirname(this_path)

print(os_path)
print(os_dirname)

print(this_path)
print(this_dirname)

