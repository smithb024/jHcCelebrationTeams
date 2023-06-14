import csv
import random
import math

# Open the named file and return the contents.
def OpenFile(filename):
    contents = []
    with open(filename) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        lineCount = 0
        for row in csvReader:
            print(f'OpenFile {filename} - line is {", ".join(row)}')
            time = int(row[2])/60
            time += int(row[1])
            content = [row[0], time, False]
            contents.append(content)
            lineCount += 1
        print(f'Processed {lineCount} lines.')
    return contents

# Open the files.
adults = OpenFile('adult.csv')
juniors = OpenFile('junior.csv')

# The tolerance is gradually increased, to help find the most even teams.
tolerance = 0

# Record of teams
completedTeams = []

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

# Print file contents for consistency checking
for row in adults:
    print(f'{row[0]}:{row[1]}:{row[2]}')
for row in juniors:
    print(f'{row[0]}:{row[1]}:{row[2]}')

# Work out the teams.
running = True
iteration = 0;
while running == True:
    iteration += 1
    print(f'Iteration {iteration}')
    tolerance += 0.1
    random.shuffle(adults)
    random.shuffle(juniors)
    
    # Loop through each adult
    for adultRow in adults:
        #Already assigned, move on.
        if adultRow[2] == True:
            continue

        # If the adult has not been used
        if adultRow[2] == False:
            # Create a team and add the adult to it. Note the adult as being used. (Remember the adult)
            teamSuccess = False
            newTeam = [adultRow[0], adultRow[1], "", 0, "", 0]
            adultRow[2] = True

            # Loop through each junior
            for junior1Row in juniors:
                #Already assigned, move on.
                if junior1Row[2] == True:
                    continue

                # If the child has not been used and no child has been added to the team add them and note them as being used. (Remember the child)
                if junior1Row[2] == False:
                    newTeam[2] = junior1Row[0]
                    newTeam[3] = junior1Row[1]
                    junior1Row[2] = True
                    
                    # Loop through each junior again to get the second child.
                    for junior2Row in juniors:
                        #Only look at juniors not in a team.
                        if junior2Row[2] == False:
                            #If the proposed time is within tolerances, record a successful team.
                            proposedTime = newTeam[1] + newTeam[3] + junior2Row[1]
                            if proposedTime < expectedTeamTime + tolerance and proposedTime > expectedTeamTime - tolerance:
                                newTeam[4] = junior2Row[0]
                                newTeam[5] = junior2Row[1]
                                junior2Row[2] = True
                                teamSuccess = True

                                totalMinutes = math.floor(proposedTime)
                                totalSeconds =  round((proposedTime - totalMinutes) * 60)

                                completedTeam = [newTeam[0], newTeam[2], newTeam[4], totalMinutes, totalSeconds]
                                completedTeams.append(completedTeam)
                                print(f'Found Team Time with {newTeam[0]}-{newTeam[2]}-{junior2Row[0]} is {proposedTime}')
                                break

                # If the team is successful break out of the loop, otherwise release the junior.
                if teamSuccess == True:
                    break
                else:
                    #print(f'Reset {junior1Row[0]}')
                    junior1Row[2] = False
                    
        # Team not successful release the adult.                
        if teamSuccess == False:
            adultRow[2] = False

    # If all the teams have been found (one per adult), complete successfully.
    print(f'Number of completed teams {len(completedTeams)}')
    if (len(completedTeams) == len(adults)):
        print('SUCCESS: All teams generated')
        running = False
    # Fail if all the teams can't be found in 100 loops.
    if (iteration == 100):
        print('ERROR: Failed to complete. One or more teams have not been generated')
        running = False
        
# Output all teams.
print('Output completed teams')
for team in completedTeams:
    print(f'{team[0]}:{team[1]}:{team[2]}:{team[3]}:{team[4]}')
with open('teams.csv', 'w', encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(completedTeams)
