import re
file = open('input.txt', 'r')
Lines = file.readlines()

firstPattern = re.compile(r"^[a-z]*([1-9])")
lastPattern = re.compile(r"([1-9])[a-z]*$")

word2nums = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

totalPart1 = 0
totalPart2 = 0
for line in Lines:
    totalPart1 += int(re.search(firstPattern,line).group(1) + re.search(lastPattern,line).group(1))
    for k, v in word2nums.items():
        line = line.replace(k, k+v+k)
    totalPart2 += int(re.search(firstPattern,line).group(1) + re.search(lastPattern,line).group(1))

print("total Part 1 : " + str(totalPart1))
print("total Part 2 : " + str(totalPart2))