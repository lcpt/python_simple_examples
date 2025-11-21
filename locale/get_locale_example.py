import locale

loc= locale.getlocale()
lang_id= loc[0][:2].lower()
print('locale: ', loc)
print('language id: ', lang_id)
number = 12345.6789
formatted_number = locale.format_string('%10.2f', number, grouping=True)
print(formatted_number) # Output: 12.345,68
