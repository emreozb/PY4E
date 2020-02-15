### Chapter 5 version
# finding the maximum and minimum numbers
largest = None
smallest = None

while True:
    num = input("Enter a number: ") 
    if num == 'done':
        break
    try:
        number = int(num)
    except:
        print("Invalid input")
        continue
    
    if smallest is None:
        smallest = number
    elif number < smallest:
        smallest = number
    elif largest is None:
        largest = number
    elif number > largest:
        largest = number

print('Maximum is', largest)
print('Minimum is', smallest)


### Chapter 8 version
# numbers = list()
# while True:
#     num = input("Enter a number: ") 
#     if num == 'done':
#         break
#     number = float(num)
#     numbers.append(number)
# print(numbers)
# print('Maximum is', max(numbers))
# print('Minimum is', min(numbers))

    

