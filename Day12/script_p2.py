import time, sys, multiprocessing
from multiprocessing import Value
from functools import lru_cache
import concurrent.futures

debug = False
result_p2 = Value('i', 0)
totalRows = Value('i', 0)
status_p2 = Value('i', 0)


def main():
    if __name__ == '__main__':
        global totalRows, result_p2
        with open('input.txt', 'r') as f:
            data = [[l.split()[0],tuple([int(x) for x in l.split()[1].split(",")])] for l in f.read().splitlines()]
            
        data_p2 = []

        for l in data:
            l_p2 = []
            l_p2.append('?'.join([l[0], l[0], l[0], l[0], l[0]]))
            l_p2.append(tuple([*l[1], *l[1], *l[1], *l[1], *l[1]]))
            data_p2.append(l_p2)
            totalRows.value += 1
    
        start_p2 = time.perf_counter()
        '''pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
        for l in data_p2:
            pool.apply(getArrangements, args = (l[0], l[1], 0),  callback = resultCallback)

        pool.close()
        pool.join()
        
        print('Total Part 2: ' + str(result_p2.value))
        print("[" + str(time.perf_counter()-start_p2) + "s]")
        print('Done', flush=True)
        '''
        total_p2 = 0
        counter = 0

        '''
        with multiprocessing.Pool() as pool:
        # execute tasks in order, process results out of order
            for result in pool.imap_unordered(launch, data_p2):
                total_p2 += result
                counter += 1
                print(str(counter) + "/" + str(len(data_p2)), end="\r", flush=True)
        '''
        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            executor.map(launch2, data_p2)

        print('Total Part 2: ' + str(result_p2.value))
        print("[" + str(time.perf_counter()-start_p2) + "s]")


def launch(data):
    return getArrangements(data[0], data[1], 0)

def launch2(data):
    resultCallback(getArrangements(data[0], data[1], 0))
    
def resultCallback(res):
    global totalRows, status_p2, result_p2
    result_p2.value += res
    status_p2.value += 1
    print(str(status_p2.value) + "/" + str(totalRows.value), end="\r", flush=True)


@lru_cache(maxsize = 5000)
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