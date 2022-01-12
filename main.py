from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

my_screen = Screen()
my_screen.setup(width=800,height=600)
my_screen.bgcolor("black")

my_screen.tracer(0)
#listening and controlling the paddle
r_paddle = Paddle(385,0)
l_paddle = Paddle(-390,0)
my_screen.onkey(r_paddle.move_up, "Up")
my_screen.onkey(r_paddle.move_down, "Down")
my_screen.onkey(l_paddle.move_up, "w")
my_screen.onkey(l_paddle.move_down, "s")
my_screen.listen()

#creating the ball
ball = Ball()

#creating a scoreboard
scoreboard = ScoreBoard(-350,230)

#set speed 
speed = 0.1

while True:
    my_screen.tracer(1)
    time.sleep(speed)
    ball.move()
    if ball.xcor() >= 390:
        my_screen.tracer(0)
        scoreboard.add_left()
        ball.reset_ball()
        speed = 0.1
        my_screen.tracer(1)
    if ball.xcor() <= -390:
        my_screen.tracer(0)
        scoreboard.add_right()
        ball.reset_ball()
        speed = 0.1
        my_screen.tracer(1)
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.change_y()
        speed *= 0.9
    if ball.xcor() > 370 and ball.distance(r_paddle) < 50 or ball.xcor() < -370  and ball.distance(l_paddle) < 50:
        ball.change_x()
        speed *= 0.9
    

my_screen.mainloop()

