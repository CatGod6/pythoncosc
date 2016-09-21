# You might run across a problem where the tar file is not in the same directory as the file you're looking for
# The fix is simple
# 1. open cmd prompt and make sure you saved the file in "C:/ users"
# 2. Then search for the folder it is saved under in that directory
# 3. Use the command "dir" to get the name of the said folders
# 4. run the setup.py file by saying "setup.py install"
# 5. You're done!!

import os
from PyPDF2 import PdfFileReader

path ="C:/Users/Catrell Washington/Pride"

input_file_name = os.path.join(path, "Pride.pdf")
input_file = PdfFileReader(open(input_file_name, "rb"))

print("Number of pages: ", input_file.getNumPages())
print("Title:", input_file.getDocumentInfo().title)

#This command gets the very first page of the PDF file 
print("Fist page " , input_file.getPage(0).extractText())
