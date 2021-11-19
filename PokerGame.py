import CardGame as cg

class Poker():

    def __init__(self):
        self.cards = cg.Cards()
        self.deck = self.cards.shuffle()
        self.playing = []
        self.term = 0
        self.table_cards = []
        self.active_playing = self.playing
        self.max_bet_size = 0
        self.pot = 0
        self.name = ""

    def add_player(self, player):
        self.playing.append(player)

    def shuffle(self):
        self.cards.shuffle()

    def give_hands(self):
        #Gives each player a card and removes that card from the deck.
        #This is done twice
        for i in range(2):
            for i in range(len(self.playing)):
                self.playing[i].get_card(self.deck[0])
                self.deck.pop(0)

    def next(self):
        self.term += 1
        self.game(self.term);

    def game(self):
        switcher = {
            0: self.pre_flop(),
            1: self.flop(),
            2: self.turn(),
            3: self.river()
        }

    def pre_flop(self):
        pass


    def flop(self):
        self.deck.pop(0)
        for i in range(3):
            self.table_cards.append(self.deck[0])

    def turn(self):
        self.deck.pop(0)
        self.table_cards.append(self.deck[0])

    def river(self):
        self.deck.pop(0)
        self.table_cards.append(self.deck[0])

    def bet(self, player, num):
        #Checks that bet is more than current bet size. If yes, bet is removed from
        #player balance and added to pot
        if (player.bet_size + num) > self.max_bet_size:
            player.bet(num)
            self.max_bet_size = player.bet_size
            self.pot += num
            self.next_player()
        else:
            print("Bet error")
        

    def check(self, player):
        if player.bet_size == self.max_bet_size:
            self.next_player()
        else:
            print("Unable to check")
        
    def fold(self, player):
        self.active_playing.pop(player)
        self.next_player()

    def win(self, player):
        player.win(self.pot)
        self.new_game()

    def next_player(self):
        pass

    def new_game(self):
        #Resets Game
        self.pot = 0
        self.active_playing = self.playing
        self.shuffle()
        self.table_cards.clear()



#texas = Poker()

#Olanre = cg.Player()
# Haden = cg.Player()
#texas.add_player("Olanre")
# texas.add_player(Haden)
# texas.give_hands()
# Olanre.set_bal(1000)
# print(Olanre.bal)
# texas.bet(Olanre, 500)
#print(repr(texas.playing))

