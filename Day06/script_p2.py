def main():
    file = open('input_p2.txt', 'r')
    lines = file.readlines()
    total = 1
    for line in lines:
        t = int(line.split()[0])
        d = int(line.split()[1])
        
        
        firstSuccess = 0
        lastSuccess = 0
        seed = 0
        i = 1
        while i<t:
            if i * (t-i) >d:
                seed = i
                break
            i+=100000
        i = seed
        while True:
            if i * (t-i) <d:
                break
            lastSuccess = i
            i+=1
        i = seed-1
        while True:
            if i * (t-i) <d:
                break
            firstSuccess = i
            i-=1
        total *= (lastSuccess - firstSuccess+1)

    print(total)
main()