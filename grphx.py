import tkinter
import random
import time


class Ball:
    def __init__(self, canvas, color,x,y,size,gol,refresh_rate):
        self.canvas = canvas
        self.size = size
        self.color = color
        self.gol = gol
        self.clr_arry=["red","blue","white"]
        self.x = x
        self.y = y
        self.refresh_rate = refresh_rate
        self.id = canvas.create_rectangle(size, size, 2*size, 2*size, fill=color, outline='')
        self.canvas.move(self.id, size*x, size*y)

        #self.canvas.bind("<Button-1>", self.canvas_onclick)
        #self.text_id = self.canvas.create_text(300, 200, anchor='se')
        #self.canvas.itemconfig(self.text_id, text='hello')

    # def canvas_onclick(self, event):
    #     self.canvas.itemconfig(
    #         self.text_id, 
    #         text="You clicked at ({}, {})".format(event.x, event.y)
    #     )

    def draw(self):
        if not self.gol.exists(self.x,self.y) : color='white' 
        else : color = self.color
        self.canvas.itemconfigure(self.id,fill=color)
        #self.canvas.after(self.refresh_rate, self.draw)

class BoardGame:
    def __init__(self,size,mx,my,color,gol,refresh_rate):
        self.root = tkinter.Tk()
        self.root.title = "Game"
        self.root.resizable(0,0)
        self.root.wm_attributes("-topmost", 1)
        self.canvas = tkinter.Canvas(self.root, width=1.15*size*mx, height=1.15*size*my+size, bd=0, highlightthickness=0)
        self.canvas.pack()
        self.size = size
        self.mx = mx
        self.my = my
        self.bb = {}
        self.color = color
        self.gol = gol
        self.refresh_rate = refresh_rate
        for x in range (mx) :
            for y in range (my) :
                self.bb[x,y] = Ball(self.canvas, color,x,y,size,gol,refresh_rate)
                self.bb[x,y].draw()
        self.sim()
        self.root.mainloop()

    def sim(self):
        for x in range (self.mx) :
            for y in range (self.my) :
                self.bb[x,y].draw()
        self.gol.Scan()
        self.gol.commit()
        self.canvas.after(self.refresh_rate, self.sim)
