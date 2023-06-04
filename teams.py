import csv
import random
import math

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

# Work out working values
totalTime = 0
totalAthletes = len(adults) + len(juniors) 
for row in adults:
    totalTime += row[1]
for row in juniors:
    totalTime += row[1]
averageTime = totalTime/totalAthletes
expectedTeamTime = averageTime * 3
print(f'TotalTime:{totalTime}')
print(f'TotalAthletes:{totalAthletes}')
print(f'AverageTime:{averageTime}')
print(f'ExpectedTeamTime:{expectedTeamTime}')

# Return to minutes and seconds.
totalMinutes = math.floor(expectedTeamTime)
totalSeconds =  round((expectedTeamTime - totalMinutes) * 60)
print(f'Expected Team Time: {totalMinutes}Minutes, {totalSeconds}Seconds')

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
completedTeams = []

# Loop 10 times
for i in range(0,1):
    print(f'Iteration {i}')
    random.shuffle(adults)
    random.shuffle(juniors)
    
    # Loop through each adult
    for adultRow in adults:
        #print(f'Analysing {adultRow[0]}')
        # If the adult has not been used
        if adultRow[2] == False:
            # Create a team and add the adult to it. Note the adult as being used. (Remember the adult)
            teamSuccess = False
            newTeam = [adultRow[0], adultRow[1], "", 0, "", 0]
            adultRow[2] = True

            # Loop through each junior
            for junior1Row in juniors:
                #print(f'(1) Analysing {junior1Row[0]}')

                if junior1Row[2] == True:
                    #print(f'Already assigned, move on')
                    continue
                # If the child has not been used and no child has been added to the team add them and note them as being used. (Remember the child)
                if junior1Row[2] == False:
                    newTeam[2] = junior1Row[0]
                    newTeam[3] = junior1Row[1]
                    junior1Row[2] = True
                    
                    # Loop through each junior again to get the second child.
                    for junior2Row in juniors:
                        #print(f'(2) Analysing {junior2Row[0]}')
                        # If the sum of the child and the existing team fall with in tolerances, add the child to the team and not them as being used. Save the team. Loop through to the next adult.
                        if junior2Row[2] == False:
                            proposedTime = newTeam[1] + newTeam[3] + junior2Row[1]
                            #print(f'Proposed Team Time with {newTeam[0]}-{newTeam[2]}-{junior2Row[0]} is {proposedTime}')
                            if proposedTime < expectedTeamTime + tolerance and proposedTime > expectedTeamTime - tolerance:
                                newTeam[4] = junior2Row[0]
                                newTeam[5] = junior2Row[1]
                                junior2Row[2] = True
                                teamSuccess = True
                                completedTeams.append(newTeam)
                                print(f'Found Team Time with {newTeam[0]}-{newTeam[2]}-{junior2Row[0]} is {proposedTime}')
                                break

                if teamSuccess == True:
                    break
                else:
                    #print(f'Reset {junior1Row[0]}')
                    junior1Row[2] = False
        if teamSuccess == True:
            # Assign team to array
            print('Success')
        else:
            adultRow[2] = False
                        # If the test fails, loop through to the next child.

                        # If the team can't be completed, clear the adult and child. Move onto the next adult.

                        # If all adults/children have been allocated. Break out of the loop (10).
                        # On the 10th loop. Just take any team.


print(f'Number of completed teams {len(completedTeams)}')
for team in completedTeams:
    print(f'{team[0]}:{team[1]}:{team[2]}:{team[3]}:{team[4]}:{team[5]}')

#print('Shuffle')
#for row in juniors:
    #print(f'{row[0]}:{row[1]}:{row[2]}')
