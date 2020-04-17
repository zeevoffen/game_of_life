import random

class game_of_life :
    DEAD=0
    ALIVE=1
    DIE = 2
    SPAWN = 3
    state_lookup = ['-DEADI-','-ALIVE-','-DIED!-','-SPAWN-']
    commit_table = [  DEAD,     ALIVE  ,  DEAD   ,  ALIVE  ]
    def ValidPos(self,x,y):
        if ((x<self.w) and (y<self.h) and (y>=0) and (x>=0)) : return True
        return False
    def UpdateState(self,x,y,state):
        if self.ValidPos(x,y) : self.m[x,y]=state
    def __init__(self,w,h):
        self.w=w
        self.h=h
        self.m={}
        for x in range(w):
            for y in range(h):
                self.m[x,y]=self.DEAD
    def populated(self,x,y):
        if not self.ValidPos(x,y) : return 0
        if ((self.m[x,y]==self.ALIVE) or (self.m[x,y]==self.DIE))  : return 1
        return 0
    def NumNeigbours(self,x,y):
        return (self.populated(x-1,y)   + self.populated(x+1,y) +   self.populated(x,y-1) + self.populated(x,y+1) +
                self.populated(x-1,y-1) + self.populated(x+1,y+1) + self.populated(x-1,y+1) + self.populated(x+1,y-1))
    def Scan(self):
        for x in range(self.w):
            for y in range(self.h):
                if (self.NumNeigbours(x,y)==3) and (self.populated(x,y)==0): self.UpdateState(x,y,self.SPAWN)
                if (self.NumNeigbours(x,y)>3) and (self.populated(x,y)==1): self.UpdateState(x,y,self.DIE)
                if (self.NumNeigbours(x,y)<2) and (self.populated(x,y)==1): self.UpdateState(x,y,self.DIE)
    def commit(self):
        for x in range(self.w):
            for y in range(self.h):
                self.UpdateState(x,y,self.commit_table[self.m[x,y]])
    def exists(self,x,y):
        if self.ValidPos(x,y) and (self.populated(x,y)==1) : return True
        return False
    def rand_board(self,alive_prob) :
        for y in range(self.h):
            for x in range(self.w):
                if (random.random() < alive_prob) : self.UpdateState(x,y,self.ALIVE)
    def __str__(self):
        s=''
        for y in range(self.h):
            for x in range(self.w):
                s+=str(self.state_lookup[self.m[x,y]])
            s+="\n"
        return s

import grphx as gr

class gol():
    def __init__(self,MX,MY,square_size,color,initial_population):
        self.MX=MX
        self.MY=MY
        self.gl = game_of_life(MX,MY)
        self.gl.rand_board(initial_population)
        self.bg = gr.BoardGame(size=square_size,mx=MX,my=MY,color=color,gol=self.gl,refresh_rate=10)

