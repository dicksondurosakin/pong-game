from turtle import Turtle

class Ball(Turtle):
    '''creating the model of a ball'''
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_distance = 10
        self.y_distance = 10

    def move(self):
        new_x = self.xcor() + self.x_distance
        new_y = self.ycor() + self.y_distance
        self.goto(new_x,new_y)
    
    def change_y(self):
        self.y_distance *= -1
        # print(self.pos()) 
    
    def change_x(self):
        self.x_distance *= -1
        print(self.pos())

    def reset_ball(self):
        self.goto(0,0) 