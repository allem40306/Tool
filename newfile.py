prefix = input('Input prefix: ')
nameMode = int(input('name mode(1:number, 2:alpha): '))
num = int(input('number of files: '))
outputMode = int(input('4-2-1 select(4:.cpp,2:.in,1:.out): '))

filenames = []
if nameMode == 1:
    for i in range(0, num):
        filenames.append(prefix + chr(i + ord('1')))
elif nameMode == 2:
    for i in range(0, num):
        filenames.append(prefix + chr(i + ord('A')))

for filename in filenames:
    if outputMode & 4 != 0:
        open(filename + '.cpp', 'w')
    if outputMode & 2 != 0:
        open(filename + '.in', 'w')
    if outputMode & 1 != 0:
        open(filename + '.out', 'w')
