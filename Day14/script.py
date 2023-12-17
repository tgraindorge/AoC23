from functools import lru_cache
def main():
    if __name__ == '__main__':
        with open('input.txt', 'r') as f:
            data = [[*c] for c in f.read().splitlines()]
            data = moveNorth(data)
            print("Part 1: " + str(getResult(data)))
            data = moveSouth(data)
            for i in range(100):
                data = moveNorth(data)
                data = moveWest(data)
                data = moveSouth(data)
                data = moveEast(data)

                print("Part 2: " + str(getResult(data)))
            #for lst in data:
            #    print(*lst)
            #print("///////")

 
def moveSouth(data : [[]]):
    rotated = [list(elem) for elem in zip(*data[::-1])]
    rotated2 = [list(elem) for elem in zip(*rotated[::-1])]
    moveNorth(rotated2)
    rotated3 = [list(elem) for elem in zip(*rotated2[::-1])]
    return [list(elem) for elem in zip(*rotated3[::-1])]

     
def moveWest(data : [[]]):
    rotated = [list(elem) for elem in zip(*data[::-1])]
    moveNorth(rotated)
    rotated2 = [list(elem) for elem in zip(*rotated[::-1])]
    rotated3 = [list(elem) for elem in zip(*rotated2[::-1])]
    return [list(elem) for elem in zip(*rotated3[::-1])]

     
def moveEast(data : [[]]):
    rotated = [list(elem) for elem in zip(*data[::-1])]
    rotated2 = [list(elem) for elem in zip(*rotated[::-1])]
    rotated3 = [list(elem) for elem in zip(*rotated2[::-1])]
    moveNorth(rotated3)
    return [list(elem) for elem in zip(*rotated3[::-1])]

    
def moveNorth(data : []):
    for c in range(len(data[0])):
        for r in range(len(data)):
            if r > 0 and data[r][c] == "O" and data[r-1][c] not in ["O", "#"]:
                i = r - 1
                while i>=0:
                    if((i==0 and data[i][c] == ".") or
                        (i>0 and data[i-1][c] in ["#", "O"])):
                        data[i][c] = "O"
                        data[r][c] = "."
                        break
                    i -= 1
    return data

def getResult(data : []):
    weight = len(data)
    total = 0
    for r in data:
        total += sum(1 for i in r if i== "O") * weight
        weight -= 1
    return total
    
if __name__ == "__main__":
    main()