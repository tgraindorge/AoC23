import re
from itertools import cycle
from math import lcm

def main():
    file = open('input2.txt', 'r')
    directions, _, *str_map = file.read().splitlines()
    map = {mp[0:3]: {'L': mp[7:10], 'R': mp[12:15]} for mp in str_map}

    positions = [mp for mp in map if mp.endswith('A')]
    ways_distance = [0] * len(positions)

    
    for i, p in enumerate(positions):
        dir = cycle(directions)
        while not p.endswith('Z'):
            ways_distance[i] += 1
            p = map[p][next(dir)]

    print("Part 2: " + str(lcm(*ways_distance)))
    
main()