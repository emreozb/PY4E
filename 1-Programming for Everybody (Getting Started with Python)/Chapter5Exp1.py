### Chapter 5 version
# finding total, counter and average number
counter = 0
total = 0.0
while True:
        sval = input("Enter a number: ")
        if sval == 'done':
            break
        try:
            fval = float(sval)
        except:
            print("Invalid input. Please try again.")
            continue
        # print(fval)
        counter += 1
        total += fval 
        # print('All Done')
print(total, counter, total / counter)

           
### Chapter 8 version
# numbers = list()
# while True:
#     num = input("Enter a number: ") 
#     if num == 'done':
#         break
#     number = float(num)
#     numbers.append(number)
# average = sum(numbers) / len(numbers)
# print(sum(numbers), len(numbers), average)

