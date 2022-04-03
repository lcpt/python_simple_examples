from tabulate import tabulate

dict1 = [["#", "Gender", "age"], ["Alice", "F", 24], ["Bob", "M", 19]]

print('\nASCII output:')
print(tabulate(dict1, headers="firstrow"))

# Latex output
print('\nLaTeX output:')
print(tabulate(dict1, headers='firstrow', tablefmt='latex'))

