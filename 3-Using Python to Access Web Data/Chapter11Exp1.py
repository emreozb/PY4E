# Importing the regex library
import re

# Asking user to enter the source file
fh  = open('regex_sum_279651.txt')
numlist = list()
for line in fh:   # Reading file line-by-line
    numbers = re.findall('[0-9]+', line)  # Finding all the numbers as strings into listOfNums
    for num in numbers: # Looping through the list numbers found
        num = int(num) 
        numlist.append(num) # Adding the numbers into the list

print(len(numlist)) # Printing length of the list
print(sum(numlist)) # Printing sum of the numbers in the list
