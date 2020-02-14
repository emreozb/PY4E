fname = input("Enter a file name: ") # mbox-short.txt
if len(fname) < 1 : 
    fname = "mbox-short.txt"
fh = open(fname)
counts = dict()
for line in fh:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    if line.startswith('From'):
        words = line.split()
        word_2nd = words[1]
        counts[word_2nd] = counts.get(word_2nd,0) + 1

counter = None  
most_repeater = None
for word_2nd, count in counts.items():
    if counter is None or count > counter:
        most_repeater = word_2nd
        counter = count

print(most_repeater, counter)
