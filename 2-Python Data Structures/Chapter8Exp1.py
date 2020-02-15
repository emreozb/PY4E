fname = input("Enter file name: ") # romeo.txt or any .txt file
fh = open(fname)
words_list = list()

for line in fh:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if not word in words_list:
            words_list.append(word)

words_list.sort()
print(words_list)
