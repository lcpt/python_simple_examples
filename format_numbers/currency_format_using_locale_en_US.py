import locale

locale.setlocale(locale.LC_ALL, "en_US")
number = 12345.6789
formatted_number = locale.currency(number, grouping=True)
print(formatted_number) # Output: $12,345.68
