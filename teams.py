import csv
import random

def OpenFile(filename):
    contents = []
    with open(filename) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        lineCount = 0
        for row in csvReader:
            print(f'OpenFile {filename} - line is {", ".join(row)}')
            time = int(row[2])/60
            time += int(row[1])
            #print(time)
            content = [row[0], time, False]
            contents.append(content)
            lineCount += 1
        print(f'Processed {lineCount} lines.')
    return contents

adults = OpenFile('adult.csv')
juniors = OpenFile('junior.csv')

#with open('adult.csv') as csvFile:
#    csvReader = csv.reader(csvFile, delimiter=',')
#    lineCount = 0
#    for row in csvReader:
#        print(f'Adult - line is {", ".join(row)}')
#        time = int(row[2])/60
#        time += int(row[1])
#        print(time)
#        adult = [row[0], time, False]
#        adults.append(adult)
#        lineCount += 1
#    print(f'Processed {lineCount} lines.')

#with open('junior.csv') as csvFile:
#    csvReader = csv.reader(csvFile, delimiter=',')
#    lineCount = 0
#    for row in csvReader:
#        print(f'Junior - line is {", ".join(row)}')
#        time = int(row[2])/60
#        time += int(row[1])
#        print(time)
#        lineCount += 1
#    print(f'Processed {lineCount} lines.')

for row in adults:
    print(f'{row[0]}:{row[1]}:{row[2]}')
for row in juniors:
    print(f'{row[0]}:{row[1]}:{row[2]}')

random.shuffle(adults)
random.shuffle(juniors)

print('Shuffle')
for row in juniors:
    print(f'{row[0]}:{row[1]}:{row[2]}')
