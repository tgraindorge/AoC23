import re

def main():
    file = open('input.txt', 'r').read()
    wf_data = file.split("\n\n")[0].splitlines()
    parts_data = file.split("\n\n")[1].splitlines()
    wfNamePattern = re.compile(r"([a-z]+){")
    
    l_parts = [Part(p) for p in parts_data]
    l_wf = dict()
    for w_str in wf_data:
        wf = Workflow(w_str, wfNamePattern)
        l_wf[wf.label] = wf

    total = 0
    for p in l_parts:
        if(isPartValid(l_wf, p)):
            total += p.getTotal()

    print("Total part 1: " + str(total))

def isPartValid(l_wf, p):
    cur = "in"
    while cur not in ['A', 'R']:
        cur = l_wf[cur].process(p.x, p.m, p.a, p.s)
    if cur == "A":
        return True
    return False

class Part:
    def __init__(self, data) -> None:
        self.x, self.m, self.a, self.s = (int(v[2:]) for v in data[1:-1].split(','))
    def getTotal(self):
        return sum([self.x, self.m, self.a, self.s])

class Workflow:
    def __init__(self, data, wfNamePattern) -> None:
        self.label = re.search(wfNamePattern, data).group(1)
        self.cond = [c for c in data[len(self.label)+1:-1].split(',')]
        self.default = self.cond[-1]
        self.cond.pop()

    def process(self, x, m, a ,s):
        for c in self.cond:
            if eval(c.split(":")[0]):
                return c.split(":")[1]
        return self.default

if __name__ == "__main__":
    main()