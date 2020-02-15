import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignoring SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urllist = list()

# Asking user to input the URL
url = input("Enter URL: ")

# Converting the inputs
counter =int(input("Enter count: "))
pos = int(input("Enter position: "))

for i in range(counter):   # Looping through the layers of webpages 4 times
    print("Retrieving:",url)
    html = urllib.request.urlopen(url, context=ctx).read()     # Reading the whole fine into a single long string
    soup=BeautifulSoup(html, 'html.parser')     # Creating an organised string (soup) with BeautifulSoup
    tags = soup('a')       # Retrieving all of the 'a' tags
    for tag in tags:
        urllist.append(tag)   
    url = urllist[pos-1].get('href', None)   # Updating the URL for the next loop
    del urllist[:]

print("Retrieving:",url)