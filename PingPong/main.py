from tkinter import NW, Tk

from PIL import Image, ImageTk
from PingPong.game.game import Game

# Variáveis globais
score_now = 0
game = " "
lost = False
length = 10


def create_root():
    instance = Tk()
    instance.title("Ping Pong")
    instance.resizable(False, False)
    instance.wm_attributes("-topmost", 1)
    instance.iconbitmap('assets/favicon.ico')
    return instance


root = create_root()  # Cria  o root da janela

# Cria a interface inicial com o botão enviar
game_instance = Game(root, score_now, game, lost, length)

# Adiciona background
background_image_path = "assets/marte.png"
bg_image = Image.open(background_image_path)
bg_photo = ImageTk.PhotoImage(bg_image)
game_instance.canvas.create_image(0, 0, image=bg_photo, anchor=NW)  # Só deus sabe pq só aqui que o background funciona
# Fim background

game_instance.create_gui()

root.mainloop()
