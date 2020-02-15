# salary calculator with overtime 
hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

print(h,r)

if h <= 40:
    grossPay = (h * r)
    print(grossPay)
else:
    grossPay = ((40 * r) + ((h-40)*(r*1.5)))
    print(grossPay)