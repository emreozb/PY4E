text = "X-DSPAM-Confidence:    0.8475"
number_pos = text.find('0')
num = float(text[number_pos:])
print(num)
print(type(num))