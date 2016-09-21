import re
from urllib.request import urlopen

my_address = "https://realpython.com/practice/dionysus.html"
html_page = urlopen(my_address)

html_text = html_page.read().decode('utf-8')

print (html_text) 
