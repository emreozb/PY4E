from urllib.request import urlopen
import xml.etree.ElementTree as ET 

# Asking user to input the source URL of the XML data file
url = input('Enter URL: ')
print('Retrieving:', url)

xml = urlopen(url).read()
print('Retrieved', len(xml), 'characters')

# Transforming the text of the XML file to a tree
tree = ET.fromstring(xml)

# Finding all the <comment> tags and putting them into a list
counts = tree.findall('.//count')
numlist = list()

# Looping through all the <count> nodes
for count in counts:
    numlist.append(int(count.text))    # Converting the text of the <count> nodes into an integer
print('Count:', len(counts))
print('Sum:', sum(numlist))
