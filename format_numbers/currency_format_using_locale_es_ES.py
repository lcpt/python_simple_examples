import locale

locale.setlocale(locale.LC_ALL, "es_ES.utf8")
number = 12345.6789
formatted_number = locale.currency(number, grouping=True)
print(formatted_number) # Output: $12,345.68
