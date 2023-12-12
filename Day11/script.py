import re

def main():

    with open('input.txt', 'r') as f:
        map = [[c for c in [*line] if c !='\n'] for line in f]

    print("Part 1: " + str(getDistance(map, 2)))
    print("Part 2: " + str(getDistance(map, 1000000)))


def getDistance(matrix : [[str]], expTime: int) -> int:
    points = getPoints(matrix)
    emptyRows = getEmptyRows(matrix)
    emptyCols = getEmptyCols(matrix)
    total = 0
    z = 0
    for i, p in enumerate(points):
        z=i
        while z < len(points):
            z+=1
            if(z<len(points)):
                total += abs(p[0] - points[z][0]) + (countInRange(p[0], points[z][0], emptyCols) * (expTime-1))
                total += abs(p[1] - points[z][1]) + (countInRange(p[1], points[z][1], emptyRows) * (expTime-1))
    return total

def getEmptyRows(matrix : [[str]])  -> [int]:
    emptyRows = []
    blankLine = ['.'] * len(matrix[0])
    for i, l in enumerate(matrix):
        if l == blankLine:
            emptyRows.append(i)
    return emptyRows

def getEmptyCols(matrix : [[str]])  -> [int]:
    emptycols = []
    blankCol = [True] * len(matrix[0])
    for l in matrix:
        for i,c in enumerate(l):
            if c !=".":
                blankCol[i] = False
    for i, r in enumerate(blankCol):
        if r: emptycols.append(i)
    return emptycols


def countInRange(x: int, y: int, nums : [int]) -> int:
    start = x
    end = y
    if x > y:
        start = y
        end = x
    total = 0
    for n in nums:
        if n > start and n < end: total +=1
    return total

def getPoints(matrix : [[str]]) -> [int,int]:
    points = []
    for y, l in enumerate(matrix):
        for x, c in enumerate(l):
            if c == "#":
                points.append([x, y])
    return points
main()