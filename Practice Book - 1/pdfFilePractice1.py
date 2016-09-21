import os
from PyPDF2 import PdfFileReader

path = "C:/Users/Catrell Washington/Pride"

input_file_name = os.path.join(path, "BibleKJV.pdf")
input_file = PdfFileReader(open(input_file_name, "rb"))

print("Title: " , input_file.getDocumentInfo().title)
print("Number of Pages:  " , input_file.getNumPages())


