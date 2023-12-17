def main():
    if __name__ == '__main__':
        with open('input.txt', 'r') as f:
            data = [[[*c] for c in l.splitlines()] for l in [b for b in f.read().split("\n\n")]]
            total = 0
            total_p2 = 0
            for block in data:
                p1_v = getvline(block)
                p1_h = gethline(block)

                total += p1_v + 100 * p1_h
                p2_v = getvline(block,False, p1_v, True)
                if p2_v == 0:
                    p2_h = gethline(block,False, p1_h, True)
                else:
                    p2_h = gethline(block,True, p1_h, True)
                total_p2 += p2_v + 100 * p2_h
            print("Part 1: " + str(total))
            print("Part 2: " + str(total_p2))
            

def getvline(block : [[]], isFixed = False, ignoreLine = 0, part2 = False):
    rotated = [list(elem) for elem in zip(*block[::-1])]
    return gethline (rotated, isFixed, ignoreLine, part2)

def gethline(block : [[]], isFixed = False, ignoreLine = 0, part2 = False):
    i = 1
    mirrorLine = 0
    while i < len(block):
        if i == ignoreLine:
            i +=1
            continue
        maxLinesCheck = min(i, len(block)-i)
        y = 1
        isValid = True
        smudgeFound = False
        while y <= maxLinesCheck:
            if not smudgeFound and not isFixed and part2 and errCount(block[i-y], block[i+y-1]) == 1:
                y +=1
                smudgeFound =True
                continue
            if errCount(block[i-y], block[i+y-1]) != 0:
                isValid = False
                break
            y +=1
        if isValid:
            mirrorLine = i
        i +=1
    return mirrorLine

def errCount(l1 : [], l2 : []) -> int:
    total = 0
    for i, c in enumerate(l1):
        if l2[i] != c:
            total += 1
    return total

if __name__ == "__main__":
    main()