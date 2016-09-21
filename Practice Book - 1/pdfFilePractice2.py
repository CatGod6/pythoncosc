import os
from PyPDF2 import PdfFileReader

path = "C:/Users/Catrell Washington/Pride"

input_file_name = os.path.join(path , "BibleKJV.pdf")
input_file = PdfFileReader(open(input_file_name, "rb"))

output_file_name = os.path.join(path, "BibleKJV.txt")
output_file = open(output_file_name, "w")

title = input_file.getDocumentInfo().title
total_pages = input_file.getNumPages()

output_file.write(title + "\n")
output_file.write("Number of Pages: {} \n\n".format(total_pages))

for page_num in range(0,total_pages) :
                           text = input_file.getPage(page_num).extractText()
                           text = text.replace("  ", "\n")
                           output_file.write(text)

output_file.close()
