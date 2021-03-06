import random
class Card():
    #Creates an object with a specified number and type
    def __init__(self, type, num):
        self.type = type
        self.num = num
    
class Cards(): 
    #Instantiates and defines multiple Card objects   
    def __init__(self):
        self.deck = []
        self.types = ["H", "D", "C", "S"]
        self.nums = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        #Dictionary that connects a card to it's image path
        self.image_dict = {}
        for num in self.nums:
            for type in self.types:
                card = str(num+type)
                path = str("card_images/"+card+".jpg")
                self.image_dict[card] = path
        
    def shuffle(self):
        temp = []
        self.deck.clear()
        for type in self.types:
        #Creates a ordered temporary deck from 1- 13 of different card types
            for num in self.nums:
                temp.append(Card(type, num))
        
        while len(temp):
        #Randomizes the temporary deck
            x = random.randrange(len(temp))
            self.deck.append(temp[x])
            temp.pop(x) 

        return self.deck
        
        
class Player:
    def __init__(self):
        self.hand = []
        self.bal = 0
        self.bet_size = 0

    def set_bal(self, bal):
        self.bal = bal
        
    def bet(self, num):
        self.bal -= num
        self.bet_size += num

    def clear_bets(self):
        self.bet_size = 0
    
    def win(self, num):
        self.bal += num

    def fold(self):
        pass

    def check(self):
        pass

    def get_card(self, card):
        self.hand.append(card)
        return self.hand


# if __name__ == "__main__":

#     # cards = Cards()
#     # cards.shuffle()
#     # card = Card("H","A")
#     # for value in card.image_dict.values():
#     #     print(card.image_dict[value])

#     cards = Cards()
#     print(cards.image_dict['5S'])

    # card = Card("H","A")
    # for key in card.image_dict.keys():
    #     print(card.image_dict[key])
#     # for i in range(len(cards.deck)):
#     #     print(f"{cards.deck[0]}")
#     print(f"{cards.deck[0].image_dict}")
    