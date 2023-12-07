import re

debug = False

def main():
    file = open('input.txt', 'r')
    Lines = file.readlines()

    Total = 0
    for line in Lines:
        winNums = list()
        myNums = list()
        cardPoints = 0
        cardsInfo = line.split(":")[1]
        for num in re.finditer(r"([0-9]+)(?!:)", cardsInfo.split("|")[0]):
            winNums.append(int(num.group()))
        for num in re.finditer(r"([0-9]+)(?!:)", cardsInfo.split("|")[1]):
            if int(num.group()) in winNums:
                if debug : print("win Num: " + num.group())
                if cardPoints == 0:
                    cardPoints=1
                else:
                    cardPoints *= 2
        Total+=cardPoints
    print(Total)

main()