from mmap import ALLOCATIONGRANULARITY
from turtle import Turtle

ALIGNMENT = "center"

class StateName(Turtle):
    
    def __init__(self):
        super().__init__()
        self.us_state_name = ""
        self.color("black")
        self.x_cor = 0
        self.y_cor = 0
        self.penup()
        self.hideturtle()

    def set_name(self, name, x, y):
        self.x_cor = int(x)
        self.y_cor = int(y)
        
        self.goto(self.x_cor, self.y_cor)
        self.write(name, align=ALIGNMENT)
