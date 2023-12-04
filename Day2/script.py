import re
file = open('input.txt', 'r')
Lines = file.readlines()

maxRED = 12
maxGREEN = 13
maxBLUE = 14
GameIDPattern = re.compile(r"^Game ([0-9]+)")
redPattern = re.compile(r"([0-9]+) red")
greenPattern = re.compile(r"([0-9]+) green")
bluePattern = re.compile(r"([0-9]+) blue")

totalPart1 = 0
totalPart2 = 0

for line in Lines:
    gameMaxRED = 0
    gameMaxGREEN = 0
    gameMaxBLUE = 0
    gameID = int(re.search(GameIDPattern,line).group(1))
    gameData = line.split(":",1)[1]
    for gameSet in gameData.split(";"):
        redCount = re.search(redPattern, gameSet)
        greenCount = re.search(greenPattern, gameSet)
        blueCount = re.search(bluePattern, gameSet)
        if redCount and int(redCount.group(1)) > gameMaxRED:
            gameMaxRED = int(redCount.group(1))
        if greenCount and int(greenCount.group(1)) > gameMaxGREEN:
            gameMaxGREEN = int(greenCount.group(1))
        if blueCount and int(blueCount.group(1)) > gameMaxBLUE:
            gameMaxBLUE = int(blueCount.group(1))
    
    if gameMaxRED <= maxRED and gameMaxGREEN <= maxGREEN and gameMaxBLUE <= maxBLUE:
        totalPart1 += gameID

    if(gameMaxRED == 0):
        gameMaxRED = 1
    if(gameMaxGREEN == 0):
        gameMaxGREEN = 1
    if(gameMaxBLUE == 0):
        gameMaxBLUE = 1
    totalPart2 += gameMaxRED * gameMaxGREEN * gameMaxBLUE


print("total Part 1 : " + str(totalPart1))
print("total Part 2 : " + str(totalPart2))