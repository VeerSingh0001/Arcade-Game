import random
import turtle

screen = turtle.Screen()
screen.tracer()
screen.delay(1)


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.055
        self.shape("circle")
        self.penup()
        self.color("#FDDE55")
        self.speed(1)
        self.move()

    def move(self, ):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self, x=1, y=1):
        self.x_move *= x
        self.y_move *= y
        self.move_speed -= 0.001

    def reset_position(self):
        y = random.randint(-200, 200)
        self.goto(0, y)
        self.move_speed = 0.055
        self.bounce(x=-1)
