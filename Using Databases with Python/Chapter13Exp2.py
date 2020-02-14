from urllib.request import urlopen
import json

# Asking user to input the source URL of the JSON data file
url = input('Enter URL: ')
print('Retrieving:', url)

json_1 = urlopen(url).read()
print('Retrieved', len(json_1), 'characters')

# Transforming the text of the JSON file
json_2 = json.loads(json_1)

num = 0
numlist = list()

for count in json_2['comments']:
    num = int(count['count'])
    numlist.append(num)
print(sum(numlist))
    


