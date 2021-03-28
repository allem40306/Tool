prefix = input('Input prefix: ')
nameMode = int(input('name mode(1:number, 2:alpha): '))
num = int(input('number of files: '))
ext = input('the extend name: ')

filenames = []
if nameMode == 1:
    for i in range(0, num):
        filenames.append(prefix + chr(i + ord('1')))
elif nameMode == 2:
    for i in range(0, num):
        filenames.append(prefix + chr(i + ord('A')))

for filename in filenames:
        open(filename + '.' + 'txt', 'w')
