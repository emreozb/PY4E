# usage of elif
score = input("Enter Score: ")

try:
    s = float(score)
    if 1.0 >= s >= 0.9:
        print(s, 'A')
    elif 0.9 >= s >= 0.8:
        print(s, 'B')
    elif 0.8 >= s >= 0.7:
        print(s, 'C')
    elif 0.7 >= s >= 0.6:
        print(s, 'D')
    elif 0.0 <= s <= 0.5:
        print(s, 'F')
    elif s > 1.0:
        print("Out of range!")
except:
    print("Please enter a score between 0.0 and 1.0!")
