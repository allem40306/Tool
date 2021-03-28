n = int(input('number of files: ')) + 1
ext = input('the extend name: ')
filenames = []

for i in range(1, n):
    filenames.append(str(i) + '.' + ext)
with open('test.'+ ext, 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)