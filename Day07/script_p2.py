import re
import math

def main():
    file = open('input.txt', 'r')
    Lines = file.readlines()
    Hands = list()
    for line in Lines:
       hand = Hand(line.split(" ")[0], int(line.split(" ")[1]))
       hand.computeHand()
       Hands.append(hand)
    sortedHands = sorted(Hands, key=lambda x: x.rank, reverse=False)
    total = 0
    i = 1
    for h in sortedHands:
        total += h.bet * i
        i +=1
    print("Total: " + str(total))
    

class Hand:
  def __init__(self, cards : str, bet : int):
    self.cards = cards
    self.bet = bet
    self.type = 0
    self.rank = 0
    self.TYPE_5OAK = 0xF
    self.TYPE_4OAK = 0xE
    self.TYPE_FH   = 0xD
    self.TYPE_3OAK = 0xC
    self.TYPE_2P   = 0xB
    self.TYPE_1P   = 0xA
    self.TYPE_HC   = 0x9
    
    self.cardValue = {}
    self.cardValue['A'] = 0xF
    self.cardValue['K'] = 0xE
    self.cardValue['Q'] = 0xD
    self.cardValue['J'] = 0x2
    self.cardValue['T'] = 0xB
    self.cardValue['9'] = 0xA
    self.cardValue['8'] = 0x9
    self.cardValue['7'] = 0x8
    self.cardValue['6'] = 0x7
    self.cardValue['5'] = 0x6
    self.cardValue['4'] = 0x5
    self.cardValue['3'] = 0x4
    self.cardValue['2'] = 0x3
    
  def computeHand(self):
    cardCount = {}
    jokerCount = 0
    for c in self.cards:
        if c == "J":
            jokerCount+=1
        if c in cardCount:
            cardCount[c] +=1
        else:
            cardCount[c] = 1

    cardCount = dict(sorted(cardCount.items(), key=lambda x:x[1], reverse=True))

    match list(cardCount.values())[0]:
        case 5:
            self.type = self.TYPE_5OAK
        case 4:
            self.type = self.TYPE_4OAK
            if jokerCount == 1 or jokerCount == 4:
                self.type = self.TYPE_5OAK
        case 3:
            if list(cardCount.values())[1] == 2:
               self.type = self.TYPE_FH
               if jokerCount == 3 or jokerCount == 2:
                   self.type = self.TYPE_5OAK
            else:
               self.type = self.TYPE_3OAK
               if jokerCount == 3 or jokerCount == 1:
                   self.type = self.TYPE_4OAK
        case 2:
            if list(cardCount.values())[1] == 2:
               self.type = self.TYPE_2P
               if jokerCount == 1:
                   self.type = self.TYPE_FH
               elif  jokerCount == 2:
                   self.type = self.TYPE_4OAK
               
            else:
               self.type = self.TYPE_1P
               if jokerCount >= 1:
                   self.type = self.TYPE_3OAK
        case _:
          self.type = self.TYPE_HC
          if jokerCount == 1:
                   self.type = self.TYPE_1P
    
    self.rank = self.type
    for c in self.cards:
        self.rank = append_hex(self.rank, self.cardValue[c])


def append_hex(a, b):
    sizeof_b = 0
    while((b >> sizeof_b) > 0):
            sizeof_b += 1
    sizeof_b_hex = math.ceil(sizeof_b/4) * 4
    return (a << sizeof_b_hex) | b

main()