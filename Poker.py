import CardGame as cg

class Poker():

    def __init__(self):
        #instantiates class Cards as Cards
        self.Cards = cg.Cards()
        self.Cards.shuffle()
        self.deck = self.Cards.deck
        term = ["pre", "river", "turn", "flop"]
        term_int = 0
        self.gamers = []
        self.term = term[0]

    def add_gamer(self, gamer):
        self.gamers.append(gamer)
    
    def shuffle(self):
        self.table.shuffle()

    def give_hands(self):     
        for i in range(len(self.gamers)):
            self.gamers[i].get_card(self.deck[0])
            self.deck.pop(0)  
        for i in range(len(self.gamers)):
            self.gamers[i].get_card(self.deck[0])
            self.deck.pop(0)

    def next(self):
        if (self.term_int == 3):
            self.term_int = 0
        else:
            self.term_int += 1

Poker = Poker()
Olanre = cg.Player()
Haden = cg.Player()
Poker.add_gamer(Olanre)
Poker.add_gamer(Haden)
Poker.give_hands()
print(Olanre.hand[0].numb)
print(Haden.hand[0].numb)