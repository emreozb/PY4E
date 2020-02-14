fname = input("Enter file name: ") # mbox-short.txt
fh = open(fname)
counter = 0
    
for line in fh:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    if line.startswith('From'):
        counter += 1  
    words = line.split()
    print(words[1])

