# defining the function to compute weekly payment
def computepay(h, r):
    if h > 40:
        return ( 40 * r) + ((h - 40) * (r*1.5))
    else:
        return (h * r)

try:
    hrs = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    pay = computepay(hrs, rate)
    print(pay)
except:
    print("Error, please enter numeric input")