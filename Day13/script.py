def main():
    if __name__ == '__main__':
        with open('input.txt', 'r') as f:
            data = [l.splitlines() for l in [b for b in f.read().split("\n\n")]]
            '''
            str_lines = f.read().splitlines()
            data = [[]]
            b = 0
            for l in str_lines:
                if(l==""):
                    data.append([])
                    b += 1
                else:
                    data[b].append([*l])
            '''
            total = 0
            for block in data:
                total += getvline(block)
                total += 100 * gethline(block)
            
            print("total: " + str(total))
            

def getvline(block : [[]]):
    rotated = [list(elem) for elem in zip(*block[::-1])]
    return gethline (rotated)

def gethline(block : [[]]):
    i = 1
    mirrorLine = 0
    
    while i < len(block):
        maxLinesCheck = min(i, len(block)-i)
        y = 1
        isValid = True
        while y <= maxLinesCheck:
            if block[i-y] != block[i+y-1]:
                isValid = False
                break
            y +=1
        if isValid and i > mirrorLine:
            mirrorLine = i
        i +=1
    return mirrorLine

if __name__ == "__main__":
    main()