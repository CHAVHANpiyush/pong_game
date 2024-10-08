

from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.xmove=10
        self.ymove=10
        self.move_speed=0.07

    def move(self):
        new_x=self.xcor()+self.xmove
        new_y=self.ycor()+self.ymove
        self.goto(new_x,new_y)
    def bounce_y(self):
        self.ymove*=-1
    def reposition(self):
        self.goto(0,0)
        self.move_speed=0.07
        self.xmove *= -1
    def bounce_x(self):
        self.xmove *= -1
        self.move_speed *= 0.9

