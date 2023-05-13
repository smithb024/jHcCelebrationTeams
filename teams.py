import csv

with open('adult.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    lineCount = 0
    for row in csvReader:
        print(f'Adult - line is {", ".join(row)}')
        lineCount += 1
    print(f'Processed {lineCount} lines.')

with open('junior.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    lineCount = 0
    for row in csvReader:
        print(f'Junior - line is {", ".join(row)}')
        lineCount += 1
    print(f'Processed {lineCount} lines.')
