from itertools import cycle

def main():
    file = open('input.txt', 'r')
    directions, _, *str_map = file.read().splitlines()
    map = {mp[0:3]: {'L': mp[7:10], 'R': mp[12:15]} for mp in str_map}

    curPosition = "AAA"
    total = 0
    dir = cycle(directions)
    while curPosition != "ZZZ":
        total += 1
        curPosition = map[curPosition][next(dir)]

    print("Total: " + str(total))

main()