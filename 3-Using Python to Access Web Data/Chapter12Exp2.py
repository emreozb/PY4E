import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') # no need for GET command, no need for encode 
for line in fhand:
        print(line.decode().strip())