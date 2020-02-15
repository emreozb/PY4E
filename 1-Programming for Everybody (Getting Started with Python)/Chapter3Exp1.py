# try-except usage
# salary calculator
try:
    h = float(input("Enter Hours: "))
    r = float(input("Enter Rate: "))
    if h <= 40:
        grossPay = (h * r)
        print(grossPay)
    elif h > 40:
        grossPay = ((40 * r) + ((h-40)*(r*1.5)))
        print(grossPay)
except:
    print("Please enter proper numbers")