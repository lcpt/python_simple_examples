# Use a temporary directory with temporary files inside.

import tempfile

with tempfile.TemporaryDirectory() as temp_dir:
    with tempfile.NamedTemporaryFile(mode='w', dir= temp_dir, suffix= '.tex', delete= False) as fd1:
        fd1.write('test1')
        print(fd1.name)
    with tempfile.NamedTemporaryFile(mode='w', dir= temp_dir, suffix= '.eps', delete= False) as fd2:
        fd2.write('test2')
        print(fd2.name)


        
        
