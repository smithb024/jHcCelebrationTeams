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
tolerance = 1

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

# Loop 10 times
for i in range(0,10):
    print(f'Iteration {i}')
    random.shuffle(adults)
    random.shuffle(juniors)
    
    # Loop through each adult
    for adultRow in adults:
        # If the adult has not been used
        if adultRow[2] == False:
            # Create a team and add the adult to it. Note the adult as being used. (Remember the adult)
            teamSuccess = False
            newTeam = [adultRow[0], adultRow[1], "", 0, "", 0]
            adultRow[2] = True

            # Loop through each child
            # If the child has not been used and no child has been added to the team add them and note them as being used. (Remember the child)
            # If the child has not been used and a child has been added.
            # If the sum of the child and the existing team fall with in tolerances, add the child to the team and not them as being used. Save the team. Loop through to the next adult.
            # If the test fails, loop through to the next child.

            # If the team can't be completed, clear the adult and child. Move onto the next adult.

            # If all adults/children have been allocated. Break out of the loop (10).
            # On the 10th loop. Just take any team.




print('Shuffle')
for row in juniors:
    print(f'{row[0]}:{row[1]}:{row[2]}')
