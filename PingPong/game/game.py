import time
from tkinter import Button, Entry, Label, Canvas

from PingPong.Entities.barra_entity import Barra
from PingPong.Entities.bola_entity import Bola


class Game:
    def __init__(self, root, score_now, game, lost, length):
        self.length = length
        self.root = root
        self.count = 0
        self.score_now = score_now
        self.barra_entity = None
        self.canvas = Canvas(root, width=800, height=600, bd=0, highlightthickness=0)
        self.canvas.pack()
        self.bola_entity = None
        self.lost = lost
        self.game = game

    def init_game(self):
        self.barra_entity = Barra(self.canvas, "olive", self.length, self.lost)

        self.bola_entity = Bola(self.canvas, self.barra_entity, "white", self.barra_entity.pos, self.lost, self.count,
                                self.score, self.game_over)

        self.score_now = self.canvas.create_text(370, 20, text="Você acertou " + str(self.count) + "x", fill="lime",
                                                 font=("Arial", 20))
        self.game = self.canvas.create_text(400, 300, text=" ", fill="white", font=("Arial", 40))

        self.canvas.bind_all("<Button-1>", self.start_game)

        self.start_game()

    def create_gui(self):
        level_label = Label(self.root, text="Qual nível você gostaria de jogar? 1/2/3/4/5", font=("Arial", 20))
        level_label.pack()
        level_entry = Entry(self.root, font=("Arial", 20))
        level_entry.pack()
        submit_button = Button(self.root,
                               text="Enviar",
                               font=("Arial", 20),
                               command=lambda: self.set_level(None, level_label, level_entry, submit_button))
        submit_button.pack()
        submit_button.bind("<Return>", self.set_level)

    def start_game(self, event=None):
        self.lost = False
        self.count = 0
        self.score()
        self.canvas.itemconfig(self.game, text=" ")
        time.sleep(1)
        self.barra_entity.draw()
        self.bola_entity.draw()

    def game_over(self):
        self.canvas.itemconfig(self.game, text="Game over!")

    def score(self):
        self.canvas.itemconfig(self.score_now, text="Você acertou " + str(self.count) + "x")

    def set_level(self, event, level_label, level_entry, submit_button):
        level = int(level_entry.get())
        self.length = 500 / level
        level_label.destroy()
        level_entry.destroy()
        submit_button.destroy()
        self.init_game()
