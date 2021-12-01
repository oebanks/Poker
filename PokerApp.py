import tkinter as tk
from PIL import ImageTk, Image
import PokerGame as pg
import CardGame as cg



class PokerGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("910x540")
        self.window.title("Poker")
        #Fonts
        self.LARGE_FONT_STYLE = ("Arial", 40, "bold")
        #Instantiates poker variables
        self.poker = pg.Poker()
        self.poker.playing = []
        self.player_count = 0
        self.first_player = True
        #image_directories
        self.images = {}
        for key in self.poker.cards.image_dict.keys():
            self.images[key] = self.ready_img(self.poker.cards.image_dict[key], (115, 176))
        self.images["start_screen"] = self.ready_img("start_screen1.jpg",(910,540))
        self.images["red_back"] = self.ready_img("card_images/red_back.jpg",(115, 176))
        #Instantiates start screen
        self.start_canvas = self.create_start_canvas()

        self.button_num = 0
        self.dealt = False

    def ready_img(self, path, size): 
            return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ANTIALIAS))

    def create_start_canvas(self):
        #Creates a start screen with an image resized to fill the screen
        start_canvas = tk.Canvas(self.window, width = 1820, height= 1080)
        start_canvas.pack(fill = "both", expand = True)
        start_canvas.create_image(0,0, image = self.images.get("start_screen"), anchor = "nw")
        start_canvas.create_text(455,250, text = "TEXAS HOLD'EM", font=("Algerian, 50"), fill="gold")
        start_btn = tk.Button(self.window, text="Start", command= lambda:self.start())
        start_btn_window = start_canvas.create_window(450,330, anchor="nw", window=start_btn)
        return start_canvas

    def start(self):
        #Deletes start screen widgets and canvas
        for widget in self.window.winfo_children():
            widget.destroy()
        self.start_canvas.pack_forget()

        #Instantiates new frames
        #self.title_frame = self.create_title_frame()
        self.player_list_frame = self.create_player_entry_frame()
        # self.table_frame = self.create_table_frame()
        self.actions_frame = self.create_player_actions_frame()
        self.player_frame = self.create_player_frame()
        self.player_canvas = self.create_player_canvas()
        self.player_cards_canvas = self.create_player_cards_canvas()
        self.player_button_frame = self.create_player_button_frame()
        self.table_canvas = self.create_table_canvas()

    def create_player_entry_frame(self):
        #Creates a frame to input players
        player_list_frame = tk.Frame(self.window)
        player_list_frame.place( relx= .75, rely =.02, relheight=.3, relwidth=.2)
        player_list_frame.grid_columnconfigure(0, weight=1)
        self.players_ent = tk.Entry(player_list_frame, width = 10)
        self.players_ent.grid(row=0, column=0,sticky= "ne")
        players_btn = tk.Button(player_list_frame, text = "Add Player", command = self.add_player_button)
        players_btn.grid(row = 0, column=1)
        deal_players_btn = tk.Button(player_list_frame, text = "Deal Players", command = self.deal_player_cards)
        deal_players_btn.grid(row = 1, column=1)
        flop_btn = tk.Button(player_list_frame, text = "Deal Flop Cards", command = self.flop)
        flop_btn.grid(row = 2, column=1)
        turn_btn = tk.Button(player_list_frame, text = "Deal Turn Card", command = self.turn)
        turn_btn.grid(row = 3, column=1)
        river_btn = tk.Button(player_list_frame, text = "Deal River Card", command = self.river)
        river_btn.grid(row = 4, column=1)
        return player_list_frame

    def add_player_button(self):
        if self.first_player :
            self.update_player_button_frame()
            self.first_player = False
        else :
            self.player_count += 1
            self.button_num += 1
            self.update_player_button_frame()

    def create_player_button_frame(self):
        player_button_frame = tk.Frame(self.window)
        player_button_frame.place( relx= .1, rely =.07, relheight=.1, relwidth=.7)
        return player_button_frame

    def create_table_canvas(self):
        table_canvas = tk.Canvas(self.window)
        table_canvas.place( relx= .15, rely =.2, relheight=.33, relwidth=.65)
        return table_canvas

    def update_table_canvas(self):
        for i, card in enumerate(self.poker.table_cards):
            card_name = card.num + card.type
            image = self.images.get(card_name)
            self.table_canvas.create_image(115*i,0, image = image, anchor = "nw")

    def flop(self):
        self.poker.flop()
        self.update_table_canvas()

    def turn(self):
        self.poker.turn()
        self.update_table_canvas()
    
    def river(self):
        self.poker.river()
        self.update_table_canvas()

    def update_player_button_frame(self):
        if self.players_ent.get():
            player = cg.Player()
            player.name = self.players_ent.get()
            self.poker.playing.append(player)
            button = tk.Button(self.player_button_frame, text = self.players_ent.get(), command = lambda num =self.button_num: self.name_button(num))
            button.grid(row = 0, column=self.player_count)
            self.update_screen()

    def name_button(self, num):
        self.player_count = num
        self.update_screen()

    def update_screen(self):
        if self.dealt == False:
            self.update_player_frame()
        else:
            self.update_player_frame()
            self.update_player_cards_canvas()
            
    def create_player_cards_canvas(self):
        self.player_cards_canvas = tk.Canvas(self.window, width = 352, height= 120, bg = "blue")
        self.player_cards_canvas.place( relx= .02, rely =.65, relheight=.33, relwidth=.25)
        card = self.images.get("red_back")
        self.player_cards_canvas.create_image(0,0, image = card, anchor = "nw")
        self.player_cards_canvas.create_image(115,0, image = card, anchor = "nw")
        return self.player_cards_canvas

    def update_player_cards_canvas(self):
        for widget in self.player_cards_canvas.winfo_children():
            widget.destroy()
        
        player = self.current_player()
        #print(f"{player},{self.poker.playing}")
        card1_name = player.hand[0].num + player.hand[0].type
        card2_name = player.hand[1].num + player.hand[1].type
        card1 = self.images.get(card1_name)
        card2 = self.images.get(card2_name)
        self.player_cards_canvas.create_image(0,0, image = card1, anchor = "nw")
        self.player_cards_canvas.create_image(115,0, image = card2, anchor = "nw")
        
    def deal_player_cards(self):
        self.poker.give_hands()
        self.dealt = True
        self.update_player_cards_canvas()

    def create_player_actions_frame(self):
        actions_frame = tk.Frame(self.window)
        actions_frame.place( relx = .75, rely =.7, relheight= .3, relwidth= .25)
        bet_button = tk.Button(actions_frame, text = "Bet")
        bet_button.grid(row = 0, column=0)
        bet_entry = tk.Entry(actions_frame)
        bet_entry.grid(row = 0, column=1)
        check_button = tk.Button(actions_frame, text = "Check")
        check_button.grid(row = 1, column=0)
        raise_button = tk.Button(actions_frame, text = "Raise")
        raise_button.grid(row = 2, column=0)
        fold_button = tk.Button(actions_frame, text = "Fold")
        fold_button.grid(row = 3, column=0)
        bal_button = tk.Button(actions_frame, text = "Set Balance", command = self.set_balance)
        bal_button.grid(row = 4, column=0)
        self.bal_entry = tk.Entry(actions_frame)
        self.bal_entry.grid(row = 4, column=1)
        return actions_frame

    def create_player_frame(self):
        #Instantiates area for profile picture, name, and balance
        player_frame = tk.Frame(self.window)
        player_frame.place( relx = .4, rely =.7, relheight= .3, relwidth= .2)
        return player_frame

    def update_player_frame(self):
        #Shows Profile picture and player name and balance
        player = self.current_player()
        for widget in self.player_frame.winfo_children():
            widget.destroy()

        self.player_canvas = tk.Canvas(self.player_frame, width = 130, height=130, borderwidth= 0)
        self.player_canvas.grid(row=0,columnspan=2)
        self.player_canvas.create_oval(10, 10, 130, 120, fill= 'cyan')
        self.player_name_label = tk.Label(self.player_frame, text = player.name)
        self.player_name_label.grid(row=1,column=0)
        self.player_bal_label = tk.Label(self.player_frame, text = player.bal)
        self.player_bal_label.grid(row=1,column=1) 

    def create_player_canvas(self):
        #Instantiates area for profile picture, name, and balance
        player_canvas = tk.Canvas(self.player_frame, width = 130, height=130, borderwidth= 0)
        player_canvas.grid(row=0,columnspan=2)
        return player_canvas
    
    def set_balance(self):
        player = self.current_player()
        bal_str = self.bal_entry.get()
        bal = int(bal_str)
        player.set_bal(bal)
        self.update_player_frame()

    def current_player(self):
        player = self.poker.playing[self.player_count]
        return player

    def run(self):
        self.window.mainloop()      

if __name__ == "__main__":
    pokergui = PokerGUI()
    pokergui.run()
