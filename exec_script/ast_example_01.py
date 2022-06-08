import ast  

code = ast.parse("print('Hello Learner ! Welcome to JavaTpoint')")  
print(code)  

exec(compile(code, filename="", mode="exec"))  
