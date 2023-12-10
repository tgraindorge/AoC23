def main():
    file = open('input.txt', 'r')
    lines = file.readlines()
    total = 1
    for line in lines:
        t = int(line.split()[0])
        d = int(line.split()[1])
        
        i = 1
        successCount = 0
        while i<t:
            if i * (t-i) >d:
                successCount +=1
            i+=1
        total *= successCount

    print(total)
main()