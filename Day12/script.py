import re

debug = True

ValidBlock = re.compile(r"^([#?]+)$")
NoBlock = re.compile(r"^([.?]+)$")

def main():
    with open('input2.txt', 'r') as f:
        data = [[l.split()[0],[int(x) for x in l.split()[1].split(",")]] for l in f.read().splitlines()]
    
    total = 0
    for l in data:
        rowTot = getArrangements(l[0], l[1], 0)
        print(rowTot)
        total += rowTot

    print(total)

def getArrangements(pat : str, blocks : [int], count : int) -> int:
    
    minLength = 0
    for b in blocks:
        minLength += b + 1
    minLength -=1
    bMax = len(pat) - minLength
    if debug: print("------")
    if debug: print("Pat: " + pat)
    if debug: print(blocks)
    if debug: print("bMax: " + str(bMax))
    if debug: print("MinLen: " + str(minLength))
    if bMax == 0 and re.match(ValidBlock, pat[0:blocks[0]]):
        if debug: print(" COUNT ++ - bMax == 0")
        return count + 1
    isLastBlock = len(blocks) == 1
    i = 0
    if debug and isLastBlock: print("is last Block")
    while i<= bMax:

        '''
        validPos = True
        y = 0
        while y < blocks[0]:
            print("checking " + pat[y+i+blocks[0]])
            if pat[y+i] not in ['#', '?'] or ((y+i+blocks[0]) < len(pat) and pat[y+i+blocks[0]] == "#" ):
                validPos = False
                break
            print("valid pos")
            y += 1
        if validPos:
        '''
        #if debug: print("i+blocks[0]): " + pat[i+blocks[0]])
        if debug: print("len(pat): " + str(len(pat)))
        if (re.match(ValidBlock, pat[i:i+blocks[0]]) and # Block placecment OK
                ((i+blocks[0]) == len(pat) or pat[i+blocks[0]] in ["?","."] ) and # End of string OR next char ? or .
                 (i == 0 or pat[i-1] in ["?","."]) # First in string OR prev char ? or .
            ):
            if debug: print("validBlock " + pat[i:i+blocks[0]])
            if isLastBlock:
                if debug: print(pat[i+blocks[0]:])
                if len(pat[i+blocks[0]:])==0 or re.match(NoBlock, pat[i+blocks[0]:]):
                    count += 1
                    if debug: print(" COUNT ++ - last block position VALID")
                else:
                    if debug: print("position INVALID - More block after")
            else:
                if debug: print("i : " + str(i))
                if debug: print("blocks[0] : " + str(blocks[1:][0]))
                count = getArrangements(pat[i+blocks[0]+1:], blocks[1:], count)
        i+=1
    #print(str(bMax))

    return count
main()