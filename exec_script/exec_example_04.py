import ast

def inlineCode(inputFile):
    codeSource= open(inputFile).read()
    code= ast.parse(codeSource)
    compiledCode= compile(code, filename=inputFile, mode='exec')
    return exec(compiledCode)

inlineCode('./deliberate_error.py')

print(testString)
