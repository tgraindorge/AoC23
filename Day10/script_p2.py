def main():
    file = open('input.txt', 'r')
    map = file.read().splitlines()

    startPosition = [83, 25]
    cur = Cursor(startPosition,map, "L")
    total = 0
    loopTiles = []

    while True:
        tile = cur.move()
        loopTiles.append(tile)
        if tile == startPosition:
            break
        
        
    r = 0
    while r < len(map):
        inLoop = False
        c = 0
        while c < len(map[r]):
            if [r, c] in loopTiles:
                if map[r][c] in ["|","F","7","S"]:
                    inLoop = not inLoop
            else:
                if inLoop: total +=1
            c += 1
        r += 1
    print(total)

class Cursor:
    def __init__(self, _startPos : [int,int], _map : list[str], _nextDirection: str):
        self.position = {"r" : _startPos[0],
                         "c" : _startPos[1]}
        self.map = _map
        self.moveCount = 0
        self.nextDirection = _nextDirection

    def move(self) ->[int,int]:
        match self.nextDirection:
            case "U":
                self.position["r"] -= 1
                match self.map[self.position["r"]][self.position["c"]]:
                    case "7":
                        self.nextDirection = "L"
                    case "F":
                        self.nextDirection = "R"
            case "R":
                self.position["c"] += 1
                match self.map[self.position["r"]][self.position["c"]]:
                    case "7":
                        self.nextDirection = "D"
                    case "J":
                        self.nextDirection = "U"
            case "D":
                self.position["r"] += 1
                match self.map[self.position["r"]][self.position["c"]]:
                    case "L":
                        self.nextDirection = "R"
                    case "J":
                        self.nextDirection = "L"
            case "L":
                self.position["c"] -= 1
                match self.map[self.position["r"]][self.position["c"]]:
                    case "L":
                        self.nextDirection = "U"
                    case "F":
                        self.nextDirection = "D"
        return [self.position["r"],self.position["c"]]


main()