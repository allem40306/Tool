filenames = []
for i in range(1, 17):
    filenames.append(str(i) + '.out')
with open('test.out', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)