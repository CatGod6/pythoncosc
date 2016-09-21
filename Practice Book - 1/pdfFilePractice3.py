import os
from PyPDF2 import PdfFileReader , PdfFileWriter

path = "C:/Users/Catrell Washington/Pride"

input_file_name = os.path.join(path, "BibleKJV.pdf")
input_file = PdfFileReader(open(input_file_name , "rb"))

output_PDF = PdfFileWriter()

total_pages = input_file.getNumPages()

for page_num in range(1,total_pages) :
    output_PDF.addPage(input_file.getPage(page_num))

output_file_name = os.path.join(path, "BibleKJV.pdf")
output_file = open(output_file_name , "wb")
output_PDF.write(output_file)

output_file.close()
