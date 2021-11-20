import tkinter as tk
from PIL import ImageTk, Image
import PokerGame as pg
import CardGame as cg



class PokerGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("910x540")
        self.window.title("Poker")
        #self.window.configure(bg='#808080')#808080

        #Images
        self.start_img = ImageTk.PhotoImage(Image.open("start_screen1.jpg").resize((910,540), Image.ANTIALIAS))

        #Images are often deleted within functions due to a bug
        #Making images global variables was recommended but this also doesn't work
        global card1_image
        global card2_image 
        card1_image = ImageTk.PhotoImage(Image.open("Card_Images/red_back.png").resize((100,100), Image.ANTIALIAS))
        card2_image = ImageTk.PhotoImage(Image.open("Card_Images/red_back.png").resize((100,100), Image.ANTIALIAS))
        

        #Fonts
        self.LARGE_FONT_STYLE = ("Arial", 40, "bold")


        #Instantiates start screen
        self.start_canvas = self.create_start_canvas()

        self.poker = pg.Poker()
        self.poker.playing = []
        self.playing_cnt = 0

    def create_start_canvas(self):
        #Creates a start screen with an image resized to fill the screen
        start_canvas = tk.Canvas(self.window, width = 1820, height= 1080)
        start_canvas.pack(fill = "both", expand = True)
        start_canvas.create_image(0,0, image = self.start_img, anchor = "nw")
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
        self.title_frame = self.create_title_frame()
        self.player_list_frame = self.create_player_list_frame()
        # self.table_frame = self.create_table_frame()
        self.actions_frame = self.create_actions_frame()
        self.player_frame = self.create_player_frame()
        self.player_canvas = self.create_player_canvas()
        self.player_cards_canvas = self.create_player_cards_canvas()

    def create_title_frame(self):
        #Title Frame with label
        title_frame = tk.Frame(self.window)
        title_frame.place(relx = .32, rely =.05, relheight= .2, relwidth= .4)
        title_lbl = tk.Label(title_frame, text = "TEXAS HOLD'EM", font = self.LARGE_FONT_STYLE)
        title_lbl.pack(fill = tk.BOTH, expand = True)
        return title_frame

    def create_player_list_frame(self):
        #Creates a frame to input players
        player_list_frame = tk.Frame(self.window)
        player_list_frame.place( relx= .02, rely =.1, relheight=.2, relwidth=.25)
        self.players_ent = tk.Entry(player_list_frame, width = 15)
        self.players_ent.grid(row=0, column=0,sticky= "nsew")
        players_btn = tk.Button(player_list_frame, text = "Add Player", command = self.update_player_list)
        players_btn.grid(row = 0, column=1)
        return player_list_frame

    def create_player_cards_canvas(self):
        player_cards_canvas = tk.Canvas(self.window, width = 50, height= 50)
        player_cards_canvas.place( relx= .02, rely =.7, relheight=.2, relwidth=.25)
        player_cards_canvas.create_image(0,0, image = card1_image, anchor = "nw")
        player_cards_canvas.create_image(100,0, image = card2_image, anchor = "nw")

        return player_cards_canvas


    def create_actions_frame(self):
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

    def create_player_canvas(self):
        #Instantiates area for profile picture, name, and balance
        player_canvas = tk.Canvas(self.player_frame, width = 130, height=130, borderwidth= 0)
        player_canvas.grid(row=0,columnspan=2)
        return player_canvas
    
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
        # im_a = Image.new("L", size= [640, 1271], color= 0)
        # draw = Image.ImageDraw.Draw(im_a)
        # draw.ellipse((140, 50, 260, 170), fill=255)
        # im_rgba = self.img.copy()
        # im_rgba.putalpha(im_a)
        # im_rgba_crop = im_rgba.crop((140, 50, 260, 170))
        # player_canvas = tk.Canvas(self.player_frame, bg ="black", width = 100, height=100)
        # player_canvas.grid(row=0,column=0)
        # player_canvas.create_image(0,0, image=im_rgba_crop, anchor="nw")      

        


    def update_player_list(self):
        #Checks that something has been typed in players_ent. 
        #Displays that name and adds them to playing list 
        if self.players_ent.get():
            lbl = tk.Label(self.player_list_frame, text = self.players_ent.get()).grid(row = self.playing_cnt+1, column=0)
            player = cg.Player()
            player.name = self.players_ent.get()
            self.poker.playing.append(player)
            self.update_player_frame()


    def set_balance(self):
        if self.bal_entry.get():
            player = self.current_player()
            bal_str = self.bal_entry.get()
            bal = int(bal_str)
            player.set_bal(bal)
            self.update_player_frame()

    def current_player(self):
        player = self.poker.playing[self.playing_cnt]
        self.playing_cnt += 1
        return player

        


        


    def run(self):
        self.window.mainloop()      

if __name__ == "__main__":
    pokergui = PokerGUI()
    pokergui.run()
    
    