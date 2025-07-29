
import os
from pathlib import Path
import inspect

this_file_path= inspect.getfile(inspect.currentframe())
this_dirname= os.path.dirname(this_file_path)
this_parent_dirname= Path(this_dirname).parent.absolute()

print(this_file_path)
print(this_dirname)
print(this_parent_dirname)

