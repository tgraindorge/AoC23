import time

def main():
    with open('input.txt', 'r') as f:
        data = [[l.split()[0],tuple([int(x) for x in l.split()[1].split(",")])] for l in f.read().splitlines()]
        
    total = 0
    
    start_p1 = time.perf_counter()
    for l in data:
       total += getArrangements(l[0], l[1], 0)

    print("Total Part 1: " + str(total))
    print("[" + str(time.perf_counter()-start_p1) + "s]")

    
def getArrangements(pat : str, blocks : [int], count : int) -> int:
    minLength = 0
    for b in blocks:
        minLength += b + 1
    minLength -=1
    bMax = len(pat) - minLength

    isLastBlock = len(blocks) == 1
    i = 0
    while i<= bMax:
        if (all( tile in ['?', '#'] for tile in pat[i:i+blocks[0]])  and # Block placecment OK
                ((i+blocks[0]) == len(pat) or pat[i+blocks[0]] in ["?","."] ) and # End of string OR next char ? or .
                (i == 0 or pat[i-1] in ["?","."]) # First in string OR prev char ? or .
            ):
            if isLastBlock:
                if len(pat[i+blocks[0]:])==0 or all(tile in ['.','?'] for tile in pat[i+blocks[0]:]):
                    count += 1
            else:
                count = getArrangements(pat[i+blocks[0]+1:], blocks[1:], count)
        if pat[i] == "#":
            break
        i+=1
    return count

if __name__ == "__main__":
    main()