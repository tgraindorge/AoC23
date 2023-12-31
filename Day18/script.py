from shapely import Polygon

def main():
    file = open('input.txt', 'r').read()
    instr = [[ln.split()[0], int(ln.split()[1])] for ln in file.splitlines()]
    instr_p2 = [[ln.split()[2][7], int(ln.split()[2][2:7],16)] for ln in file.splitlines()]

    print("Total part 1: " + str(computeArea(instr)))
    print("Total part 2: " + str(computeArea(instr_p2)))

def computeArea(instr):
    cur_x, cur_y, len = 0, 0, 0
    pointsMap = []
    for l in instr:
        len += l[1]
        match l[0]:
            case "3" | "U":
                cur_y -= l[1]
            case "0" | "R":
                cur_x += l[1]
            case "1" | "D":
                cur_y += l[1]
            case "2" | "L":
                cur_x -= l[1]
        pointsMap.append([cur_x, cur_y])
    pointsMap.append([0,0])
    return int(Polygon(pointsMap).area + (len/2)+1)

main()