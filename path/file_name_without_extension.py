from pathlib import Path

testPath= '/root/dir/sub/file_name_to_extract.ext'
fileName= Path(testPath).stem

print('test path: ', testPath)
print('file name without extension: ', fileName)
