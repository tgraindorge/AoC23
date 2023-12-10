import re

debug = False

def main():
    file = open('input.txt', 'r')
    Lines = file.readlines()

    Total = 0
    currLineNum = 0
    prevLineNumbers = None
    curLineNumbers = None
    nextLineNumbers = None
    
    for line in Lines:
        if currLineNum == 0:
            # First Line
            curLineNumbers = getNumbersFromLine(line)
            if currLineNum < len(Lines):
                nextLineNumbers = getNumbersFromLine(Lines[currLineNum+1])
        else:
            prevLineNumbers = curLineNumbers
            curLineNumbers = nextLineNumbers
            if currLineNum < len(Lines)-1:
                nextLineNumbers = getNumbersFromLine(Lines[currLineNum+1])
            else:
                #last line
                nextLineNumbers = None

        for star in re.finditer(r"(\*)", line):
            gearRatio = 0
            gears = list()
            if debug : print("checking " + star.group() + " @ line " + str(currLineNum) + ":" + str(star.start()) + ">" + str(star.end()))
            contatNumList = list()
            contatNumList += curLineNumbers
            if prevLineNumbers != None:
                contatNumList += prevLineNumbers
            if nextLineNumbers != None:
                contatNumList += nextLineNumbers
            for num in contatNumList:
                if isGear(num, star):
                    if debug : print(num.group() + " is a gear")
                    gears.append(int(num.group()))
            if len(gears)==2:
                Total+=gears[0]*gears[1]
        currLineNum += 1
    print(Total)


def getNumbersFromLine(line: str) ->list:
    numbers = list()
    for num in re.finditer(r"([0-9]+)", line):
        numbers.append(num)
    return numbers

def isGear(num : re.Match , star : re.Match) -> bool:
    if debug : print("checking gear " + num.group() + " : " + str(num.start()) + ">" + str(num.end()))
    return star.start() == num.end() or star.end() == num.start() or (num.end() >= star.end() and num.start() <= star.start())

