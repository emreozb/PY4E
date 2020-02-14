fname = input('Enter a file name: ') # mbox-short.txt
fhand = open(fname)
counter = 0
total = 0
for line in fhand:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    spam_pos = line.find('0')
    spam_conf = line[spam_pos : ]
    fspam_conf = float(spam_conf)
    total += fspam_conf
    counter += 1
print('Average spam confidence:', total / counter)