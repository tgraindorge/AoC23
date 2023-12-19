def main():
    with open('input2.txt', 'r') as f:
        data = [s for s in f.read().split(",")]
        total = 0
        for s in data:
            total += holiday(s)
        print("Part 1: " + str(total))

        boxes = []
        for i in range(256):
            boxes.append(Box())
        
        for s in data:
            print("Label: " + s.split("=")[0] + " | box: " + str(holiday(s.split("=")[0])) + " | focale: " + s[-1])
            if "=" in s:
                boxes[holiday(s.split("=")[0])].addLens(s)
            else:
                boxes[holiday(s.split("-")[0])].removeLens(s.split("-")[0])

        total_p2 = 0
        
        for i, b in enumerate(boxes):
            total_p2 += b.getTotal(i+1)
            if len(b.lenses) > 0:
                print("Box #" + str(i+1) + " > " + str(b.getTotal(i+1)))
        
        print("Part 2: " + str(total_p2))

def holiday(str):
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
        existingLensIndex = self.hasLens(newLens.label)
        if existingLensIndex != 99999:
            self.lenses[existingLensIndex] = newLens
        else:
            self.lenses.append(newLens)

    def removeLens(self, _label):
        lensIndex = 99999
        for i, l in enumerate(self.lenses):
            if l.label == _label:
                lensIndex = i
        if lensIndex != 99999:
            self.lenses.pop(lensIndex)

    def getTotal(self, _boxIndex):
        total = 0
        for i, l in enumerate(self.lenses):
            print(l.label)
            total += _boxIndex * i * l.val
        return total


if __name__ == "__main__":
    main()