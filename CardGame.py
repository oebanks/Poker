import random

class Card():
    def __init__(self, type, numb):
        self.type = type
        self.numb = numb
    

class Deck():   
    def Shuffle(self):
        temp = []
        deck = []
        types = ["hearts", "diamonds", "clubs", "spades"]

        for type in types:
            for i in range(1,14):
                temp.append(Card(type, i))
        
        while len(temp) != 0:
            x = random.randrange(len(temp))
            deck.append(temp[x])
            temp.pop(x) 
            
        return deck
        
class Player:
    def __init__(self, name, bal):
        self.name = name
        self.bal = bal
        self.hand = []
        
    def bet(self, numb):
        pass
    
    def fold(self):
        pass

    def check(self):
        pass

    def get_card(self, type, numb):
        self.hand.append(Card(type, numb))
        return self.hand

    def show_hand(self):
        for i in range(len(self.hand)):
            print(self.hand[i].type, self.hand[i].numb)









        


        




        




            
        
