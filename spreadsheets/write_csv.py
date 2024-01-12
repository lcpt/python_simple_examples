import csv

with open('write_csv.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'age'])
    writer.writerow(['John Doe', 30])
  
