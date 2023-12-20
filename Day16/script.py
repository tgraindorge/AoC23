def main():
    with open('input.txt', 'r') as f:
        board = Contraption([[*c] for c in f.read().splitlines()])
        board.launch()
        print("Part 1: " + str(len(board.tilesValid)))
        


class Beam:
    def __init__(self, _x, _y, _dir) -> None:
        self.x = _x
        self.y = _y
        self.dir = _dir
        self.active = True




class Contraption:
    def __init__(self, _data) -> None:
        self.data = _data
        self.tilesValid = []
        self.tilesDir = []
        self.beams = []
        self.activeBeams = 1

        self.maxStep = int((len(_data) * len(_data[0])))


    def launch(self):
        self.beams.append(Beam(-1, 0, "R"))
        while self.activeBeams > 0:
            for b in self.beams:
                if(b.active):
                    self.moveBeam(b)


    def moveBeam(self, b : Beam):
        

        match b.dir:
            case "R":
                if b.x < len(self.data[b.y])-1:
                    b.x += 1
                    match self.data[b.y][b.x]:
                        case "|":
                            b.dir = "D"
                            self.beams.append(Beam(b.x, b.y, "U"))
                            self.activeBeams += 1
                        case "\\":
                            b.dir = "D"
                        case "/":
                            b.dir = "U"
                else:
                    b.active = False
                    self.activeBeams -= 1
                    return
            case "L":
                if b.x > 0:
                    b.x -= 1
                    match self.data[b.y][b.x]:
                        case "|":
                            b.dir = "D"
                            self.beams.append(Beam(b.x, b.y, "U"))
                            self.activeBeams += 1
                        case "\\":
                            b.dir = "U"
                        case "/":
                            b.dir = "D"
                else:
                    b.active = False
                    self.activeBeams -= 1
                    return
            case "U":
                if b.y > 0:
                    b.y -= 1
                    match self.data[b.y][b.x]:
                        case "-":
                            b.dir = "L"
                            self.beams.append(Beam(b.x, b.y, "R"))
                            self.activeBeams += 1
                        case "\\":
                            b.dir = "L"
                        case "/":
                            b.dir = "R"
                else:
                    b.active = False
                    self.activeBeams -= 1
                    return
            case "D":
                if b.y < len(self.data)-1:
                    b.y += 1
                    match self.data[b.y][b.x]:
                        case "-":
                            b.dir = "L"
                            self.beams.append(Beam(b.x, b.y, "R"))
                            self.activeBeams += 1
                        case "\\":
                            b.dir = "R"
                        case "/":
                            b.dir = "L"
                else:
                    b.active = False
                    self.activeBeams -= 1
                    return

        tile = str(b.x) + ":" + str(b.y)
        if (tile + b.dir) in self.tilesDir:
            b.active = False
            self.activeBeams -= 1
        else:
            self.tilesDir.append(tile + b.dir)
        if tile not in self.tilesValid:
            self.tilesValid.append(tile)
        




if __name__ == '__main__':
    main()