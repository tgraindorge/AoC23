import re

def main():
    file = open('input.txt', 'r')
    Lines = file.readlines()

    Total = 0

    cardCopies = list()
    for i in range(len(Lines)):
        cardCopies.append(1)
    lineKey = 0
    for line in Lines:
        winNums = list()
        cardPoints = 0
        cardsInfo = line.split(":")[1]
        for num in re.finditer(r"([0-9]+)(?!:)", cardsInfo.split("|")[0]):
            winNums.append(int(num.group()))
        winNumsCount = 0
        for num in re.finditer(r"([0-9]+)(?!:)", cardsInfo.split("|")[1]):
            if int(num.group()) in winNums:
                winNumsCount += 1
                if cardPoints == 0:
                    cardPoints=1
                else:
                    cardPoints *= 2
                
        for i in range(winNumsCount):
            cardCopies[lineKey + 1 + i] += cardCopies[lineKey]
        Total+=cardPoints
        lineKey += 1
    total_part2 = 0
    for i in range(len(cardCopies)):
        total_part2 += cardCopies[i]
    print("Part 1: " + str(Total))
    print("Part 2: " + str(total_part2))

main()