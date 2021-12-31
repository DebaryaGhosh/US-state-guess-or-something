from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.goto(250, 250)
        self.color("black")
        self.score = 0
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align = ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.update_scoreboard()