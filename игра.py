from tkinter import *
import time
import random

tk = Tk()
tk.title('Арканоид')
tk.resizable(0, 0)
tk.wm_attributes('-topmost',1)
canvas = Canvas(tk, width=500, height=400, bd=5, highlightthickness=0)
canvas.pack()
tk.update()

class Board:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.board_width = 150
        self.id = canvas.create_rectangle(0, 0, self.board_width, 15, fill= color)

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

        self.x = 0
        self.speed_x = 5

        self.xx = self.canvas_width/2 - self.board_width/2
        self.yy =self.canvas_height - 40
        self.canvas.move(self.id, self.xx, self.yy)

    def move_left(self, event):
        if self.xx + (-1) * self.speed_x >= 0:
            self.x = (-1)*self.speed_x
            self.xx += self.x
            self.draw()

    def move_right(self, event):
        if self.xx + self.speed_x <= self.canvas_width - self.board_width:
            self.x = self.speed_x
            self.xx += self.x
            self.draw()

    def draw(self):
        self.canvas.move(self.id, self.x, 0)



class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 50, 50, fill= color)
        self.canvas.move(self.id, 250, 150)
        start =[-4,-3,3,4]
        random.shuffle(start)
        self.x = start[0]
        self.y = start[1]
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        #print(pos)
        #print(pos[0], pos[1], pos[2], pos[3])
        if pos[1]<=0:
            self.y = self.y * (-1)

        if pos[3]>=self.canvas_height:
            self.y = self.y * (-1)

        if pos[0]<=0:
            self.x = self.x * (-1)

        if pos[2]>=self.canvas_width:
            self.x = self.x * (-1)

ball = Ball(canvas,'black')
board = Board(canvas, 'red')
canvas.bind_all("<KeyPress-Left>", board.move_left)
canvas.bind_all("<KeyPress-Right>", board.move_right)
while 1:

    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.00005)
tk.mainloop( )