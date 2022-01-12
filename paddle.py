from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,x_pos,y_pos):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.shape("square")
        self.turtlesize(0.5,4)
        self.penup()
        self.setheading(90)
        self.color("white")
        self.goto(self.x_pos,self.y_pos)
    
    def move_up(self):
        self.forward(10)
        

    def move_down(self):
        self.backward(10)
        