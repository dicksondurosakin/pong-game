from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self,x_pos,y_pos):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x_pos,y_pos)
        self.l_player = 0
        self.r_player = 0
        self.write(f"{self.l_player}:{self.r_player}",font=('Segoe UI',40,'normal'))

    def add_right(self):
        self.clear()
        self.r_player += 1
        self.write(f"{self.l_player}:{self.r_player}",font=('Segoe UI',40,'normal'))
        
    def add_left(self):
        self.clear()
        self.l_player += 1
        self.write(f"{self.l_player}:{self.r_player}",font=('Segoe UI',40,'normal'))

