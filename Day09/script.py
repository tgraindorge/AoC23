def main():
    file = open('input.txt', 'r')
    str_lines = file.read().splitlines()
    dataLines = []

    total = 0
    for l in str_lines:
        dataLines.append([])
        dataLine = [int(n) for n in l.split()]
        dataLines[len(dataLines)-1].append(dataLine)
        
        cursor = 0
        while True:
            
            dataLines[len(dataLines)-1].append([])
            
            nonZeroItems = 0
            i = 0
            while i < len(dataLine)-cursor-1:
                diff = dataLines[len(dataLines)-1][cursor][i+1] - dataLines[len(dataLines)-1][cursor][i]
                
                dataLines[len(dataLines)-1][cursor+1].append(diff)
                
                if(diff !=0):
                    nonZeroItems += 1
                i += 1
            cursor +=1
            if nonZeroItems == 0: 
                cursor = 0
                break
            
    for block in dataLines:
        i = len(block)-2
        block[i+1].append(0)
        while i>0:
            i -= 1
            val = block[i+1][-1] + block[i][-1]
            block[i].append(val)
            if i == 0:
                total += val

    print ("Total: " + str(total))
main()