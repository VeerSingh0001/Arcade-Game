import turtle

screen = turtle.Screen()
screen.tracer()
screen.delay(10)


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed(1)
        self.move()

    def move(self, ):
        # current_x = self.x_move
        # current_y = self.y_move
        # print(current_x, current_y)

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self, x=1, y=1):
        self.x_move *= x
        self.y_move *= y
        self.move_speed *= 0.9
        # current_x = self.x_move
        # current_y = self.y_move
        # print(current_x, current_y)
        # print(self.position())

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce(x=-1)
