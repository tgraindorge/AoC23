import re

debug = False

def main():
    file = open('input.txt', 'r')
    Lines = file.readlines()

    Total = 0
    currLineNum = 0
    for line in Lines:
        if currLineNum == 0:
            prevLine = None
        else:
            prevLine = Lines[currLineNum-1]
        if currLineNum+1 == len(Lines):
            nextLine = None
        else:
            nextLine = Lines[currLineNum+1]

        for match in re.finditer("([0-9]+)", line):
            if debug : print("checking " + match.group())
            if isValidNumber(match.start(), (match.end() - match.start()), prevLine, line, nextLine):
                Total += int(match.group())
                if debug : print("  >> " + match.group() + " is valid")
        currLineNum += 1
    print(Total)




def symbolPresent(data : str, startPosition : int, length: int) ->bool:
    overflow = startPosition + length - (len(data)-1)
    correctedLength = length
    if overflow > 0:
        correctedLength -= overflow
    if startPosition < 0:
        startPosition = 0
        correctedLength = length - 1
    if debug : print("StartPosition: " + str(startPosition) + " - length: " + str(length) + " - corrected length: " + str(correctedLength) + " - overflow: " + str(overflow))
    if re.search(r"^.{" + str(startPosition) + "}(?![.0-9]{" + str(correctedLength) + "})",data):
        return True
    else:
        return False

def isValidNumber(startPosition : int, length: int, prevLine: str, curLine : str, nextLine : str) ->bool:
    if prevLine and symbolPresent(prevLine, startPosition-1, length+2):
        if debug : print("++ Prev Line")
        return True
    if startPosition > 0 and symbolPresent(curLine, startPosition-1, 1):
        if debug : print("++ before")
        return True
    if (startPosition+length) < (len(curLine)-1) and symbolPresent(curLine, startPosition+length, 1):
        if debug : print("++ after")
        return True
    if nextLine and symbolPresent(nextLine, startPosition-1, length+2):
        if debug : print("++ Next Line")
        return True
    return False

    
main()