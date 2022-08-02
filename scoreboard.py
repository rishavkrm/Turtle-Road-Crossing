from turtle import Turtle



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color(187, 134, 252)
        self.level = 1
        self.penup()
        self.goto(0,260)
        self.update_level()
        self.hideturtle()

    def increase_level(self):
        self.level += 1

    def update_level(self):
        self.hideturtle()
        self.write(f"Level : {self.level}", move=False, align="center", font=("Courier", 30, "normal"))

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.color("orange")
        self.write(f"GAME OVER", move=False, align="center", font=("Courier", 24, "normal"))