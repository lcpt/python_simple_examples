from PyPDF2 import PdfFileReader
  
# creating a pdf reader object
reader = PdfFileReader('lorem-ipsum.pdf')
  
# printing number of pages in pdf file
print('Number of pages: ', len(reader.pages))
  
# getting a specific page from the pdf file
for i, page in enumerate(reader.pages):
  # extracting text from page
  text = page.extractText()
  print("page ", i, " text: '",text,"'")
