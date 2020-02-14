fname = input("Enter a file name: ")
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
        word_hr = words[5]
        time = word_hr.split(':')
        hrs =  time[0]
        counts[hrs] = counts.get(hrs,0) + 1 

for hrs, count in sorted(counts.items()):
    print(hrs,count)






