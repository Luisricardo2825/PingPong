import random


# Classe responsável por criar a entidade "Bola" dentro do canvas
class Bola:
    scores = 0

    def __init__(self, canvas, barra, color, barra_pos, score, game_over):
        self.scores = 0
        self.game_over = game_over
        self.score = score
        self.Barra_pos = barra_pos
        self.canvas = canvas
        self.Barra = barra
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 245, 200)

        starts_x = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts_x) # Posição de X é definidoa de uma forma pseudo aleatoria

        self.x = starts_x[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):  # Metodo que desenha a bola dentro do canvas
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        if not pos:  # Valida se o array esta vazio ou não para evitar erro
            return print("Pos of bola is empty")
        if pos[1] <= 0:
            self.y = 3

        if pos[3] >= self.canvas_height:
            self.y = -3

        if pos[0] <= 0:
            self.x = 3

        if pos[2] >= self.canvas_width:
            self.x = -3
        self.Barra_pos = self.canvas.coords(self.Barra.id)

        # Valida se a bola chegou até a barra, se sim, atuliza o score
        if pos[2] >= self.Barra_pos[0] and pos[0] <= self.Barra_pos[2]:
            if self.Barra_pos[1] <= pos[3] <= self.Barra_pos[3]:
                self.y = -3
                self.scores += 1  # Atualiza LOGICO o valor da pontuação(Atualiza a variavel)
                self.score(self.scores)  # Atualiza o valor VISUAL da pontuação(Basicamente o texto)

        if pos[3] <= self.canvas_height:
            self.canvas.after(10, self.draw)
        else:
            self.game_over()

    # Para corrigir o Bug de "pontuação fantasma"
    def __del__(self):  # Metodo para destruir o objeto
        print("Destroyed bola")
        self.canvas.delete(self.id)
