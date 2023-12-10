def main():
    file = open('input.txt', 'r')
    map = file.read().splitlines()

    startPosition = [83, 25]
    cur1 = Cursor(startPosition,map, "L")
    cur2 = Cursor(startPosition,map, "D")

    total = 1
    while cur1.move() != cur2.move():
        total +=1
    
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