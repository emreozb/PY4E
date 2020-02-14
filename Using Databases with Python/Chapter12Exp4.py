import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


# Ignoring SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Asking user to input the URL
url = input('Enter - ')

 # Reading the whole fine into a single long string
html = urllib.request.urlopen(url, context=ctx).read()

# Creating an organised string (soup) with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Retrieving all of the 'a' tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
