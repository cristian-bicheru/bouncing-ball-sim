from tkinter import *
import time
import random

WIDTH = 1200
HEIGHT = 700
dT = 0.008           #delay between frames, 0.0166 ~ 60fps
gravity = 9.8/dT     #gravity value
bC = 0.9             #bounce efficiency (y)
bxC = 0.9            #bounce efficiency (x)
ballN = 30           #number of balls
ox = 600             #spawn offset x
oy = 175             #spawn offset y

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="black")
tk.title("bounce")
canvas.pack()

colors = ['red', 'green', 'blue', 'orange', 'yellow', 'cyan', 'magenta',
          'dodgerblue', 'turquoise', 'grey', 'gold', 'pink']

class Ball:
    def __init__(self):
        self.size = random.randrange(20, 40)
        color = random.choice(colors)
        self.shape = canvas.create_oval(ox, oy, self.size+ox, self.size+oy, fill=color)
        self.speedx = random.randint(1,27)/random.randint(1,10)*85*random.choice([-1,1])
        self.speedy = random.randint(1,35)/random.randint(1,10)*75*random.choice([-1,1])
        self.t = 0
        self.delayt = 0
        self.dT = dT

    def update(self):
        self.t = self.t + self.dT
        self.delayt = self.delayt + self.dT
        if abs(self.speedx) <= 0.1:
            self.speedx = 0
            self.delayt = 0
            self.dT = 0
        if abs(self.speedy) <= 0.1:
            self.speedy = 0
            self.t = 0
            self.dT = 0
        dy = self.speedy*self.t+0.5*gravity*self.t**2-self.speedy*(self.t-self.dT)-0.5*gravity*(self.t-self.dT)**2
        dx = self.speedx*self.t-self.speedx*(self.t-self.dT)
        canvas.move(self.shape, dx, dy)
        pos = canvas.coords(self.shape)
        if pos[2] >= WIDTH or pos[0] <= 0:
            if self.delayt >= 3*self.dT:
                self.speedx *= -bxC
                self.delayt = 0
        if pos[1] <= 0:
            if self.t >= 3*self.dT:
                self.speedy = -dy*bC*(1/dT)
                self.t = 0
                self.speedx *= bxC
        if pos[3] >= HEIGHT:
            if self.t >= 3*self.dT:
                self.speedy = -dy*bC*(1/dT)
                self.speedx *= bxC
                self.t = 0
       

balls = []
for i in range(ballN):
    balls.append(Ball())
while True:
    for ball in balls:
        ball.update()
    tk.update()
    time.sleep(dT)
