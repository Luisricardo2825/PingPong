# Classe responsável por criar a entidade "Barra" dentro do canvas
class Barra:
    def __init__(self, canvas, color, length, lost):
        self.lost = lost
        self.pos = 0
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, length, 10, fill=color)  # Cria a barra(Visualmente)
        self.canvas.move(self.id, 200, 400)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()  # Captura o tamanho do canvas instanciado
        self.canvas.bind_all("<KeyPress-Left>", self.move_left)  # Ação ao clicar na teclas "Arrow Left"
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)  # Ação ao clicar na tecla "Arrow Right"

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        self.pos = self.canvas.coords(self.id)

        if not self.pos:  # Valida se "pos" esta vazio, para evitar erros por conta do tamanho do array
            return print("Pos of barra is empty")
        if self.pos[0] <= 0:
            self.x = 0

        if self.pos[2] >= self.canvas_width:
            self.x = 0

        if not self.lost:
            self.canvas.after(10, self.draw)

    def move_left(self, event):
        if self.pos[0] >= 0:
            self.x = -3

    def move_right(self, event):
        if self.pos[2] <= self.canvas_width:
            self.x = 3

    # Para corrigir o Bug de "pontuação fantasma"
    def __del__(self):
        print("Destroyed barra")
        self.canvas.delete(self.id)
