import time
from tkinter import Button, Entry, Label, Canvas

from Entities.barra_entity import Barra
from Entities.bola_entity import Bola


class Game:
    lost = False
    length = 10

    def __init__(self, root, score_now, game):  # Responsável apenas por administrar os elementos do jogo
        # e metodos de ciclo de vida
        self.root = root
        self.count = 0
        self.score_now = score_now
        self.barra_entity: Barra = None
        self.canvas = Canvas(root, width=800, height=600, bd=0, highlightthickness=0)
        self.canvas.pack()
        self.bola_entity: Bola = None
        self.game = game

    def init_game(self):  # Instancia um novo jogo
        self.init_entities()  # Inicializa os componentes Barra e Bola
        self.score_now = self.canvas.create_text(370, 20, text="Você acertou " + str(self.count) + "x", fill="lime",
                                                 font=("Arial", 20))
        self.game = self.canvas.create_text(400, 300, text=" ", fill="white", font=("Arial", 40))

        self.canvas.bind_all("<Button-1>", self.start_game)  # Botão responsável pelo "restart"

        self.start_game()

    def init_entities(self):  # Cria as entidades dentro do canvas(Bola e barra)
        self.barra_entity = Barra(self.canvas,
                                  "olive",  # Cor da barra
                                  self.length,
                                  self.lost)

        self.bola_entity = Bola(self.canvas,
                                self.barra_entity,
                                "white",  # Cor da bola
                                self.barra_entity.pos,
                                self.score,
                                self.game_over)
        self.bola_entity.draw()  # Desenha a entidade bola no canvas
        self.barra_entity.draw()  # Desenha a entidade barra no canvas

    def destroy_entities(self):  # Destroi as entidades adicionadas ao canvas(Bola e barra)
        self.barra_entity.__del__()
        self.bola_entity.__del__()

    def create_gui(self):  # Criar os componentes de interface(Botões inicias)
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

    def start_game(self, event=None):  # Inicia um novo jogo
        self.lost = False
        self.count = 0
        self.score(0)
        self.canvas.itemconfig(self.game, text=" ")  # Remove o "Game over" ao iniciar
        time.sleep(1)
        self.destroy_entities()  # Destroi as entitades
        self.init_entities()  # Cria as entidades no canvas

    def game_over(self):  # Adiciona um texto de "game over" ao canvas
        self.canvas.itemconfig(self.game, text="Game over!")
        self.lost = True

    def score(self, scores):  # Atualiza os scores
        self.canvas.itemconfig(self.score_now, text="Você acertou " + str(self.count + scores) + "x")

    # "Seta" o valor da variavel nivel e inicia o jogo
    def set_level(self, event, level_label, level_entry, submit_button):
        level = int(level_entry.get())
        self.length = 500 / level
        level_label.destroy()
        level_entry.destroy()
        submit_button.destroy()
        self.init_game()
