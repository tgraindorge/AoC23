import re

def main():
    lines = open('input2.txt', 'r').readlines()
    map = []
    emptyRow = re.compile(r"^\.*$")
    for line in lines:
        map.append(line)
        if re.search(emptyRow,line):
            map.append(line)
    
    for r in map:
        print(r)

main()