from PyPDF2 import PdfFileReader
import mechanicalsoup
from time import sleep
import scipy

my_browser = mechanicalsoup.Browser()

for i in range(0,3) :
    page = my_browser.get("https://finance.yahoo.com/q?s=yahoo")
    html_text = page.soup
    
    my_tags = html_text.select("#yfs_l84_yhoo")
    
    my_price = my_tags[0].text
    
    print("The current price of YAHOO is : {}".format(my_price))
    if i < 2 :
        sleep(60)
