from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


# Ignoring SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# Asking user to input the URL
url = input('Enter - ')
html = urlopen(url, context=ctx).read()

# Creating an organised string (soup) with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')

numlist = list() 
for tag in tags:
    numlist.append(int(tag.string))

print(sum(numlist))    