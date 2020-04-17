import tkinter
import random
import time


class Ball:
    def __init__(self, root, color,x,y,size,gol,refresh_rate):
        #self.canvas = canvas
        self.root = root
        self.size = size
        self.color = color
        self.gol = gol
        self.clr_arry=["red","blue","white"]
        self.x = x
        self.y = y
        self.refresh_rate = refresh_rate
        self.lb = tkinter.Label(root,text=' ')
        self.lb.grid(row=y,column=x)

        #self.id = canvas.create_rectangle(size, size, 2*size, 2*size, fill=color, outline='')
        #self.canvas.move(self.id, size*x, size*y)


    # def canvas_onclick(self, event):
    #     self.canvas.itemconfig(
    #         self.text_id, 
    #         text="You clicked at ({}, {})".format(event.x, event.y)
    #     )

    def draw(self):
        if not self.gol.exists(self.x,self.y) : bg='white' 
        else : bg = self.color
        #self.canvas.itemconfigure(self.id,fill=color)
        self.lb.configure(bg=bg,text=' ')
        #self.root.after(self.refresh_rate, self.draw)





# ball = Ball(canvas, "red",200,100)
# ball.draw())

# bb = {}
# for x in range (10) :
#     for y in range (5) :
#         bb[x,y] = Ball(canvas, "red",x,y,10)
#         bb[x,y].draw()
class BoardGame:
    def __init__(self,size,mx,my,color,gol,refresh_rate):
        self.root = tkinter.Tk()
        self.root.title = "Game"
        self.root.resizable(0,0)
        self.root.wm_attributes("-topmost", 1)
        self.size = size
        self.mx = mx
        self.my = my
        self.bb = {}
        self.color = color
        self.gol = gol
        self.refresh_rate = refresh_rate
        for x in range (mx) :
            for y in range (my) :
                self.bb[x,y] = Ball(self.root, color,x,y,size,gol,refresh_rate)
                self.bb[x,y].draw()
        self.sim()
        self.root.mainloop()

    def sim(self):
        self.gol.Scan()
        self.gol.commit()
        #self.canvas.after(self.refresh_rate, self.sim)
        for x in range (self.mx) :
            for y in range (self.my) :
                self.bb[x,y].draw()
        self.root.after(self.refresh_rate, self.sim)


