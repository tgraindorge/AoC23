def main():
    with open('input.txt', 'r') as f:
        data = [s for s in f.read().split(",")]
        total = 0
        for s in data:
            total += holidayHash(s)
        print("Part 1: " + str(total))

        boxes = []
        for i in range(256):
            boxes.append(Box())
        for s in data:
            if "=" in s:
                boxes[holidayHash(s.split("=")[0])].addLens(s)
            else:
                boxes[holidayHash(s.split("-")[0])].removeLens(s.split("-")[0])

        total_p2 = 0
        for i, b in enumerate(boxes):
            total_p2 += b.getTotal(i+1)
        
        print("Part 2: " + str(total_p2))

def holidayHash(str):
    seq = 0
    for c in str:
        seq += ord(c)
        seq = (seq*17)%256
    return seq

class Lens:
    def __init__(self, _str) -> None:
        self.label = _str.split("=")[0]
        self.val = int(_str[-1])

class Box:
    def __init__(self) -> None:
        self.lenses = []
    
    def hasLens(self, _label) -> int:
        for i, l in enumerate(self.lenses):
            if l.label == _label:
                return i
        return 99999

    def addLens(self, _str):
        newLens = Lens(_str)
        for l in self.lenses:
            if l.label == newLens.label:
                l.val = newLens.val
                return
        self.lenses.append(newLens)

    def removeLens(self, _label):
        lensIndex = self.hasLens(_label)
        if lensIndex != 99999:
            self.lenses.pop(lensIndex)

    def getTotal(self, _boxIndex):
        total = 0
        for i, l in enumerate(self.lenses):
            total += _boxIndex * (i+1) * l.val
        return total

if __name__ == "__main__":
    main()