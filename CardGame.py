import random

class Card():
    def __init__(self, type, numb):
        self.type = type
        self.numb = numb
    

class Cards():   
    def __init__(self):
        self.temp = []
        self.deck = []
        self.types = ["hearts", "diamonds", "clubs", "spades"]


    def shuffle(self):
        self.temp.clear()
        self.deck.clear()
        for type in self.types:
            for i in range(1,14):
                self.temp.append(Card(type, i))
        
        while len(self.temp) != 0:
            x = random.randrange(len(self.temp))
            self.deck.append(self.temp[x])
            self.temp.pop(x) 
            
        
        
class Player:
    def __init__(self):
        self.hand = []
        self.bal = 0

    def set_bat(self, bal):
        self.bal = bal
        
    def bet(self, numb):
        pass
    
    def fold(self):
        pass

    def check(self):
        pass

    def get_card(self, card):
        self.hand.append(card)
        return self.hand

    def show_hand(self):
        for i in range(len(self.hand)):
            print(self.hand[i].type, self.hand[i].numb)




