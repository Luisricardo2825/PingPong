import random


class Bola:
    def __init__(self, canvas, barra, color, barra_pos, lost, count, score, game_over):
        self.score = score
        self.game_over = game_over
        self.count = count
        self.lost = lost
        self.Barra_pos = barra_pos
        self.canvas = canvas
        self.Barra = barra
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 245, 200)

        starts_x = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts_x)

        self.x = starts_x[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = 3

        if pos[3] >= self.canvas_height:
            self.y = -3

        if pos[0] <= 0:
            self.x = 3

        if pos[2] >= self.canvas_width:
            self.x = -3
        # print()
        self.Barra_pos = self.canvas.coords(self.Barra.id)

        if pos[2] >= self.Barra_pos[0] and pos[0] <= self.Barra_pos[2]:
            if self.Barra_pos[1] <= pos[3] <= self.Barra_pos[3]:
                self.y = -3
                self.count += 1

                self.score()

        if pos[3] <= self.canvas_height:
            self.canvas.after(10, self.draw)
        else:
            self.game_over()
            self.lost = True
