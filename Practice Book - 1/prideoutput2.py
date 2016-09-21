# This script shows us how to make a portion of a pdf into another pdf
# 1. you must import your os and the PyPDF2 packages
# 2. create a path and variables that designate where the (paths*) may go into
# 3. create a loop that reads in a selected range and copies each page number that is restricted with that range
# 4. create the file that you want to print to and write to it
# 5. close the file

import os
from PyPDF2 import PdfFileReader , PdfFileWriter

path ="C:/Users/Catrell Washington/Pride"

input_file_name = os.path.join(path, "Pride.pdf") 
input_file = PdfFileReader(open(input_file_name, "rb"))
output_PDF = PdfFileWriter()

for page_num in range(1, 4):
    output_PDF.addPage(input_file.getPage(page_num))

output_file_name = os.path.join(path, "portion.pdf")
output_file = open(output_file_name, "wb")
output_PDF.write(output_file)
output_file.close()
