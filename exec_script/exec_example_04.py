import ast
from pathlib import Path

def inlineCode(inputFile):
    fullPath= Path(inputFile).resolve()
    codeSource= open(inputFile).read()
    code= ast.parse(codeSource)
    compiledCode= compile(code, filename=str(fullPath), mode='exec')
    return exec(compiledCode)

inlineCode('./deliberate_error.py')

print(testString)
