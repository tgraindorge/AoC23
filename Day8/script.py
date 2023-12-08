import re
import math

debug = False

def main():
    file = open('input.txt', 'r')
    Lines = file.readlines()
    Map = {}
    Directions = []

    lineNumber = 1
    for line in Lines:
        if lineNumber == 1:
           for dir in line:
               if dir == "L": Directions.append(0)
               if dir == "R": Directions.append(1)

               
        if lineNumber > 2:
            Map[re.search(r"^([A-Z]{3})",line).group(1)] = [re.search(r"\(([A-Z]{3})",line).group(1), re.search(r"([A-Z]{3})\)",line).group(1)]
        lineNumber += 1

    curPosition = "AAA"
    dirCursor = 0
    total = 0
    while curPosition != "ZZZ":
        if debug: print(curPosition + " / dir: " + str(Directions[dirCursor]) )
        curPosition = Map[curPosition][Directions[dirCursor]]
        total +=1
        if dirCursor < (len(Directions)-1):
            dirCursor +=1
        else:
            dirCursor = 0
    

    print("Total: " + str(total))
    

main()